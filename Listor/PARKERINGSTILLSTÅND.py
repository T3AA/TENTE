granted_parking_permits = ['910101-1234', '820202-5678']

print(" .: PARKING PERMIT MANEGER :. ")
print("------------------------------")
print("Grant | grant parkering permit")
print("Check | check parkering permit")
print("------------------------------")


while True:
    comand = input("Command > ")

    if comand == "grant":
        student = input("student > ")

        if student in granted_parking_permits:
            print("Error : stdudent allredy have a parking")

        else:
            print("Sucsses: granted parkering permit to ", student)
            granted_parking_permits.append(student)

    elif comand == "check":
        student = input("student > ")

        if student in granted_parking_permits:
            print(student, "has a parking permit")

        elif student not in granted_parking_permits:
            print(student, "dose not have a parking permit")

    else:
        print("error: Unknown command")


