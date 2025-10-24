import random
from tkinter import Y


def dice_rolling_game():
    
    while True:
        dice_start = input("Roll the dice? (y/n)").strip().lower()

        if dice_start == "y":
            n1 = random.randint(0, 6)
            n2 = random.randint(0, 6)
            print(f"{n1}, {n2}")
            

        elif dice_start == "n":
            print ("Thanks for playing!")
            break

        else:
            print("Invalid Choice!")
    

dice_rolling_game()





    



