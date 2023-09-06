csv = "maria,1997,female\nAnders,1990,male\nKarin,1977,female"

rows = csv.split("\n")
match = False
for row in rows:
    columns = row.split(",")
    if columns[2] == "male":
        match = columns[1]
        break
print(match)

# fråga 1
# vilken typ innehåller variabeln "rows" efter tilldelningen vid rad 3
# svar: list

# fråga 2
# vilken typ innehåller variabeln columns efter tilldelningen vid rad 6
# svar: list

# fråga 3
# vilken typ innehåller variabeln match efter tilldelningen vid rad 8
# svar: str

# fråga 4
# vad skrivs ut vid rad 11
# svar: 1990