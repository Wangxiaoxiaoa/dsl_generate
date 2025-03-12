import dspy
from dspy import ChainOfThought, Signature, InputField, OutputField, Module, ReAct
import dspy.evaluate
from src.tools.read_file import read_file
from dspy.teleprompt import BootstrapFewShot
from src.tools.dspy_metric import rouge_compute_tokenizer
from src.parse.parse import CFG_ParserTool

class StatementGeneration(Signature):
    prompt_template = InputField(desc="提示词模板，包含待填充的参数占位符")
    generated_stmt = OutputField(desc="生成的符合语法的语句")

class ReactProcess(Signature):
    prompt_template = InputField(desc="原始提示词模板，包含待填充的参数占位符")
    error_stmt = InputField(desc="存在语法错误的语句")
    corrected_stmt = OutputField(desc="修正后的符合语法的语句")

class CoTWithValidation(Module):
    def __init__(self,model_name, api_key, url, max_retries=3, special_tokens=[]):
        super().__init__()
        model_name = "openai/" + model_name
        self.llm = dspy.LM(model_name, api_key=api_key, api_base=url)
        dspy.configure(lm=self.llm)
        self.generate = ChainOfThought(StatementGeneration)
        self.react_correct = dspy.Predict(ReactProcess)
        self.max_retries = max_retries
        self.special_tokens = special_tokens  

    def clean_special_tokens(self, stmt):
        for token in self.special_tokens:
            stmt = stmt.replace(token, "")
        return stmt

    def forward(self, prompt_template, grammar, grammar_help, sentence, cot_sample_path, parser_dir):
        if cot_sample_path:
            cot_sample = read_file(cot_sample_path)
        else:
            cot_sample = None
        prompt = prompt_template.format(
            grammar=grammar,
            grammar_help=grammar_help,
            sentence=sentence,
            special_token1=self.special_tokens[0],
            special_token2=self.special_tokens[1],
            cot_sample=cot_sample
        )
        generation = self.generate(
            prompt_template=prompt,
        )
        parser = CFG_ParserTool(grammar, parser_dir)
        for _ in range(self.max_retries):
            cleaned_stmt = self.clean_special_tokens(generation.generated_stmt) if self.special_tokens else generation.generated_stmt
            if parser.parse(cleaned_stmt):
                return cleaned_stmt, True

            correction = self.react_correct(
                prompt_template=prompt,
                error_stmt=generation.generated_stmt
            )
            generation.generated_stmt = correction.corrected_stmt
        cleaned_stmt = self.clean_special_tokens(generation.generated_stmt)
        if not parser.parse(cleaned_stmt):
            return cleaned_stmt, False
        else:
            return cleaned_stmt, True


class CoTWithValidation_Train(Module):
    def __init__(self, model_name, api_key, url, max_retries=3, special_tokens=[]):
        super().__init__()
        model_name = "openai/" + model_name
        self.llm = dspy.LM(model_name, api_key=api_key, api_base=url)
        dspy.configure(lm=self.llm)
        self.max_retries = max_retries
        self.special_tokens = special_tokens
        self.cot_module = CoTWithValidation(model_name, api_key, url, max_retries, special_tokens)

    def forward(self, prompt_template, grammar, grammar_help, sentence, cot_sample_path, train_dataset_path, train_metric, train_metric_threshold, parser_dir):
        train_data = read_file(train_dataset_path)
        if train_metric == "rouge":
            teleprompter = BootstrapFewShot(metric=rouge_compute_tokenizer,metric_threshold=train_metric_threshold)
        else:
            raise ValueError(f"Unsupported metric: {train_metric}")
        optimized_cot = teleprompter.compile(self.cot_module, trainset=train_data)
        complete_sentence, result_flag = optimized_cot(prompt_template, grammar, grammar_help, sentence, cot_sample_path, parser_dir)
        return complete_sentence, result_flag

def fill_regex(
    model_name,
    api_key,
    url,
    prompt,
    grammar,
    grammar_help,
    sentence,
    max_retries,
    special_token,
    cot_sample_path,
    train_prompt,
    train_dataset_path,
    train_metric,
    train_metric_threshold,
    parser_dir
):
    if train_prompt:
        train_prompt_cot = CoTWithValidation_Train(model_name, api_key, url, max_retries=max_retries, special_tokens=special_token)
        complete_sentence, result_flag = train_prompt_cot(prompt, grammar, grammar_help, sentence, cot_sample_path, train_dataset_path,train_metric,train_metric_threshold, parser_dir)
        return complete_sentence, result_flag
    else:
        cot = CoTWithValidation(model_name, api_key, url, max_retries=max_retries, special_tokens=special_token)
        complete_sentence, result_flag = cot(prompt, grammar, grammar_help, sentence, cot_sample_path, parser_dir)
        return complete_sentence, result_flag
