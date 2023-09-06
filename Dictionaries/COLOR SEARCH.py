countries = {
    'Denmark': ['red', 'white'],
    'Finland': ['white', 'blue'],
    'France': ['blue', 'white', 'red'],
    'Germany': ['black', 'red', 'yellow'],
    'Iceland': ['blue', 'white', 'red'],
    'Netherlands': ['red', 'white', 'blue'],
    'Norway': ['red', 'white', 'blue'],
    'Sweden': ['yellow', 'blue'],
    'Ukraine': ['blue', 'yellow']
}

colors = input("colors > ").split()

for country, country_colors in countries.items():
    if all(color in country_colors for color in colors):
        print(country)