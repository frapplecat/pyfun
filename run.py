"""
Libraries and imports
"""
import os   # To use to clear screen function
import random  # Import random library for random word selection from word_list
from words import word_list
# pylint: disable=consider-using-f-string


def pr_green(skk):
    """
    Defines green color for output in terminal
    """
    print("\033[92m {}\033[00m".format(skk))


def pr_red(skk):
    """
    Defines red color for output in terminal
    """
    print("\033[91m {}\033[00m" .format(skk))


def pr_yellow(skk):
    """
    Defines yellow color for output in terminal
    """
    print("\033[93m {}\033[00m" .format(skk))


def clear_screen():
    """
    Used to clear Terminal screen
    """
    os.system("clear")


def intro():
    """
    Welcome intro to Hangman game
    """
    pr_green("""

                    ██████╗ ██╗   ██╗███████╗██╗   ██╗███╗   ██╗
                    ██╔══██╗╚██╗ ██╔╝██╔════╝██║   ██║████╗  ██║
                    ██████╔╝ ╚████╔╝ █████╗  ██║   ██║██╔██╗ ██║
                    ██╔═══╝   ╚██╔╝  ██╔══╝  ██║   ██║██║╚██╗██║
                    ██║        ██║   ██║     ╚██████╔╝██║ ╚████║
                    ╚═╝        ╚═╝   ╚═╝      ╚═════╝ ╚═╝  ╚═══╝
""")
    pr_yellow("""

        ██╗  ██╗ █████╗ ███╗   ██╗ ██████╗ ███╗   ███╗ █████╗ ███╗   ██╗
        ██║  ██║██╔══██╗████╗  ██║██╔════╝ ████╗ ████║██╔══██╗████╗  ██║
        ███████║███████║██╔██╗ ██║██║  ███╗██╔████╔██║███████║██╔██╗ ██║
        ██╔══██║██╔══██║██║╚██╗██║██║   ██║██║╚██╔╝██║██╔══██║██║╚██╗██║
        ██║  ██║██║  ██║██║ ╚████║╚██████╔╝██║ ╚═╝ ██║██║  ██║██║ ╚████║
        ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝
""")
    username = " "
    while True:
        pr_yellow("{:+^79}".format("I hope you brought a thesaurus!"))
        print("\n")
        print("{: ^79}".format("Please enter your name below"))
        print("\n")
        username = input(" " * 37)
        clear_screen()

        if username.isalnum() is not True:
            pr_red("{: ^79}".format("Error: Letters and numbers only."))
            print("\n")
            continue
        else:
            pr_green("""
        ♥♥     ♥♥ ♥♥♥♥♥♥♥ ♥♥       ♥♥♥♥♥♥  ♥♥♥♥♥♥  ♥♥♥    ♥♥♥ ♥♥♥♥♥♥♥ ♥♥
        ♥♥     ♥♥ ♥♥      ♥♥      ♥♥      ♥♥    ♥♥ ♥♥♥♥  ♥♥♥♥ ♥♥      ♥♥
        ♥♥  ♥  ♥♥ ♥♥♥♥♥   ♥♥      ♥♥      ♥♥    ♥♥ ♥♥ ♥♥♥♥ ♥♥ ♥♥♥♥♥   ♥♥
        ♥♥ ♥♥♥ ♥♥ ♥♥      ♥♥      ♥♥      ♥♥    ♥♥ ♥♥  ♥♥  ♥♥ ♥♥
         ♥♥♥ ♥♥♥  ♥♥♥♥♥♥♥ ♥♥♥♥♥♥♥  ♥♥♥♥♥♥  ♥♥♥♥♥♥  ♥♥      ♥♥ ♥♥♥♥♥♥♥ ♥♥
            """)
            print("\n")
            print("{: ^79}".format(f"Hi {username}."))
            print("\n")
            print("{: ^79}".format("Try to guess the word."))
            print("{: ^79}".format("Each error adds a line to the gallows"))
            print("{: ^79}".format("You have 6 incorrect guesses before..."))
            print("{: ^79}".format("it's TOO LATE!"))
            pr_green("{: ^79}".format("Wishing you the best of luck!"))
            print("\n")
            input(" " * 25 + "Hit the enter key to begin \n \n")
            return username

    pr_green("""
        ♥♥     ♥♥ ♥♥♥♥♥♥♥ ♥♥       ♥♥♥♥♥♥  ♥♥♥♥♥♥  ♥♥♥    ♥♥♥ ♥♥♥♥♥♥♥ ♥♥
        ♥♥     ♥♥ ♥♥      ♥♥      ♥♥      ♥♥    ♥♥ ♥♥♥♥  ♥♥♥♥ ♥♥      ♥♥
        ♥♥  ♥  ♥♥ ♥♥♥♥♥   ♥♥      ♥♥      ♥♥    ♥♥ ♥♥ ♥♥♥♥ ♥♥ ♥♥♥♥♥   ♥♥
        ♥♥ ♥♥♥ ♥♥ ♥♥      ♥♥      ♥♥      ♥♥    ♥♥ ♥♥  ♥♥  ♥♥ ♥♥
         ♥♥♥ ♥♥♥  ♥♥♥♥♥♥♥ ♥♥♥♥♥♥♥  ♥♥♥♥♥♥  ♥♥♥♥♥♥  ♥♥      ♥♥ ♥♥♥♥♥♥♥ ♥♥
            """)
    print("\n")
    print("{: ^79}".format(f"Hi {username}."))
    print("\n")
    print("{: ^79}".format("Try to guess the word."))
    print("{: ^79}".format("Each error adds a line to the gallows"))
    print("{: ^79}".format("You have 6 incorrect guesses before..."))
    print("{: ^79}".format("it's TOO LATE!"))
    pr_green("{: ^79}".format("Wishing you the best of luck!"))
    print("\n")
    input(" " * 25 + "Hit the enter key to begin \n \n")
    return username


