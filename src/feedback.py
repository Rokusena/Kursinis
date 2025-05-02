# wordle_solver_oop/src/feedback.py

def generate_feedback(guess, target):
    guess = guess.lower()
    target = target.lower()
    result = ['' for _ in range(5)]
    target_copy = list(target)

    # First pass: Green (correct letter, correct place)
    for i in range(5):
        if guess[i] == target[i]:
            result[i] = 'G'
            target_copy[i] = None

    # Second pass: Yellow (right letter, wrong place) and Black
    for i in range(5):
        if result[i] == '':
            if guess[i] in target_copy:
                result[i] = 'Y'
                target_copy[target_copy.index(guess[i])] = None
            else:
                result[i] = 'B'

    return result
