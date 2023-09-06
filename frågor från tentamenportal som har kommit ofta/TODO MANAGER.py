list = []

print(".: TODO MANAGER :.")
print("------------------")
print("list | list todos  ")
print("add  | add todo    ")
print("rm   | remove todo ")
print("------------------")


while True:
    command = input("Command > ")

    if command == "list":
        for todo in list:
            print(todo)

    elif command == "add":
        thing = input("todo > ")

        if thing in list:
            print("Error: todo", thing, "already exists")
        else:
            print("info: todo", thing, "added")
            list.append(thing)

    elif command == "rm":
        thing = input("todo > ")

        if thing not in list:
            print("Todo: ", thing, "not found")
        else:
            list.remove(thing)
            print("todo", thing, "removed")

    else:
        print("Error: Unknown command")