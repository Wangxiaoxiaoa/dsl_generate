import dspy
from src.tools.read_file import read_file


class DspyTransformSignature(dspy.Signature):
    prompt = dspy.InputField(desc="完整的提示词，包括antlr语法规则、antlr语法辅助说明、dsl语句和对应的人类自然语言语句")
    error_msg = dspy.OutputField(desc="模型修改后仍然错误的人类自然语言语句信息")
    result = dspy.OutputField(desc="模型修改后正确的人类自然语言语句信息")

class Stage3Transform(dspy.Module):
    def __init__(self, model_name, api_key, url, prompt_template):
        super().__init__()
        self.prompt_template = prompt_template
        # model_name = "openai/" + model_name
        # self.llm = dspy.LM(model_name, api_key=api_key, api_base=url)
        # dspy.configure(lm=self.llm)
        self.predictor = dspy.Predict(DspyTransformSignature)

    def forward(self, grammar, grammar_help, dsl_sentence, nl_sentence, error_msg):
        prompt = self.prompt_template.format(
            grammar=grammar,
            grammar_help=grammar_help,
            dsl_sentence=dsl_sentence,
            nl_sentence=nl_sentence,
        )
        response = self.predictor(prompt=prompt,error_msg=error_msg)
        return response.result.strip()


def transform(t_model_name, t_api_key, t_url, grammar_path, grammar_help_path, dsl_sentence, nl_sentence,error_msg=None):
    verifier = Stage3Transform(model_name=t_model_name, api_key=t_api_key, url=t_url, prompt_template=read_file(grammar_path))
    return verifier(
        grammar=read_file(grammar_path),
        grammar_help=read_file(grammar_help_path),
        dsl_sentence=dsl_sentence,
        nl_sentence=nl_sentence,
        error_msg=error_msg 
    )