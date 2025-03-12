import dspy

class RationalityVerificationSignature(dspy.Signature):
    prompt = dspy.InputField(desc="完整的提示词，包括语法规则、辅助说明、语句和特殊token")
    result = dspy.OutputField(desc="判断结果，只能是True或False")

class RationalityVerifier(dspy.Module):
    def __init__(self, model_name, api_key, url, prompt_template):
        super().__init__()
        self.prompt_template = prompt_template
        # model_name = "openai/" + model_name
        # self.llm = dspy.LM(model_name, api_key=api_key, api_base=url)
        # dspy.configure(lm=self.llm)
        self.predictor = dspy.Predict(RationalityVerificationSignature)

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
        
    def forward(self, grammar, grammar_help, sentence, special_token1, special_token2):
        prompt = self.prompt_template.format(
            grammar=grammar,
            grammar_help=grammar_help,
            sentence=sentence,
            special_token1=special_token1,
            special_token2=special_token2
        )
        response = self.predictor(prompt=prompt)
        return self.judge(response)


def verify(model_name, api_key, url, grammar, grammar_help, sentence, prompt, special_token:list):
    verifier = RationalityVerifier(model_name=model_name, api_key=api_key, url=url, prompt_template=prompt)
    return verifier(
        grammar=grammar,
        grammar_help=grammar_help,
        sentence=sentence,
        special_token1=special_token[0], 
        special_token2=special_token[1]
    )