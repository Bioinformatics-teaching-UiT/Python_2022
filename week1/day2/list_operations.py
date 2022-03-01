"""
This script contains operations on lists
How to declare a list, get elements from it,
add to list, and pop elements from a list
"""
# declare a list
list1 = ['a', 100, True, 'today is tuesday']
print(list1)

# get elements from your list
print(list1[2])
print('The length of your list is', len(list1))

# adding to list
list1 = list1 + ['tomorrow is wednesday']
print(list1)
list1.append('tomorrow is wednesday')
print(list1)

# popping from a list gives you the last element
lastelement = list1.pop()
print(lastelement)
print(list1)

# you can also delete items from a list
del list1[0]
print(list1)

# when you want to sort a list, make sure the items
# in your list are sortable
# if you have a mix of types, the sort function might not work
sortedlist = list1.sort()
print(sortedlist)