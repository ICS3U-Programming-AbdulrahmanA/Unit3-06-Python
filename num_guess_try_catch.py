#!/usr/bin/env python3
# Created By: Abdul
# Date: 10/22/2025
# Program to ask the user for an integer

import random


def main():
    # generate a random number between 0 and 9
    correct = random.randint(0, 9)

    # get user input and handle exceptions
    try:
        user_input = input("Enter a number between 0 and 9: ")
        guess = int(user_input)

        # check if the guess is correct
        if guess == correct:
            print("Correct!")
        else:
            print("Wrong! The correct number was", correct)

    # if user input is not an integer, catch the exception
    except ValueError:
        print(user_input, "is not an integer.")
    # display ending message to user no matter the outcome
    finally:
        print("Thanks for playing!")


if __name__ == "__main__":
    main()
