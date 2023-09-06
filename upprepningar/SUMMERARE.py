summary = 0

print("Summery")
print("-------")

while True:
    number = input("> ")

    try:
        summary += int(number)
    except ValueError:
        print("Error")

    if number == "0":
        print("-------")
        print("Resultat: ", summary)
        break


