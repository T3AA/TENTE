def print_all_keys(person):
    for key in person:
        print(key)
        if type(person[key]) == dict:
            persons = person[key]
            print_all_keys(persons)
person = {
    'namn': 'Petra Svensson',
    'bostad': {
        'typ': 'hyra',
        'avgift': 5000
    },
    'husdjur': {
        'Douglas': {
            'typ': 'hund'
        },
        'Stampe': {
            'typ': 'kanin'
        }
    }
}

print_all_keys(person)