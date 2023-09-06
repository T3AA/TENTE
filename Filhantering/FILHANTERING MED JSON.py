import json

f = open("numbers.json")
numbers = f.read()
numbers = json.loads(numbers)
f.close()

for i in range(len(numbers)):
    numbers[i] = 2 * numbers[i]

numbers.append(1)
print(numbers)

f = open("numbers.json", "w")
numbers = json.dumps(numbers)
f.write(numbers)
f.close()
