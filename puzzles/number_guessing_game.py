import random


def number_guessing_game():

    number = random.randint(0, 100)

    while True:
        try:
            guess = int(input("Guess the number between 1 and 100:"))
        except ValueError:
            print("Please enter a valid number")

        if guess == number:
            print("Congratulations! You guessed the number.")
            break

        elif guess > number:
            print("Too high!")

        elif guess < number:
            print("Too low!")

        else:
            print("Please enter a valid number")    

number_guessing_game()



