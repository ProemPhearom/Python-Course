import re
text = " Regular Expression, is a sequence of characters 0 5 that forms a search pattern."

regex = re.findall("\s", text)  # ("\s") is find space
print(regex)

if regex :
    print("There is Space contain in String")
else:
    print("Space Number Not found")
