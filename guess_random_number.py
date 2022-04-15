import random


def guess(x):
    random_number = random.randint(1, 10)
    guess = 0
    guess = int(input("Guess a number from 1 to 10: "))
    while (guess != random_number):
        if(guess>random_number):
            print("Too High... Guess the lower number")
            guess = int(input("Input Number is: "))
        elif(guess<random_number):
            print("Too Low... Guess the higher number")
            guess = int(input("Input Number is: "))

    print(f"Correct.. You have guessed the number... {random_number}")


if __name__ == "__main__":
    guess(10)










