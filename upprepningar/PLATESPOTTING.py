count = 0

while count < 999:

    number_plate = input("> ").upper()
    number_plate_int = int(number_plate[-3:])

    if number_plate_int == count + 1:
        print("progress [", number_plate, "]")
        count += 1

print("slut, tack för du lekte med oss")

