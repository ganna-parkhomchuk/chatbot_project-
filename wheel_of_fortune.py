import random

MAX_ATTEMPTS = 7


def get_user_guess():
    """
    A function that gets a valid user input for guessing a letter.
    Returns:
        str: a valid uppercase letter guessed by the user.
    """
    guess = input("Please guess the letter: ").upper()
    while len(guess) != 1 or not guess.isalpha():
        print("Wrong input. Please input one letter.")
        guess = input("Please guess the letter: ").upper()
    return guess


def main():
    """
    Main function for the word guessing game.
    Randomly selects a word from a list of words and prompts the user to guess letters.
    Displays the guessed letters and tracks the remaining attempts until the user either wins or loses.
    """
    words = ["PYTHON", "PROGRAMMING", "DEVELOPER", "FUNCTION", "ENGINEER"]
    attempts = MAX_ATTEMPTS
    word = random.choice(words)
    guessed_letters = ["_"] * len(word)

    while "_" in guessed_letters and attempts > 0:
        print(" ".join(guessed_letters))
        print(attempts, "attempt has left." if attempts == 1 else "attempts have left.")
        guess = get_user_guess()

        if guess in word:
            print("You are right!")
            for i in range(len(word)):
                if word[i] == guess:
                    guessed_letters[i] = guess
        else:
            print("You are wrong!")
            attempts -= 1

    if "_" not in guessed_letters:
        print("Congratulations, you have guessed the word: " + word)
    else:
        print("Sorry, you lost. The word was: " + word)


if __name__ == "__main__":
    main()
