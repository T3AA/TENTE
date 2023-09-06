import json

with open("users.json") as f:
    users = f.read()
    users = json.loads(users)

s = 0

for user in users:
    n = user["name"]
    a = user["age"]
    s += a
    print(n)

print(s)


# fråga 1
# vilken typ har variabeln efter tilldelningen på rad 4
# svar: str

# fråga 2
# vilken typ har variabeln users efter tilldelningen på rad 5
# svar: list

# fråga 3
# vilken typ har variabeln n efter tilldelningen på rad 10
# svar: str

# fråga 4
# vad skrivs ut på rad 15
# svar: 95