def pet_filter(pets):

    i = -1

    for pet in pets:
        i += 1

        if pet["type"] == "rabbit":
            pets.pop(i)

        elif pet["type"] == "fish":
            pets.pop(i)

    return pets




pets = [
    { 'name': 'Smulan', 'type': 'cat' },
    { 'name': 'Molly', 'type': 'dog' },
    { 'name': 'Stampe', 'type': 'rabbit' },
    { 'name': 'Bella', 'type': 'cat' },
    { 'name': 'Blubbe', 'type': 'fish' },
    { 'name': 'Morris', 'type': 'dog' }
]

cat_and_dogs = pet_filter(pets)

for pet in cat_and_dogs:
    print(pet["name"], '(' + pet["type"] + ')')
