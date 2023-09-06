birds = {}
Bird_name = 0
total = 0


while True:
    name = input("bird > ").title()

    if name not in birds.keys():
        birds[name] = ""
        Bird_name = 1
        total += 1

    elif name in birds:
        total += 1
        Bird_name += 1
    print("("+name+")", Bird_name, "out of", total)