i = ["a", "c", "b", "a", "b", "c", "a", "c", "c"]

c = {}

for e in i:
    if e not in c:
        c[e] = 0
    c[e] += 1

print(c["c"])

# fråga 1
# vilken typ har variabeln c efter tilldelningen på rad 3
# svar: dict

# fråga 2
# vilken typ har variabeln e vid loopen som startar rad 5
# svar: str

# fråga 3
# vad skrivs ut av print-satsen på rad 10
# svar: 4
