message1 = "please do not hack my computer.\n"
message2 = "my antivirus is out of date."

with open("MOTD.txt") as f:
    f.write(message1)
    f.write(message2)

print("SUCCESS: Important message written to file.")

# fråga 1
# vad är det som orskar kraschen ?
# svar: rad4 behöver skrivas om

# fråga 2
# skriv om programmet så att felet åtgärdas
# svar: with open("MOTD.txt", "w") as f: