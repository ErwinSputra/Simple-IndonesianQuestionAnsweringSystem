from input import Input
from doc_collection import DocumentCollection
from preprocessing import PreProcessing
from question_analysis import QuestionAnalysis
from answer_extraction import AnswerExtraction


class IQAS:
    def __init__(self, question):
        self.question = question

    def answer(self):
        query = Input(self.question)
        query = query.normalization()
        label = QuestionAnalysis(query)
        label = label.labeling()
        doc = DocumentCollection(query)
        doc = doc.webpage()
        text = PreProcessing(doc)
        text = text.sent_segmentation()
        string = AnswerExtraction(text, label)
        answer = string.answer(query)
        print(answer)

