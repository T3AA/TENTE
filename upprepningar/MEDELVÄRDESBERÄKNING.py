summa = 0
försök = 0

print("mean value calculator")
print("---------------------")

while True:

    spelare = input("> ")

    if spelare == 'exit':
        if försök == 0:
            print("Error: no integer")

        else:
            meanvalue = summa / försök
            print("---------------------")
            print("Result: ", meanvalue)
        break

    try:
        nummer = int(spelare)
        summa += nummer
        försök += 1
    except ValueError:
        print("Error: Invalid integer")