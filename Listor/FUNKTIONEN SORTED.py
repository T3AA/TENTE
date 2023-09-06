people = [
    {
        'name': 'Anna',
        'age': 25
    },
    {
        'name': 'Lars',
        'age': 20
    },
    {
        'name': 'Eva',
        'age': 30
    }
]

people_sorted = sorted(people, key=lambda x: x["age"], reverse=True)

for name in people_sorted:
    print(name["age"], "-", name["name"])

