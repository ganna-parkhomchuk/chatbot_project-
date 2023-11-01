"""
Entertainment Chatbot

This script implements an entertainment chatbot that interacts with the user based on the user's preferences.
It offers information about movies and music, as well as jokes and interesting stories.
Additionally, it provides various games for entertainment.

External Libraries:
- pyjokes: a library for fetching random jokes.
- prettytable: a library for creating ASCII tables.
- emoji: a library for using emoji characters in the output.
- art: a library for generating ASCII art text.

Modules:
- random: Python's built-in module for generating random numbers and choices.

External Data Files:
- 'movies.txt': contains a list of movie titles.
- 'music.txt': contains a list of music information.
- 'interesting_stories.txt': contains a list of interesting stories.

How to Use:
- Run the script. The chatbot greets the user and invites to select a topic of interest.
- The user can select options such as movies, music, games, jokes or interesting stories.
- Depending on the choice the chatbot will provide information or initiate a game.
- After providing information or playing a game the user can choose to play again or exit.
"""


import pyjokes
from prettytable import PrettyTable
import emoji
from art import *
import random
from wheel_of_fortune import main as wheel_of_fortune_game


def user_greeting():
    """
    A function that displays a greeting message using ASCII art and presents the user with available options.
    Options include movies, music, games, jokes and interesting stories.
    """
    hello_art = text2art("Hello!", font='block', chr_ignore=True)
    colored_hello_art = f"\033[32m{hello_art}\033[0m"
    print(colored_hello_art)
    print('Welcome to the entertainment chatbot! What are you interested in?')
    x = PrettyTable()
    x.field_names = ["Your options:"]
    x.add_row([emoji.emojize(':popcorn:') + " Movies"])
    x.add_row([emoji.emojize(':musical_note:') + " Music"])
    x.add_row([emoji.emojize(':video_game:') + " Games"])
    x.add_row([emoji.emojize(':face_with_tears_of_joy:') + " Jokes"])
    x.add_row([emoji.emojize(':books:') + " Interesting stories"])
    print(x)


def read_data(file_name):
    """
    A function that reads data from the specified file and returns it as a list.
    Parameters:
        file_name (str). The name of the file to be read.
    Returns:
        data (list): a list containing the lines of text from the file.
    Raises:
        FileNotFoundError: if the specified file is not found in the directory.
        Exception: If any other unexpected error occurs during file reading,
        the specific error message will be displayed.
    """
    try:
        with open(file_name, 'r', encoding='UTF-8') as file:
            data = file.read().split('\n')
        return data
    except FileNotFoundError:
        print(f"File '{file_name}' not found. Please make sure the file exists in the same directory.")
        return []
    except Exception as e:
        print(f"An error occurred: {e}")
        return []


def movie_info():
    """
    Displays a random movie information fetched from the 'movies.txt' file.
    """
    movies = read_data('movies.txt')
    print(random.choice(movies) if movies else None)


def music_info():
    """
    Displays a random music information fetched from the 'music.txt' file.
    """
    music = read_data('music.txt')
    print(random.choice(music) if music else None)


def randomizer_game():
    """
    The function generates a random number between 1 and 20 and prompts the user to guess the number.
    It provides feedback on whether the guessed number is too small, too high or correct.
    The game continues until the user guesses the correct number.
    Raises:
        ValueError: if the user enters a non-integer value.
    Returns:
        None
    """
    number = random.randint(1, 20)
    while True:
        try:
            guess = int(input('Try to guess a number between 1 and 20: '))
            if 1 <= guess <= 20:
                if guess == number:
                    print('You are right! Great!')
                    break
                elif guess < number:
                    print("Your figure is too small")
                else:
                    print("Your figure is too high")
            else:
                print('Please enter a number between 1 and 20.')
        except ValueError:
            print('Invalid input. Please enter a number.')


def rock_paper_scissors_game():
    """
    The function asks the user to pick rock, paper or scissors and generates a random choice for the computer.
    It compares the choices and determines the winner based on the classic rock-paper-scissors rules.
    The game continues until the user makes a valid choice.
    Returns:
        None
    """
    while True:
        user_choice = input('Choose rock or paper or scissors: ')
        possible_choices = ["rock", "paper", "scissors"]

        if user_choice in possible_choices:
            computer_choice = random.choice(possible_choices)
            print(f"\nYou chose {user_choice}, computer chose {computer_choice}.\n")

            if user_choice == computer_choice:
                print(f"Both players selected {user_choice}. It's a tie!")
            elif user_choice == "rock":
                if computer_choice == "scissors":
                    print("Rock smashes scissors! You win!")
                else:
                    print("Paper covers rock! You lose.")
            elif user_choice == "paper":
                if computer_choice == "rock":
                    print("Paper covers rock! You win!")
                else:
                    print("Scissors cuts paper! You lose.")
            elif user_choice == "scissors":
                if computer_choice == "paper":
                    print("Scissors cuts paper! You win!")
                else:
                    print("Rock smashes scissors! You lose.")
            break
        else:
            print("Wrong choice. Please choose rock, paper, or scissors.")


def game_info():
    """
    The function asks the user to select a category: logical games (1) or mathematical games (2).
    For logical games, the user can choose between Rock-Paper-Scissors (1) and Wheel of Fortune (2).
    For mathematical games, the number guessing game is played.
    Raises:
        ValueError: if the user enters a non-integer value.
    Returns:
        None
    """
    while True:
        try:
            game_choosing = int(input('Please choose the game. For logical games press 1, '
                                      'for mathematical games press 2: '))

            if game_choosing == 1:
                while True:
                    game_type = int(input('For Rock-Paper-Scissors game press 1, '
                                          'for Wheel of Fortune game press 2: '))
                    if game_type == 1:
                        rock_paper_scissors_game()
                        break
                    elif game_type == 2:
                        wheel_of_fortune_game()
                        break
                    else:
                        print("Please select correct option")
            elif game_choosing == 2:
                randomizer_game()
            else:
                print("Please select correct option")
                continue
            break

        except ValueError:
            print("Invalid input. Please enter a number.")


def joke_info():
    """
    Displays a random joke using the 'pyjokes' library.
    """
    print(pyjokes.get_joke())


def interesting_story_info():
    """
    Displays a random interesting story fetched from the 'interesting_stories.txt' file.
    """
    interesting_stories = read_data('interesting_stories.txt')
    print(random.choice(interesting_stories) if interesting_stories else None)


def manage_user_input():
    """
    A function that manages user interactions, displays options using user_greeting(), processes input to provide
    information or initiate games and prompts the user if he/she wants to play again.
    Returns:
        None
    """
    play_again = 'y'
    while play_again == 'y':
        user_greeting()
        user_input = input("User's choice: ").lower()

        if user_input.find("movie") != -1 or user_input.find("movies") != -1:
            movie_info()
        elif user_input.find("music") != -1:
            music_info()
        elif user_input.find("game") != -1 or user_input.find("games") != -1:
            game_info()
        elif user_input.find("joke") != -1 or user_input.find("jokes") != -1:
            joke_info()
        elif user_input.find("interesting story") != -1 or user_input.find("interesting stories") != -1:
            interesting_story_info()
        else:
            print("Please select an option from the available categories: "
                  "movies, music, games, jokes, interesting stories?")
            continue

        while True:
            play_again = input("Play again? (y/n): ").lower()
            if play_again in ['y', 'n']:
                break
            else:
                print("Wrong input. Please enter 'y' to play again or 'n' to exit.")


if __name__ == "__main__":
    manage_user_input()
