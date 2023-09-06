import random

number = random.randint(0, 99)
amount_guesses = 0

while True:
    guess = int(input("Guess a number > "))

    if guess == number:
        print("God job u guessed right")
        print("It took you", amount_guesses, "To guess right")
        break

    elif guess < number:
        print("Higher")
        amount_guesses += 1

    elif guess > number:
        print("Lower")
        amount_guesses += 1





