    # Infinite Wordle
    #### Video Demo: https://youtu.be/1L4yDf8eFhE
    #### Description:
This project is a command-line implementation of Wordle, created as my final project for CS50P. The game selects a secret random five-letter English word and allows the user six attempts to guess it. After each guess, the game provides colored feedback for each letter just like in Wordle:
Green if the letter is correct and in the correct position
Yellow if the letter is correct but in the wrong position
Gray if the letter is not in the secret word
The game is played entirely in the terminal with simple ANSI color codes to make the feedback visually intuitive.
The secret word is fetched from a real-time English word list hosted on GitHub.
The game validates all guesses against the same dictionary to ensure they're real English words.
Colored terminal output mimics the real Wordle game's visual feedback.
Guesses that are invalid (not 5-letter or not real words) do not consume an attempt.
I chose to avoid using any static or hardcoded word lists to keep the game dynamic and reflect real vocabulary. This also made the word validation process more consistent and authentic. The game includes a fallback-friendly design using try/except, though now it only uses a single method to fetch live words. To keep gameplay fair, invalid guesses do not count against the player's total attempts. I also opted to use simple color codes rather than external libraries like colorama to keep dependencies minimal and terminal compatibility high.

    #### Files:
project.py: The core game logic and entry point.

test_project.py: Contains unit tests for core logic functions.It tests:
validate_guess() with various valid and invalid inputs, ensuring the function behaves reliably.
get_feedback() to ensure correct letter comparisons and feedback generation across different guess scenarios.

requirements.txt: Lists the external library requests, which is used to fetch the live word list.

    #### Functions:

main(): Manages the overall flow of the game. It loads the word list, selects the secret word, loops through user guesses, validates them, and provides feedback. It also handles win/loss conditions and limits the game to six valid guesses.

load_words(): Fetches an entire dictionary of English words from a remote GitHub-hosted word list. It filters out all words that aren't exactly five letters long or contain non-alphabetic characters. This ensures the secret word and valid guesses are all meaningful and appropriate.

get_secret_word(): Selects a random word from the filtered list provided by load_words(). This ensures each game run has a new and unpredictable secret word.

validate_guess(guess, word_list): Ensures the user's guess is valid. It checks if the guess exists in the word list and is exactly five letters long. This prevents invalid or meaningless inputs from being processed or counted against the player's attempts.

get_feedback(secret, guess): Compares the player's guess to the secret word, letter by letter. It returns a list of five strings, each representing a color: 'green' (correct letter and position), 'yellow' (correct letter, wrong position), or 'gray' (incorrect letter). This logic is central to the Wordle experience.

print_colored_feedback(guess, feedback): Accepts a guess and its corresponding feedback list and prints each letter in the appropriate color to the terminal using ANSI escape codes. This makes it easy for the player to visually understand which letters are correct and where they should be.
