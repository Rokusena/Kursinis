# wordle_solver_oop/src/main.py

from wordlist import WordList
from solver import WordleSolver
from solver import FrequencySolverStrategy, StrategyContext



def main():
    print("🎯 Wordle Solver Assistant")
    print("Enter your guesses and feedback (G=green, Y=yellow, B=gray)")
    print("Type 'exit' to quit.\n")

    wordlist = WordList("data/words.txt")
    all_words = set(wordlist.get_words())

    # Apply strategy pattern with frequency-based solving
    strategy = FrequencySolverStrategy()
    solver = WordleSolver(wordlist)
    context = StrategyContext(strategy)

    # Optional: create or clear log file
    with open("guess_log.txt", "w") as log_file:
        log_file.write("Wordle Solver Session\n")

    while True:
        top_guesses = context.top_guesses(solver.possible_words, 10)
        if len(top_guesses) == 0:
            print("❌ No more possible words. Something went wrong.")
            break

        print(f"\n🔍 Top {min(len(top_guesses), 10)} suggestions:")
        for i, word in enumerate(top_guesses, 1):
            print(f"{i}. {word}")

        guess = input("\nYour guess (5-letter word): ").strip().lower()
        if guess == "exit":
            break

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

        if len(feedback) != 5:
            print("⚠️ Feedback must be exactly 5 characters.")
            continue
        if any(c not in "GYB" for c in feedback):
            print("⚠️ Feedback must contain only G, Y, or B.")
            continue

        with open("guess_log.txt", "a") as log_file:
            log_file.write(f"Guess: {guess.upper()}, Feedback: {feedback}\n")

        if feedback == "GGGGG":
            print(f"🎉 You guessed the word: {guess.upper()}!")
            break

        solver.update_possible_words(guess, list(feedback))


if __name__ == "__main__":
    main()
