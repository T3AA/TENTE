names = ["alice", "noah", "maja", "william", "vera", "liam"]
n = ""

for name in names:
    if name == "noah":
        continue
    elif name == "william":
        break
    n += name

print(n)

# fråga 1
# vad skrivs ut?
# det som kommer skrivas ut här är "AliceMaja"




# kolla på rad 6 så vad gör -continue-
# den hoppar över till maja
# vad händer på rad 7 och 8
# den stoppar vid william
