# programmet krachar med TypeError:

f = open("people.json")
people = f.read()
f.close()

for person in people:
    print(person["name"])


# fråga 1
# vad innehåller variabeln people för typ efter tilldelningen
# svar: str

# fråga 2
# vad innehåller variabeln person för typ i loopen
# svar: str

# fråga 3
# vilken beskrivning förklarar bäst hur felet kan återgäldas ?
# svar: typomvandla variabeln people till en lista med functioned json.loads(people)
