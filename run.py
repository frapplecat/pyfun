"""
Import random library for random word selection from word_list
"""
import random
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


def intro():
    """
    Welcome intro to Hangman game
    """
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
        pr_yellow("{:+^79}".format("Welcome!"))
        print("\n")
        print("{: ^79}".format("Please enter your name below"))
        print("\n")
        username = input(" " * 37)

        if username.isalnum() is not True:
            pr_red("{: ^79}".format("Error: Letters and numbers only."))
            print("\n")
            continue
        else:
            print("\n")
            print("{: ^79}".format(f"Hi {username},"))
            print("{: ^79}".format("You have 6 guesses to guess the word."))
            input(" " * 25 + "Hit the enter key to begin")
            return username

    print("\n")
    print("{: ^79}".format(f"Hi {username},"))
    print("{: ^79}".format("You have 6 guesses to guess the word."))
    input(" " * 25 + "Hit the enter key to begin")
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
    word_completion = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6
    print("\n")
    pr_green("{:+^79}".format("Let's play Hangman!"))
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
                if "_" not in word_completion:
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
    while input(" " * 30 + "Play Again? (Y/N) ").upper() == "Y":
        word = get_word()
        play(word)


# if __name__ == "__main__":
main()
