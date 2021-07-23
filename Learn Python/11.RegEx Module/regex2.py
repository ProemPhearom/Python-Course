import re
text = " Regular Expression, is a sequence of characters 0 5 that forms a search pattern."

# regex = re.findall("MO*", text)#  ("*") finde MO character

# if regex :
#     print("Data found")
# else:
#     print("Not found")

#===========
regex = re.findall("\d", text)
print(regex)

if regex :
    print("There is number contain in String")
else:
    print("Number Not found")
