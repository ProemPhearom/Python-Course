
import re

text = " Regular Expression, is a sequence of characters 0 5 that forms a search pattern."

# regex = re.findall("ch", text)  # ch is find ch charecter
# print(regex)

#==================
regex = re.split("\s", text)  # slit() 	Returns a list where the string has been split at each match
print(regex)

