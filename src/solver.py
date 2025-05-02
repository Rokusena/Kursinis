

from collections import Counter

class WordleSolver:
    def __init__(self, wordlist):
        self.full_wordlist = wordlist.get_words()
        self.possible_words = self.full_wordlist.copy()

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
                    allowed_count = sum(
                        1 for j in range(5)
                        if guess[j] == g_letter and feedback[j] in ('G', 'Y')
                    )
                    if word.count(g_letter) > allowed_count:
                        return False
            return True

        self.possible_words = [w for w in self.possible_words if is_valid(w)]


# Strategy base class and implementation (Strategy Pattern)
class SolverStrategy:
    def top_guesses(self, possible_words, n):
        raise NotImplementedError("Subclasses must implement this method")


class FrequencySolverStrategy(SolverStrategy):
    def top_guesses(self, possible_words, n=10):
        letter_freq = Counter()
        for word in possible_words:
            for letter in set(word):
                letter_freq[letter] += 1

        def score(word):
            return sum(letter_freq[letter] for letter in set(word))

        return sorted(possible_words, key=score, reverse=True)[:n]


class StrategyContext:
    def __init__(self, strategy: SolverStrategy):
        self.strategy = strategy

    def set_strategy(self, strategy: SolverStrategy):
        self.strategy = strategy

    def top_guesses(self, possible_words, n=10):
        return self.strategy.top_guesses(possible_words, n)
