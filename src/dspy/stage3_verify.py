import dspy
from src.tools.read_file import read_file


class VerificationSignature(dspy.Signature):    
    prompt = dspy.InputField(desc="完整的提示词，包括语法规则、辅助说明、语句以及人类自然语言")
    result = dspy.OutputField(desc="判断结果，只能是True或False")

class Verifier(dspy.Module):

    def __init__(self, model_name, api_key, url, prompt_template):
        super().__init__()
        self.prompt_template = prompt_template
        model_name = "openai/" + model_name
        self.llm = dspy.LM(model_name, api_key=api_key, api_base=url)
        dspy.configure(lm=self.llm)
        self.predictor = dspy.Predict(VerificationSignature)

    def judge(self, response):
        true_answers = ["True", "TRUE", "true", "正确", "对", "是", "yes", "Yes", "YES"]
        false_answers = ["False", "FALSE", "false", "错误", "错", "不对", "No", "NO", "no"]

        result = response.result.strip()
        result_last_word = result.split()[-1] if result.split() else ""

        if result in true_answers or result_last_word in true_answers:
            return True
        elif result in false_answers or result_last_word in false_answers:
            return False
        else:
            return False

    def forward(self, grammar, grammar_help, dsl_sentence, nl_sentence):
        prompt = self.prompt_template.format(
            grammar=grammar,
            grammar_help=grammar_help,
            sentence=dsl_sentence,
            natural_language=nl_sentence
        )
        response = self.predictor(prompt=prompt)
        return self.judge(response)


def verify(model_name, api_key, url, prompt_path, grammar_path, grammar_help_path, dsl_sentence, nl_sentence):
    verifier = Verifier(model_name=model_name, api_key=api_key, url=url, prompt_template=read_file(prompt_path))
    return verifier(
        grammar=read_file(grammar_path),
        grammar_help=read_file(grammar_help_path),
        dsl_sentence=dsl_sentence,
        nl_sentence=nl_sentence
    )