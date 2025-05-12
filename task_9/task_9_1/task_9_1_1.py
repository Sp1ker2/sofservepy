import random

def guess_the_number():
    number_to_guess = random.randint(1, 100)
    attempts = 10

    print("Welcome to the Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    print(f"You have {attempts} attempts to guess it.\n")

    for attempt in range(1, attempts + 1):
        try:
            guess = int(input(f"Attempt {attempt}: Enter your guess: "))
        except ValueError:
            print("Please enter a valid integer.")
            continue

        if guess < number_to_guess:
            print("Too low!")
        elif guess > number_to_guess:
            print("Too high!")
        else:
            print(f"Congratulations! You guessed the number {number_to_guess} in {attempt} attempts.")
            break
    else:
        print(f"Sorry, you've used all {attempts} attempts. The number was {number_to_guess}.")

guess_the_number()
