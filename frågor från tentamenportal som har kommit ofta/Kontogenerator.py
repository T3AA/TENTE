def generate_username(forename, surname):
    username = forename[0] + surname[0] + surname[-1]
    count = 1
    while username + str(count) in generated_usernames:
        count += 1
    generated_usernames.append(username + str(count))
    return username + str(count)

generated_usernames = []

users = [
    'Anna Andersson',
    'Lars Johansson',
    'Eva Lindberg',
    'Erik Lundberg',
    'Per Svensson',
    'Emma Lindberg',
    'Petra Svensson',
    'Marie Gustafsson'
]

for user in users:
    forename, surname = user.split()
    username = generate_username(forename, surname)
    print(forename, surname, '-', username)