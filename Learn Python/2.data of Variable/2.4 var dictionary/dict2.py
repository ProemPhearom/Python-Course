# Duplicate values will overwrite existing values:
mydict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(mydict)

# To determine how many items a dictionary has, use the len() function:
print(len(mydict))#count all items