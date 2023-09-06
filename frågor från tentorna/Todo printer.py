import json

f = open("person.json")
person = f.read()
f.close()

password = input("password > ")

if password != person["password"]:
    print("ERROR: wrong password")

else:
    print("Hello " + person["name"] + "!")
    print("this is your todos:")
    for todo in person["todos"]:
        print("-", todo)



# En ny programmerare har skrivit källkoden för scriptet ni ser ovan. Scriptet försöker läsa filen person.json
# som har följande innehåll:
#
# Syftet med programmet är att skriva ut samtliga todos för användare som anger korrekt lösenord.
# Som går att se från utskriften nedan kraschar programmet efter att användaren matat in ett lösenord:
#
# Koden kan korrigeras genom att byta ut en felaktigt programmerad rad. Din uppgift är att identifiera den
# felaktiga raden och korrigera dess innehåll.


# fråga 1
# vilken rad vill du byta ut för koden för
# svar: 4

# fråga 2
# vad ska stå där istället
# svar: person = json.loads(f.read())