import requests
import random

WORD_LIST_URL = "https://raw.githubusercontent.com/dwyl/english-words/master/words_alpha.txt"


def load_words():
    response = requests.get(WORD_LIST_URL)
    if response.status_code == 200:
        all_words = response.text.splitlines()
        five_letter_words = [word.lower() for word in all_words if len(word) == 5 and word.isalpha()]
        return five_letter_words
    raise ConnectionError("Failed to load word list from the internet.")


def get_secret_word(word_list):
    return random.choice(word_list)


def validate_guess(guess, word_list):
    return guess in word_list and len(guess) == 5


def get_feedback(secret, guess):
    feedback = []
    secret_chars = list(secret)
    guess_chars = list(guess)

    for i in range(5):
        if guess_chars[i] == secret_chars[i]:
            feedback.append("green")
            secret_chars[i] = None  # Mark as used
        else:
            feedback.append(None)  # Placeholder

    for i in range(5):
        if feedback[i] is None:
            if guess_chars[i] in secret_chars:
                feedback[i] = "yellow"
                secret_chars[secret_chars.index(guess_chars[i])] = None
            else:
                feedback[i] = "gray"

    return feedback


def print_colored_feedback(guess, feedback):
    colors = {
        "green": "\033[92m",   # bright green
        "yellow": "\033[93m",  # bright yellow
        "gray": "\033[90m",    # gray
        "end": "\033[0m"
    }
    for i in range(5):
        color = colors[feedback[i]]
        print(f"{color}{guess[i]}{colors['end']}", end=" ")
    print()


def main():
    print("Welcome to WORDLE!")
    word_list = load_words()
    secret = get_secret_word(word_list)
    attempts = 6
    turn = 1

    while turn <= attempts:
        guess = input(f"Guess #{turn}: ").lower()
        if not validate_guess(guess, word_list):
            print("Invalid word. Must be a valid 5-letter English word.")
            continue

        feedback = get_feedback(secret, guess)
        print_colored_feedback(guess, feedback)

        if guess == secret:
            print(f"You won in {turn} guess(es)!")
            return

        turn += 1

    print(f"Sorry! The word was '{secret}'. Better luck next time.")


if __name__ == "__main__":
    main()