import dspy

class RationalityVerification(dspy.Signature):
    prompt = dspy.InputField(desc="完整的提示词，包括语法规则、辅助说明、语句和特殊token")
    result = dspy.OutputField(desc="判断结果，只能是True或False")

class RationalityVerifier(dspy.Module):
    def __init__(self, model_name, api_key, url, prompt_template):
        super().__init__()
        self.prompt_template = prompt_template
        model_name = "openai/" + model_name
        self.llm = dspy.LM(model_name, api_key=api_key, api_base=url)
        dspy.configure(lm=self.llm)
        self.predictor = dspy.ReAct(RationalityVerification)

    def forward(self, grammar, antlr_help, sentence, special_token1, special_token2):
        prompt = self.prompt_template.format(
            grammar=grammar,
            antlr_help=antlr_help,
            sentence=sentence,
            special_token1=special_token1,
            special_token2=special_token2
        )
        response = self.predictor(prompt=prompt)
        if response.result.strip() in ["True", "False"]:
            return response.result.strip()
        elif response.result.strip().split()[-1] in ["True", "False"]:
            return response.result.strip().split()[-1]
        else:
            return "False"


def verify(model_name, api_key, url, grammar,prompt, antlr_help, sentence, special_token:list):
    verifier = RationalityVerifier(model_name=model_name, api_key=api_key, url=url, prompt_template=prompt)
    return verifier(
        grammar=grammar,
        antlr_help=antlr_help,
        sentence=sentence,
        special_token1=special_token[0], 
        special_token2=special_token[1]
    )