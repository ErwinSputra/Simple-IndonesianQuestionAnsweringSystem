class Input:
    def __init__(self, query):
        self.query = query

    def normalization(self):
        query = self.query.lower()
        return query

