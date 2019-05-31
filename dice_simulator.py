
import random

print("Hello....Lets play a dice game")
print("First Think of a number between 1 to 6 ")
ch = 1

def dice():
    read = input("Enter the number you thought of?")
    actual = random.randint(1, 7)
    if read == actual:
        print("Wow!!...That was a Perfect Guess")
    else:
        print("Oops the Guess didnt workout")

print("Lets Start the Game.")

while ch:
    ch = input("If you want to roll the dice,Press 1")
    option = int(ch)
    if option == 1:
        dice()
    else:
        print("Bye Bye...See you around")
        break











