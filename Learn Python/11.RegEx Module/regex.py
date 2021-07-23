import re # Regular Expression labrary

text = "That's hat cost around 20 bucks"

# regex = re.findall("\d", text)# 2 digit
# print(regex)
# regex = re.findall("^That ", text)# findall ("^") finde character

regex = re.findall("b$ ", text)#  ("$") finde last character

if regex :
    print("Data found")
else:
    print("Not found")
