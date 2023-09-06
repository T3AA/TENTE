
def get_int_from_user(prompt):
    while True:
        try:
            num = input(prompt)
            int(num)
            return num
        except ValueError:
            print("ERROR: not a valid integer")

a = get_int_from_user("a = ")
b = get_int_from_user("b = ")
c = a + b

print(a, "+", b, "=", c)


# felet här är på rad 6

# det du kan skriva för att fixa felet är
# num = int(num)

# tänk på att du vill testa om du kan omvanlda num till en ett tal (int) så
# så för att det ska bli rätt du måste skriva ----- >num = num(int)