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



def computer_gues(x):
    low = 1
    high = x
    feedback = ''
    
    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low

        feedback = input(f"Is the number {guess} is High [h] Or Low [l] Or Correct [c] ? ")

        if feedback == 'l':
            low = guess+1
            guess = random.randint(low, high)

        elif feedback == 'h':
            high = guess-1 
            guess = random.randint(low, high)

    print(f"Yay... Computer has guessed the number... {guess}")


if __name__ == "__main__":
    computer_gues(1000)










