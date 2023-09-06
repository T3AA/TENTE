def translate(text):
    translate = " "
    text = text.split()

    for word in text:
        for svenskaord in words:
            if word == svenskaord:
                translate += words[svenskaord] + " "

    return translate

words = {
    'att': 'to',
    'det': 'it',
    'gillar': 'like',
    'jag': 'I',
    'mat': 'food',
    'spela': 'play',
    'tv-spel': 'videogames',
    'roligt': 'fun',
    'är': 'is'
}

while True:
    text = input('text > ')
    print('translation >', translate(text))
