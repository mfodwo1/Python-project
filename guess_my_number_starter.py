"""
File: guessmynumber.py
----------------------
This program checks if a user's guess of a number matches that guessed by the computer
"""

#import random
# use code below  to generate a random integer between 30 and 50 for example
#print(random.randint(30, 50))

# ********************************** YOUR CODE GOES BELOW HERE *********************************************************
from random import randint

# Generate random number
secret_num = randint(30, 50)

# Tell the user what you have in mind
print("I am thinking of a number between 30 and 50")

# This will keep running until the user guess the right number
while True:
    try:
        # Guess a number
        guess = int(input("Guess a number: "))

        # check whether the user guess the correct number
        if guess > secret_num:
            print("Try again your guess is too high")
        elif guess < secret_num:
            print("Try again your guess if too small")
        else:
            print(f"Congrats! The number was: {secret_num}")
            break

    # This code will only execute if a user enter an alphabet
    except(TypeError, ValueError):
        print("Invalid, try again")
