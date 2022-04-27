""" 
12 Beginner Python Projects - Coding Course
https://www.youtube.com/watch?v=8ext9G7xspg

"""

import random
from string import ascii_uppercase
from random_words import data
import string

def get_valid_word(data):
    random_word = random.choice(data)
    while( '-' in random_word or ' ' in random_word):
        random_word = random.choice(data)
    return random_word.upper()


def hangman():
    word = get_valid_word(data)
    word_letters = set(word)
    used_letters = set()
    alphabets = set(string.ascii_uppercase)
    lives = 6


    while len(word_letters) > 0 and lives > 0:

        print(f"You have only {lives} lives left and You have used these letters: {' '.join(used_letters)}")

        display_word = [letter if letter in used_letters else '-' for letter in word]
        print(f"Current word: {' '.join(display_word)} ")


        user_letter = input("Guess a letter: ").upper()
        if user_letter in used_letters:
            print("You have already used this letter, Please try again...")

        elif user_letter in alphabets - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives = lives - 1
                print("Letter is not in the word...")

        else:
            print("Invalid Charecter, Please try again...")

    if len(word_letters)<=0:
        print(f"Yay!.. You have guessed the word... word is :{word}")
    else:
        print(f"Sorry, you are out of life, The correct word is: {word}")


if __name__=='__main__':
    hangman()