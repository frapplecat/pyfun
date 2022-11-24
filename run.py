import random
from words import word_list


def get_word():
    """
    Function that returns a word for the hangman game
    """
    word = random.choice(word_list)
    """
    Picks a random word from word_list
    """
    return word.upper()
    """
    returns the random word in uppercase
    """