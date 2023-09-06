import random

number = random.randint(0, 99)
amount_guesses = 0

while True:

    spelare = int(input("> "))

    if spelare == number:
        print("bra jobbat")
        print("det tog dig", amount_guesses, "gånger för att gissa rätt ")
        break

    elif spelare < number:
        print("högre")
        amount_guesses += 1

    elif spelare > number:
        print("mindre")
        amount_guesses += 1
