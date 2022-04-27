""" 
12 Beginner Python Projects - Coding Course
https://www.youtube.com/watch?v=8ext9G7xspg

"""

import random


def play():
    user_choice = input("What's your choice?  Rock [r]  Paper[p]  Scissor [s]\n")
    computer_choice = random.choice(['r', 'p', 's'])
    #  r > s   |   s > p   |    p > r

    if (user_choice == computer_choice):
        return "It's a Tie..."

    if (is_user_won(user_choice, computer_choice)):
        return "You Won!!!"

    return "You Lost..."


def is_user_won(user_choice, computer_choice):
    if ( (user_choice == 'r' and computer_choice == 's') or (user_choice == 's' and computer_choice == 'p') or (user_choice == 'p' and computer_choice == 'r') ):
        return True

if __name__=='__main__':
    print(play())