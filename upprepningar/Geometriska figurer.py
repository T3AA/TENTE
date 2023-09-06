shape = input("shape: ")
height = int(input("height : "))

if shape == "rectangle":
    width = int(input("width: "))
    for i in range(height):
        print("#" * width)

elif shape == "triangle":
    for i in range(height):
        i += 1
        print("#" * i)
