import json
import dspy
from dspy.teleprompt import BootstrapFewShot

class DSL2NL_General(dspy.Signature):    
    prompt = dspy.InputField(desc="完整的提示词，包括antlr语法规则、antlr语法辅助说明、antlr语句以及一个人类角色")
    result = dspy.OutputField(desc="转换后的人类自然语言")

class DSL2NL_General(dspy.Module):

    def __init__(self, model_name, api_key, url, prompt_template):
        super().__init__()
        self.prompt_template = prompt_template
        model_name = "openai/" + model_name
        self.llm = dspy.LM(model_name, api_key=api_key, api_base=url)
        dspy.configure(lm=self.llm)
        self.predictor = dspy.Predict(DSL2NL_General)

    def forward(self, grammar, antlr_help, dsl_sentence, human_role):
        prompt = self.prompt_template.format(
            grammar=grammar,
            antlr_help=antlr_help,
            sentence=dsl_sentence,
            human_role=human_role
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
        self.predictor = dspy.Predict(DSL2NL_General)

    def load_dataset(self, dataset_path):
        with open(dataset_path, 'r', encoding='utf-8') as f:
            dataset = json.load(f)
        examples = []
        for data in dataset:
            prompt = self.prompt_template.format(
                grammar=data["grammar"],
                antlr_help=data["antlr_help"],
                sentence=data["dsl_sentence"],
                human_role=data["human_role"]
            )
            examples.append(dspy.Example(prompt=prompt, result=data["nl_sentence"]).with_inputs("prompt"))
        return examples

    def forward(self, grammar, antlr_help, dsl_sentence, human_role, train_dataset_path):
        examples = self.load_dataset(train_dataset_path)
        teleprompter = BootstrapFewShot(metric=dspy.evaluate.answer_exact_match, max_bootstrapped_examples=5)
        compiled_predictor = teleprompter.compile(self.predictor, trainset=examples)
        prompt = self.prompt_template.format(
            grammar=grammar,
            antlr_help=antlr_help,
            sentence=dsl_sentence,
            human_role=human_role,
        )
        response = compiled_predictor(prompt=prompt)
        return response.result.strip()


def dsl2nl(model_name, api_key, url, grammar,prompt, antlr_help, dsl_sentence, human_role, cot_sample="", train_prompt=False, train_dataset_path=""):
    if not train_prompt:
        dsl2nl = DSL2NL_General(model_name=model_name, api_key=api_key, url=url, prompt_template=prompt)
        return dsl2nl(
            grammar=grammar,
            antlr_help=antlr_help,
            dsl_sentence=dsl_sentence,
            human_role=human_role,
            cot_sample=cot_sample,
        )
    else:
        dsl2nl = DSL2NL_Train(model_name=model_name, api_key=api_key, url=url, prompt_template=prompt)
        return dsl2nl(
            grammar=grammar,
            antlr_help=antlr_help,
            dsl_sentence=dsl_sentence,
            human_role=human_role,
            train_dataset_path=train_dataset_path,
        )
