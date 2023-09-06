a = 1
b = 0

print("Largest Integer")
print("---------------")

while a != 0:

    a = input("> ")

    try:
        a = int(a)
        if a > b:
            b = a
    except ValueError:
        print("Error : only integers")

print("---------------")
print("Result:", b)


