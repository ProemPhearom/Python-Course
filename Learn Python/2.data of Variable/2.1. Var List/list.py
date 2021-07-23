# Lists are used to store multiple items in a single variable.
mylist = ["apple", "banana", "cherry"]
print(mylist)

#List items are indexed and you can access them by referring to the index number:
thislist = ["apple", "banana", "cherry"]
print(thislist[1])

# Change Item Value
# To change the value of a specific item, refer to the index number:
carslist = ["Camery", "Toyota", "Ford"]
carslist[1] = "BMW"
print(carslist)

# To add an item to the end of the list, use the append() method:

thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)