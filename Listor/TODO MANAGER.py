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
        remove = input("todo > ")

        if remove not in list:
            print("Todo: ", remove, "not found")
        else:
            list.remove(remove)
            print("todo", remove, "removed")

    else:
        print("Error: Unknown command")
