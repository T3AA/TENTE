cart = [
    {
        'name': 'T-shirt',
        'quantity': 2,
        'cost': 149
    },
    {
        'name': 'Shorts',
        'quantity': 1,
        'cost': 199
    },
    {
        'name': 'Strumpor',
        'quantity': 3,
        'cost': 49
    },
    {
        'name': 'Baddräkt',
        'quantity': 1,
        'cost': 249
    }
]

print("    KVITTO    ")
print("--------------")

total = 0
frakt = 39

for set in cart:
    print(set["quantity"], set["name"], set["cost"], "kr/st")
    totals = set["quantity"] * set["cost"]
    total += totals

print("--------------")
print("fraktavgift:", frakt, "kr")
print("Total frakt:", total + frakt, "kr")
