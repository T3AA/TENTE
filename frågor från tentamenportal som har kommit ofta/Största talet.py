a = 1
b = 0

print("LARGEST INTEGER")
print("---------------")

while a != 0:

    a = input("> ")

    try:
        a = int(a)
        if a > b:
            b = a
    except ValueError:
        print("invalid integer")

print("-----------")
print("Resultat", b)
