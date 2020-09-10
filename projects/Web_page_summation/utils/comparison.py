
# https://github.com/chakki-works/sumeval
# https://github.com/Tian312/awesome-text-summarization

from sumeval.metrics.rouge import RougeCalculator
from sumeval.metrics.bleu import BLEUCalculator


def eval_rouges(refrence_summary, model_summary):
    # refrence_summary = "tokyo shares close up #.## percent"
    # model_summary = "tokyo stocks close up # percent to fresh record high"

    rouge = RougeCalculator(stopwords=True, lang="en")

    rouge_1 = rouge.rouge_n(
        summary=model_summary,
        references=refrence_summary,
        n=1)

    rouge_2 = rouge.rouge_n(
        summary=model_summary,
        references=[refrence_summary],
        n=2)

    rouge_l = rouge.rouge_l(
        summary=model_summary,
        references=[refrence_summary])

    # You need spaCy to calculate ROUGE-BE

    rouge_be = rouge.rouge_be(
        summary=model_summary,
        references=[refrence_summary])

    bleu = BLEUCalculator()
    bleu_score = bleu.bleu(summary=model_summary,
                           references=[refrence_summary])

    # print("ROUGE-1: {}, ROUGE-2: {}, ROUGE-L: {}, ROUGE-BE: {}".format(
    #    rouge_1, rouge_2, rouge_l, rouge_be
    # ).replace(", ", "\n"))

    return rouge_1, rouge_2, rouge_l, rouge_be, bleu_score

# rouge_1, rouge_2,rouge_l,rouge_be = eval_rouges( "tokyo shares close up #.## percent",
#                                                "tokyo stocks close up # percent to fresh record high")
#
# print("ROUGE-1: {}, ROUGE-2: {}, ROUGE-L: {}, ROUGE-BE: {}".format(
#        rouge_1, rouge_2, rouge_l, rouge_be
#    ).replace(", ", "\n"))
