print(".: SUMMER OF INTEGERS :.")
print("------------------------")

numbers = []

i = True
while i != "0":
    i = input("> ")
    numbers.append(i)

print("summan av alla heltal är", sum(numbers))

# En programmerare försöker skriva ett program där en användare matar in ett i förväg okänt antal
# heltal. När användaren matar in heltalet 0 ska programmet skriva ut summan av alla inmatade
# heltal:
# När programmeraren testar programmet uppstår ett fel av typen TypeError:
# Koden kan korrigeras genom att byta ut en felaktigt programmerad rad. Din uppgift är att identifiera
# den felaktiga raden och korrigera dess innehåll.


# fråga 1
# vilken rad vill du byta ut koden för
# svar: 9

#fråga 2
# vad ska stå istället
# svar: numbers.append(int(i))

