import re

txt = "The rain in Spain"
x = re.search("\s", txt)    #The search() function searches the string for a match, and returns a Match object if there is a match.

print(x)