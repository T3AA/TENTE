car_colors = [
    'red',
    'green',
    'black',
    'blue',
    'white',
    'blue',
    'black/red',
    'red',
    'blue',
    'black',
    'white',
    'black/red'
]

for color in set(car_colors):
    count = car_colors.count(color)
    print(color, count)