def get_word():
    """
    Function that returns a word for the hangman game
    """
    word = random.choice(word_list)
    return word.upper()


def play(word):
    """
    Displays the word for the game during each turn
    """
    word_completion = "?" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6
    clear_screen()
    pr_red("""
                    ██████╗ ███████╗ █████╗ ██████╗ ██╗   ██╗██████╗
                    ██╔══██╗██╔════╝██╔══██╗██╔══██╗╚██╗ ██╔╝╚════██╗
                    ██████╔╝█████╗  ███████║██║  ██║ ╚████╔╝   ▄███╔╝
                    ██╔══██╗██╔══╝  ██╔══██║██║  ██║  ╚██╔╝    ▀▀══╝
                    ██║  ██║███████╗██║  ██║██████╔╝   ██║     ██╗
                    ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═════╝    ╚═╝     ╚═╝
            """)
    pr_green("{:+^79}".format("Let's play Hangman!"))
    print("\n")
    pr_yellow(display_hangman(tries))
    print("\n")
    while not guessed and tries > 0:
        guess = input(" " * 25 + "Please guess a letter or word: ").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("\n")
                pr_red("{: ^79}".format("You've already guessed " + guess))
            elif guess not in word:
                print("\n")
                pr_red("{: ^79}".format(guess + " is not in the word."))
                tries -= 1
                guessed_letters.append(guess)
            else:
                print("\n")
                pr_green("{: ^79}".format("Cool, " + guess + " is right!"))
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                inds = [i for i, letter in enumerate(word) if letter == guess]
                for index in inds:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)
                if "?" not in word_completion:
                    guessed = True
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                pr_red("You already guessed the word" + guess)
            elif guess != word:
                pr_red(guess + "is not the word.")
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = word
        else:
            print("\n")
            pr_red("{: ^79}".format("Not a valid guess"))
        pr_yellow(display_hangman(tries))
        print("{: ^79}".format(word_completion))
        print("\n")
    if guessed:
        pr_green("{: ^79}".format("Excellent, you guessed the word!"))
        pr_green("""
                    ░▒█░░▒█░▒█▀▀▀█░▒█░▒█░░░▒█░░▒█░▀█▀░▒█▄░▒█
                    ░▒▀▄▄▄▀░▒█░░▒█░▒█░▒█░░░▒█▒█▒█░▒█░░▒█▒█▒█
                    ░░░▒█░░░▒█▄▄▄█░░▀▄▄▀░░░▒▀▄▀▄▀░▄█▄░▒█░░▀█
""")

    else:
        pr_red("{: ^79}".format("Unlucky. The word was " + word + "."))
        pr_red("""
                ░▒█░░▒█░▒█▀▀▀█░▒█░▒█░░░▒█░░░░▒█▀▀▀█░▒█▀▀▀█░▒█▀▀▀
                ░▒▀▄▄▄▀░▒█░░▒█░▒█░▒█░░░▒█░░░░▒█░░▒█░░▀▀▀▄▄░▒█▀▀▀
                ░░░▒█░░░▒█▄▄▄█░░▀▄▄▀░░░▒█▄▄█░▒█▄▄▄█░▒█▄▄▄█░▒█▄▄▄
""")


