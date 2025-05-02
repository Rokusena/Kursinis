
class WordList:
    def __init__(self, filepath):
        self.words = self.load_words(filepath)

    def load_words(self, filepath):
        with open(filepath, 'r') as f:
            return [line.strip().lower() for line in f if len(line.strip()) == 5]

    def filter_words(self, possible_words):
        self.words = [word for word in self.words if word in possible_words]

    def get_words(self):
        return self.words
