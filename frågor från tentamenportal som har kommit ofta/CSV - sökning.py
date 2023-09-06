with open("db.csv") as f:
    csv = f.read()
lines = csv.split("\n")

location = input("Location: ")
print("--------")

for line in lines:
    word = line.split(",")

    if location == word[2]:
        print(word[0], word[1], word[2])
