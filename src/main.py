
from feedback import generate_feedback
from wordlist import WordList
from solver import WordleSolver

def main():
    print("🎯 Wordle Solver Assistant")
    print("Enter your guesses and feedback (G=green, Y=yellow, B=gray)")
    print("Type 'exit' to quit.\n")

    wordlist = WordList("data/words.txt")
    solver = WordleSolver(wordlist)
    all_words = set(wordlist.get_words())

    while True:
        top_guesses = solver.top_guesses(10)
        if len(top_guesses) == 0:
            print("❌ No more possible words. Something went wrong.")
            break

        print(f"\n🔍 Top {min(len(top_guesses), 10)} suggestions:")
        for i, word in enumerate(top_guesses, 1):
            print(f"{i}. {word}")

        guess = input("\nYour guess (5-letter word): ").strip().lower()
        if guess == "exit":
            break

        # Guess validation
        if len(guess) != 5:
            print("⚠️ Guess must be exactly 5 letters.")
            continue
        if not guess.isalpha():
            print("⚠️ Guess must contain only letters (no numbers or symbols).")
            continue
        if guess not in all_words:
            print("⚠️ Word not in word list.")
            continue

        feedback = input("Feedback (e.g., BGYGB): ").strip().upper()
        if feedback == "exit":
            break

        # Feedback validation
        if len(feedback) != 5:
            print("⚠️ Feedback must be exactly 5 characters.")
            continue
        if any(c not in "GYB" for c in feedback):
            print("⚠️ Feedback must contain only G, Y, or B.")
            continue

        if feedback == "GGGGG":
            print(f"🎉 You guessed the word: {guess.upper()}!")
            break

        solver.update_possible_words(guess, list(feedback))


if __name__ == "__main__":
    main()
