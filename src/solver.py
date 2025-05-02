

from collections import Counter

class WordleSolver:
    def __init__(self, wordlist):
        self.full_wordlist = wordlist.get_words()
        self.possible_words = self.full_wordlist.copy()

    def guess(self):
        # Strategy: return the word with the most common letters
        return self.best_guess()
    
    def update_possible_words(self, guess, feedback):
        def is_valid(word):
            for i in range(5):
                g_letter = guess[i]
                f = feedback[i]
                w_letter = word[i]

                if f == 'G':
                    if w_letter != g_letter:
                        return False
                elif f == 'Y':
                    if g_letter not in word or word[i] == g_letter:
                        return False
                elif f == 'B':
                    # If the letter occurs elsewhere as G or Y, allow it
                    if g_letter in word:
                        # Count how many times this letter was marked G or Y in the guess
                        allowed_count = sum(
                            1 for j in range(5)
                            if guess[j] == g_letter and feedback[j] in ('G', 'Y')
                        )
                        if word.count(g_letter) > allowed_count:
                            return False
            return True

        self.possible_words = [w for w in self.possible_words if is_valid(w)]


    def best_guess(self):
        letter_freq = Counter()
        for word in self.possible_words:
            for letter in set(word):
                letter_freq[letter] += 1

        def score(word):
            return sum(letter_freq[letter] for letter in set(word))

        return max(self.possible_words, key=score)
    
    def top_guesses(self, n=10):
        letter_freq = Counter()
        for word in self.possible_words:
            for letter in set(word):
                letter_freq[letter] += 1

        def score(word):
            return sum(letter_freq[letter] for letter in set(word))

        return sorted(self.possible_words, key=score, reverse=True)[:n]

