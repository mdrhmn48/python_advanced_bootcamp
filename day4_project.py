from random import *
"""
Number Guessing Game
"""

name = input("Your name: ")

random_choice = randint(1,100)
print(f"random number: {random_choice}")

for count in range(8):
    while True:
        try:
            number = int(input("Guess a number between 1 to 100: "))
            if (number > 100) or (number < 1):
                raise Exception
        except Exception:
            print("number must be between 1 and 100")
            continue
        count += 1
        break
    print(f"Try :{count}")

    if number == random_choice:
        print(f"congratulations! You guess it correct {number} == {random_choice}")
        break
    elif number < random_choice:
        print(f"{number} number is below the magic number")
    elif number > random_choice:
        print(f"{number} number is above the magic number")
    else:
        print(f"Sorry you only had try. {random_choice} was the number")

