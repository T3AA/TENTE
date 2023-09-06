list_a = [4, 1, 9, 4, 7, 9, 3, 8, 5, 8]
list_b = [4, 1, 1, 4, 7, 9, 6, 8, 5, 8]

for x, y in zip(list_a, list_b):
    if x != y:
        print(x, y, sep="<->", end="<-DIiff!\n")
    else:
        print(x, y, sep="<->")