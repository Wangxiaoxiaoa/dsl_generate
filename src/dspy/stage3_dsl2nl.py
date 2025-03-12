import json
import dspy
from dspy.teleprompt import BootstrapFewShot
from src.tools.dspy_metric import rouge_compute_jieba
from src.tools.read_file import read_file, read_roles

class DSL2NL_General_Signature(dspy.Signature):    
    prompt = dspy.InputField(desc="完整的提示词，包括antlr语法规则、antlr语法辅助说明、antlr语句以及一个人类角色")
    result = dspy.OutputField(desc="转换后的人类自然语言")

class DSL2NL_General(dspy.Module):

    def __init__(self, model_name, api_key, url, prompt_template):
        super().__init__()
        self.prompt_template = prompt_template
        model_name = "openai/" + model_name
        self.llm = dspy.LM(model_name, api_key=api_key, api_base=url)
        dspy.configure(lm=self.llm)
        self.predictor = dspy.Predict(DSL2NL_General_Signature)

    def forward(self, grammar, grammar_help, dsl_sentence, human_role,cot_sample):
        prompt = self.prompt_template.format(
            grammar=grammar,
            grammar_help=grammar_help,
            sentence=dsl_sentence,
            human_role=human_role,
            cot_sample=cot_sample
        )
        response = self.predictor(prompt=prompt)
        return response.result.strip()


class DSL2NL_Train(dspy.Module):
    def __init__(self, model_name, api_key, url, prompt_template):
        super().__init__()
        self.prompt_template = prompt_template
        model_name = "openai/" + model_name
        self.llm = dspy.LM(model_name, api_key=api_key, api_base=url)
        dspy.configure(lm=self.llm)
        self.predictor = dspy.Predict(DSL2NL_General_Signature)

    def load_dataset(self, dataset_path):
        with open(dataset_path, 'r', encoding='utf-8') as f:
            dataset = json.load(f)
        examples = []
        for data in dataset:
            prompt = self.prompt_template.format(
                grammar=data["grammar"],
                grammar_help=data["grammar_help"],
                sentence=data["dsl_sentence"],
                human_role=data["human_role"]
            )
            examples.append(dspy.Example(prompt=prompt, result=data["nl_sentence"]).with_inputs("prompt"))
        return examples

    def forward(self, grammar, grammar_help, dsl_sentence, human_role, train_dataset_path, train_metric, train_metric_threshold):
        examples = self.load_dataset(train_dataset_path)
        if train_metric == "rouge":
            teleprompter = BootstrapFewShot(metric=rouge_compute_jieba, metric_threshold=train_metric_threshold)
        else:
            raise ValueError(f"Unsupported metric: {train_metric}")
        compiled_predictor = teleprompter.compile(self.predictor, trainset=examples)
        prompt = self.prompt_template.format(
            grammar=grammar,
            grammar_help=grammar_help,
            sentence=dsl_sentence,
            human_role=human_role,
        )
        response = compiled_predictor(prompt=prompt)
        return response.result.strip()


def dsl2nl(
            d2n_model_name,
            d2n_prompt_path,
            d2n_api_key,
            d2n_url,
            d2n_cot_sample_path,
            d2n_train_prompt,
            d2n_train_dataset_path,
            d2n_train_metric,
            d2n_train_metric_threshold,
            grammar_path,
            grammar_help_path,
            complete_sentence,
            roles_path,
):
    
    if not d2n_train_prompt:
        dsl2nl = DSL2NL_General(model_name=d2n_model_name, api_key=d2n_api_key, url=d2n_url, prompt_template=read_file(d2n_prompt_path))
        return dsl2nl(
            grammar=read_file(grammar_path),
            grammar_help=read_file(grammar_help_path),
            dsl_sentence=complete_sentence,
            human_role=read_roles(roles_path),
            cot_sample=read_file(d2n_cot_sample_path) if d2n_cot_sample_path else "",
        )
    else:
        dsl2nl = DSL2NL_Train(model_name=d2n_model_name, api_key=d2n_api_key, url=d2n_url, prompt_template=read_file(d2n_prompt_path))
        return dsl2nl(
            grammar=read_file(grammar_path),
            grammar_help=read_file(grammar_help_path),
            dsl_sentence=complete_sentence,
            human_role=read_roles(roles_path),
            train_dataset_path=d2n_train_dataset_path,
            train_metric=d2n_train_metric,
            train_metric_threshold=d2n_train_metric_threshold
        )
