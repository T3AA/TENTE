import json

with open("passwords.json") as f:
    password_file = f.read()
    password_file = json.loads(password_file)


while True:
    master_password = input("Master password: ")

    if master_password == password_file['master_password']:
        print("success: authorized")

        domain = input("domain: ")
        for place in password_file['passwords']:

            if domain == place:
                print('username: ', password_file['passwords'][place]['username'])
                print('password: ', password_file['passwords'][place]['password'])
                break

            else:
                print("Error: unknown domain")

    else:

        print("Error")

