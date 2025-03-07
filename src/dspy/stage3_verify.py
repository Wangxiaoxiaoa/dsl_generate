import dspy

class Verification(dspy.Signature):    
    prompt = dspy.InputField(desc="完整的提示词，包括语法规则、辅助说明、语句以及人类自然语言")
    result = dspy.OutputField(desc="判断结果，只能是True或False")

class Verifier(dspy.Module):

    def __init__(self, model_name, api_key, url, prompt_template):
        super().__init__()
        self.prompt_template = prompt_template
        model_name = "openai/" + model_name
        self.llm = dspy.LM(model_name, api_key=api_key, api_base=url)
        dspy.configure(lm=self.llm)
        self.predictor = dspy.ReAct(Verification)

    def forward(self, grammar, antlr_help, dsl_sentence, nl_sentence):
        prompt = self.prompt_template.format(
            grammar=grammar,
            antlr_help=antlr_help,
            sentence=dsl_sentence,
            natural_language=nl_sentence
        )
        response = self.predictor(prompt=prompt)
        if response.result.strip() in ["True", "False"]:
            return response.result.strip()
        elif response.result.strip().split()[-1] in ["True", "False"]:
            return response.result.strip().split()[-1]
        else:
            return "False"


def verify(model_name, api_key, url, grammar,prompt, antlr_help, dsl_sentence, nl_sentence):
    verifier = Verifier(model_name=model_name, api_key=api_key, url=url, prompt_template=prompt)
    return verifier(
        grammar=grammar,
        antlr_help=antlr_help,
        dsl_sentence=dsl_sentence,
        nl_sentence=nl_sentence
    )