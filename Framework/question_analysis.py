class QuestionAnalysis:
    def __init__(self, string):
        self.string = string

    def labeling(self):
        label = ""
        if "siapa" in self.string:
            label = "PERSON"
        elif "kapan" in self.string:
            label = "TIME"
        elif "dimana" in self.string:
            label = "LOCATION"
        return label

    # def q_classification(self):

