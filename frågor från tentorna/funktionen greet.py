def greet(forename, surname):
    print("Hallå", forename, surname)

greet("Anna", "Johansson")
greet("Lars", "karlsson")
greet("Eva")
greet("Mikael", "Nilsson")



# en programerare som försöker lära sig om standardvärden har producerat koden ovan
# Scriptet kör inte som det ska när man kör scriptet kraschar python ,med TypeError på rad 6
# funktionen greet ska vid anrop ta två argument (forname och surname) sista argumentet ska anta
# standardvärdet "Andersson" om funktionsanropet endast görs med en parameter
# koden kan korrigeras genom att byta ut en felaktig programmerad rad.
# Din uppgift är att identifiera den felaktiga raden och korrigeras dess innehåll




# fråga 1
# vilken rad vill du byta ut koden för
# svar: 1

#fråga 2
# vad ska stå istället
# svar: def greet(forename, surname ="Andersson"):