# En programmerare försöker förhindra minderåriga från att ansluta till ett chattprogram. För att göra detta tvingas
# användare mata in information om sin ålder under tiden programmet startar:

def get_name():
    return input("ange ditt name: ")

def get_age():
    return input("ange din ålder: ")

name = get_name()
age = get_age()

if age < 15:
    print("Du behöver vara 15 för att starta det här programmet")
else:
    print("välkommen")

# fråga 1
# vad beror felet på
# svar: felet uppstår eftersom åldern som användaren matar in är en
# sträng och inte ett heltal d.v.s en integer, och det gör att jämförelsen met talet 15 inte fungerar

# fråga 2
# hur kan felet åtgärdas
# svar: rad 8 kan ändras till --- return int(input("ange din ålder: ))