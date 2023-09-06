all_students = [
    'Anna',
    'Lars',
    'Eva',
    'Mikael',
    'Maria',
    'Anders'
]

team_a = [
    'Anna',
    'Maria',
]

team_b = [
    'Eva',
    'Anders'
]

for i in range(len(all_students)):
    if all_students[i] not in team_a and all_students[i] not in team_b:
        print(all_students[i])

