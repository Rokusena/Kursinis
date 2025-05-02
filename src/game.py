
class WordleGame:
    def __init__(self, target_word):
        self.target_word = target_word.lower()

    def check_guess(self, guess):
        guess = guess.lower()
        result = ['' for _ in range(5)]
        target_copy = list(self.target_word)

     
        for i in range(5):
            if guess[i] == self.target_word[i]:
                result[i] = 'G'
                target_copy[i] = None

       
        for i in range(5):
            if result[i] == '':
                if guess[i] in target_copy:
                    result[i] = 'Y'
                    target_copy[target_copy.index(guess[i])] = None
                else:
                    result[i] = 'B'

        return result
