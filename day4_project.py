from random import *
"""
Number Guessing Game
"""

# name = input("Your name: ")
number = int(input("Guess a number between 1 to 100: "))

random_choice = randint(1,100)
print(f"random numnber: {random_choice}")

for count in range(8):
    if number == random_choice:
        print(f"congratulations! You guess it correct {number} == {random_choice}")
    elif number < random_choice:
        print(f"{number}number is below the magic number")
    elif number > random_choice:
        print(f"{number}number is above the magic number")

# while True:
#     if 0 > number > 100:

