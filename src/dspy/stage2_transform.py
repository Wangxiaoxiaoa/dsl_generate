import dspy
from src.tools.read_file import read_file

class DspyTransformSignature(dspy.Signature):
    prompt = dspy.InputField(desc="完整的提示词，包括antlr语法规则、antlr语法辅助说明、错误的语句和特殊token")
    error_msg = dspy.OutputField(desc="模型修改后仍然错误的语句信息")    
    result = dspy.OutputField(desc="模型修改后正确的语句信息")

class Transform(dspy.Module):
    def __init__(self, model_name, api_key, url, prompt_template):
        super().__init__()
        self.prompt_template = prompt_template
        model_name = "openai/" + model_name
        self.llm = dspy.LM(model_name, api_key=api_key, api_base=url)
        dspy.configure(lm=self.llm)
        self.predictor = dspy.Predict(DspyTransformSignature)

    def forward(self, grammar, grammar_help, sentence, special_token1, special_token2,error_msg):
        prompt = self.prompt_template.format(
            grammar=grammar,
            grammar_help=grammar_help,
            sentence=sentence,
            special_token1=special_token1,
            special_token2=special_token2,
        )
        response = self.predictor(prompt=prompt,error_msg=error_msg)
        return response.result.strip()


def transform(model_name, api_key, url, grammar,prompt, grammar_help, sentence, special_token:list,error_msg=None):
    verifier = Transform(model_name=model_name, api_key=api_key, url=url, prompt_template=prompt)
    return verifier(
        grammar=grammar,
        grammar_help=grammar_help,
        sentence=sentence,
        special_token1=special_token[0], 
        special_token2=special_token[1],
        error_msg=error_msg,
    )