pet_owners = [
    { 'name': 'Anna', 'id': 'aa' },
    { 'name': 'Lars', 'id': 'bb' },
    { 'name': 'Eva', 'id': 'cc' }
]

pets = [
    { 'name': 'Doris', 'owner_id': 'bb' },
    { 'name': 'Molly', 'owner_id': 'cc' },
    { 'name': 'Stampe', 'owner_id': 'aa' },
    { 'name': 'Luna', 'owner_id': 'bb' },
    { 'name': 'Pelle', 'owner_id': 'aa' }
]

pet_owner_name = input('pet owner name> ')

print(pet_owner_name, "pets: ")

for owner in pet_owners:
    owner_name = owner["name"]
    owner_id = owner["id"]

    for pet in pets:
        pet_name = pet["name"]
        pet_id = pet["owner_id"]

        if pet_owner_name == owner_name:
            if owner_id == pet_id:
                print("-", pet_name)



