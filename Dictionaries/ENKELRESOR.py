flights = [
    { 'from': 'Stockholm', 'to': 'Göteborg' },
    { 'from': 'Göteborg', 'to': 'Malmö' },
    { 'from': 'Malmö', 'to': 'Västerås' },
    { 'from': 'Göteborg', 'to': 'Stockholm' },
    { 'from': 'Västerås', 'to': 'Göteborg' },
    { 'from': 'Stockholm', 'to': 'Malmö' },
    { 'from': 'Göteborg', 'to': 'Västerås' }
]

destinations = {}

for flight in flights:
    from_city = flight['from']
    to_city = flight['to']

    if from_city not in destinations:
        destinations[from_city] = []

    destinations[from_city].append(to_city)

print(destinations)

