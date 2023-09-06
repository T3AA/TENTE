f = open("person.json")
p = f.read()
f.close()

name = p["name"]

print(name)

# scriptet kraschar dock med TypeError-exception

# fråga 1
# vid vilken rad uppstår krachen
# svar: rad 5

# fråga 2
# vilken mening beskriver bäst orsaken till kraschen
# svar : programmet kraschar eftersom man försöker indexera en sträng med en sträng