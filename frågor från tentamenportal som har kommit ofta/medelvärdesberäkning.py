summa = 0
försök = 0

print("---------------------")
print("MEAN VALUE CALCULATOR")
print("---------------------")

while True:

    spelare = input("> ")

    if spelare == "exit":
        if försök == 0:
            print("Error : invalid integer")

        else:
            meanvalue = summa / försök
            print("---------------------")
            print("RESULT:", meanvalue)
        break

    try:
        nummer = int(spelare)
        summa += nummer
        försök += 1
    except ValueError:
        print("invalid integer")