from rouge_score import rouge_scorer
from rouge_chinese import Rouge
import jieba

def rouge_compute_jieba(references,predictions, trace=None):
    metric = Rouge()
    predictions = [' '.join(jieba.cut(predictions))]
    references = [' '.join(jieba.cut(references))]
    predictions = [i if i else '__PREDPLACEHOLDER__' for i in predictions]
    references = [i if i else '__REFRPLACEHOLDER__' for i in references]
    rouge_scores = metric.get_scores(predictions, references, avg=True)
    return rouge_scores['rouge-l']['f']

def rouge_compute_tokenizer(references, predictions, trace=None):
    scorer = rouge_scorer.RougeScorer(['rougeL'], use_stemmer=True)
    score = scorer.score(predictions, references)
    return score['rougeL']['fmeasure']