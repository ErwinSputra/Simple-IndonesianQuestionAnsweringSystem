import spacy
from collections import Counter
import regex
import operator


class AnswerExtraction:
    def __init__(self, docx, labeling):
        self.docx = docx
        self.labeling = labeling

    def answer(self, query):
        model_spacy = "model_ner_spacy"
        print("Loading from", model_spacy)
        ner = spacy.load(model_spacy)
        doc = ner(self.docx)
        entity = [(ent.text, ent.label_) for ent in doc.ents]
        lbl = []
        for kata, label in entity:
            if label == self.labeling:
                lbl.append(kata)
        cnt = Counter(lbl)
        word = max(cnt.items(), key=operator.itemgetter(1))[0]
        answer = self.pattern(query, word)
        return answer

    def pattern(self, query, answer):
        if self.labeling == "LOCATION":
            result = regex.sub(r'\bdimana\b\s+', "", query)
            result = result.capitalize()
            res = result + " di " + answer
            return res
        elif self.labeling == "PERSON":
            result = regex.sub(r'\bsiapa\b\s+', "", query)
            result = result.capitalize()
            res = result + " adalah " + answer
            return res
        elif self.labeling == "TIME":
            result = regex.sub(r'\bkapan\b\s+', "", query)
            result = result.capitalize()
            res = result + " pada {}".format(answer)
            return res

