# wordle_solver_oop/test/test_solver.py

import unittest
from src.feedback import generate_feedback
from src.solver import WordleSolver
from src.wordlist import WordList

class TestFeedbackLogic(unittest.TestCase):
    def test_exact_match(self):
        self.assertEqual(generate_feedback("crane", "crane"), ['G', 'G', 'G', 'G', 'G'])

    def test_partial_match(self):
        self.assertEqual(generate_feedback("cared", "crane"), ['G', 'Y', 'Y', 'Y', 'B'])

    def test_no_match(self):
        self.assertEqual(generate_feedback("blush", "crane"), ['B', 'B', 'B', 'B', 'B'])

    def test_duplicate_handling(self):
        self.assertEqual(generate_feedback("eerie", "serve"), ['B', 'G', 'G', 'B', 'G'])

class TestWordleSolver(unittest.TestCase):
    def setUp(self):
        self.wordlist = WordList("data/words.txt")
        self.solver = WordleSolver(self.wordlist)
        self.guesses = set()

    def test_possible_words_reduce_after_feedback(self):
        original_len = len(self.solver.possible_words)
        self.solver.update_possible_words("blush", ['B', 'B', 'B', 'B', 'B'])
        new_len = len(self.solver.possible_words)
        self.assertLess(new_len, original_len)

    def test_invalid_letters_removed(self):
        self.solver.update_possible_words("blush", ['B', 'B', 'B', 'B', 'B'])
        for word in self.solver.possible_words:
            for letter in "blush":
                self.assertNotIn(letter, word)

    def test_correct_letter_position(self):
        self.solver.update_possible_words("cared", ['G', 'B', 'B', 'B', 'B'])
        for word in self.solver.possible_words:
            self.assertEqual(word[0], 'c')

    def test_wrong_position_letters_present(self):
        self.solver.update_possible_words("cared", ['B', 'Y', 'B', 'B', 'B'])
        for word in self.solver.possible_words:
            self.assertIn('a', word)
            self.assertNotEqual(word[1], 'a')

    def test_repeated_guess_handling(self):
        guess = "alert"
        self.guesses.add(guess)
        self.assertIn(guess, self.guesses)
        # simulate repeated entry
        self.assertTrue(guess in self.guesses)

    def test_invalid_symbols_or_numbers(self):
        invalid_words = ["a1ert", "al!rt", "ale", "", "12345"]
        for word in invalid_words:
            is_valid = word.isalpha() and len(word) == 5
            self.assertFalse(is_valid, msg=f"Word '{word}' should be invalid")

    def test_invalid_feedback_characters(self):
        valid = ["GGGGG", "BGYBG"]
        invalid = ["GGGGX", "12345", "GYB!!", "AABBB", "BBGGR"]
        for fb in valid:
            is_valid = all(c in "GYB" for c in fb) and len(fb) == 5
            self.assertTrue(is_valid, msg=f"Feedback '{fb}' should be valid")
        for fb in invalid:
            is_valid = all(c in "GYB" for c in fb) and len(fb) == 5
            self.assertFalse(is_valid, msg=f"Feedback '{fb}' should be invalid")

if __name__ == "__main__":
    unittest.main()




