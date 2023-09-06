import random

def get_rand():
    random.randint(0, 10)

i = 0
while i != 5:
    i = get_rand()
    print(i)

# En programmerare försöker skriva ett script som printar slumpade heltal (mellan 0 till 10). Efter att
# heltalet 5 slumpats och skrivits ut ska scriptet stänga.
# Något verkar inte stämma. När programmeraren kör scriptet skrivs strängen 'None' ut i all
# oändlighet.
# Felet kan åtgärdas genom att modifiera en rad i koden. Din uppgift är att besvara följande:


# Fråga 1
# vilken mening beskriver bästa orsaken till kraschen
# svar: inget svar retuneras från funktionskroppen


# fråga 2
# vilken rad behöver modifieras för att åtgärda felet
# svar: rad 4 