def display_hangman(tries):
    """
    Display hangman for various stages of tries
    """
    stages = [  # final state: head, torso, both arms, and both legs
                """
                                    --------
                                    |      |
                                    |      |
                                    |      O
                                    |     /|\\
                                    |      |
                                    |     / \\
                                    |
                                    |
                                    --------
                """,
                # head, torso, both arms, and one leg
                """
                                    --------
                                    |      |
                                    |      |
                                    |      O
                                    |     /|\\
                                    |      |
                                    |     /
                                    |
                                    |
                                    --------
                """,
                # head, torso, and both arms
                """
                                    --------
                                    |      |
                                    |      |
                                    |      O
                                    |     /|\\
                                    |      |
                                    |
                                    |
                                    |
                                    --------
                """,
                # head, torso, and one arm
                """
                                    --------
                                    |      |
                                    |      |
                                    |      O
                                    |     /|
                                    |      |
                                    |
                                    |
                                    |
                                    --------
                """,
                # head and torso
                """
                                    --------
                                    |      |
                                    |      |
                                    |      O
                                    |      |
                                    |      |
                                    |
                                    |
                                    |
                                    --------
                """,
                # head
                """
                                    --------
                                    |      |
                                    |      |
                                    |      O
                                    |
                                    |
                                    |
                                    |
                                    |
                                    --------
                """,
                # initial empty state
                """
                                    --------
                                    |      |
                                    |      |
                                    |
                                    |
                                    |
                                    |
                                    |
                                    |
                                    --------
                """
    ]
    return stages[tries]


def main():
    """
    Main game function
    """
    intro()

    word = get_word()
    play(word)
    while True:
        if input(" " * 30 + "Play Again? (Y/N) ").upper() == "Y":
            word = get_word()
            play(word)
        else:
            clear_screen()
            pr_green("{: ^79}".format("See you again hopefully! \n"))
            pr_green("""
             ██████╗  ██████╗  ██████╗ ██████╗ ██████╗ ██╗   ██╗███████╗
            ██╔════╝ ██╔═══██╗██╔═══██╗██╔══██╗██╔══██╗╚██╗ ██╔╝██╔════╝
            ██║  ███╗██║   ██║██║   ██║██║  ██║██████╔╝ ╚████╔╝ █████╗
            ██║   ██║██║   ██║██║   ██║██║  ██║██╔══██╗  ╚██╔╝  ██╔══╝
            ╚██████╔╝╚██████╔╝╚██████╔╝██████╔╝██████╔╝   ██║   ███████╗
             ╚═════╝  ╚═════╝  ╚═════╝ ╚═════╝ ╚═════╝    ╚═╝   ╚══════╝
""")
            break


main()
