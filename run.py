"""
Import random library for random word selection from word_list
"""
import random
from words import word_list


def intro():
    """
    Welcome intro to Hangman game
    """
    print("""

██╗  ██╗ █████╗ ███╗   ██╗ ██████╗ ███╗   ███╗ █████╗ ███╗   ██╗
██║  ██║██╔══██╗████╗  ██║██╔════╝ ████╗ ████║██╔══██╗████╗  ██║
███████║███████║██╔██╗ ██║██║  ███╗██╔████╔██║███████║██╔██╗ ██║
██╔══██║██╔══██║██║╚██╗██║██║   ██║██║╚██╔╝██║██╔══██║██║╚██╗██║
██║  ██║██║  ██║██║ ╚████║╚██████╔╝██║ ╚═╝ ██║██║  ██║██║ ╚████║
╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝
""")
    username = " "
    while True:
        username = input("Welcome! Please enter your name: \n")

        if username.isalnum() is not True:
            print("Error: Letters and numbers only.")
            continue
        else:
            print(f"Hi {username}, You have 6 guesses to guess the word.")
            input("When you are ready to play, hit the enter key to begin")
            return username

    print(f"Hi {username}, You have 6 guesses to guess the word.")
    input("When you are ready to play, hit the enter key to begin")
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
    print("Let's play Hangman!")
    print(display_hangman(tries))
    print("\n")
    while not guessed and tries > 0:
        guess = input("Please guess a letter or word: ").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("You've already guessed this letter", guess)
            elif guess not in word:
                print(guess, "is not in the word.")
                tries -= 1
                guessed_letters.append(guess)
            else:
                print("Good job,", guess, "is in the word!")
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)
                if "_" not in word_completion:
                    guessed = True
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print("You already guessed the word", guess)
            elif guess != word:
                print(guess, "is not the word.")
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = word
        else:
            print("Not a valid guess")
        print(display_hangman(tries))
        print(word_completion)
        print("\n")
    if guessed:
        print("Congrats, you guessed the word! You win!")
        print("""
░▒█░░▒█░▒█▀▀▀█░▒█░▒█░░░▒█░░▒█░▀█▀░▒█▄░▒█
░▒▀▄▄▄▀░▒█░░▒█░▒█░▒█░░░▒█▒█▒█░▒█░░▒█▒█▒█
░░░▒█░░░▒█▄▄▄█░░▀▄▄▀░░░▒▀▄▀▄▀░▄█▄░▒█░░▀█
""")

    else:
        print("Sorry, out of tries. The word was " + word + ".")
        print("""
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
                   |
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
    while input("Play Again? (Y/N) ").upper() == "Y":
        word = get_word()
        play(word)


# if __name__ == "__main__":
main()
