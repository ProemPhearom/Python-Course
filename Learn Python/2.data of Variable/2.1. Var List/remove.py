# The remove() method removes the specified item.
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

print('===============')
# The pop() method removes the specified index.
thislist2 = ["apple", "banana", "cherry"]
thislist2.pop(1)
print(thislist2)

print('===============')
# If you do not specify the index, the pop() method removes the last item.
thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)

print('===============')
# The del keyword also removes the specified index:
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)

print('===============')
#The del keyword can also delete the list completely.

# thislist = ["apple", "banana", "cherry"]
# del thislist
# print(thislist)

print('===============')
# The clear() method empties the list.
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)