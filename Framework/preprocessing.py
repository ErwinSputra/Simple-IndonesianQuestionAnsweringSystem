import regex


class PreProcessing:
    def __init__(self, teks):
        self.teks = teks

    def sent_segmentation(self):
        token = regex.split(r"[?!\.]", self.teks)
        str1 = ""
        for ele in token:
            str1 += ele
        return str1

