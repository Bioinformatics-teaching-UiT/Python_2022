"""
Set operations:

A set is a collection of objects that is:
1) mutable
2) unordered (meaning you can not index to access)
3) does not allow duplicate elements
"""

# how to declare a set
set1 = {1,2,3,4,5,5}
print(set1) # notice that your set is {1,2,3,4,5} no matter how many 5's you give it

# making a list into a set and back to a list
list_w_multiples = [1,2,3,3,3,3,5,5,7,8,10,10]
list_uniqs = list(set(list_w_multiples))
print(list_uniqs)

# adding to a set (this is like append for lists)
set2 = {1,2,3}
set2.add(4)
print(set2)

# deleting from a set
set2.remove(3)
print(set2)

# common set operations
set1 = {1,2,3,4,5}
set2 = {1,2,3,6,7,8,9}

# union |
print(set1 | set2)

# intersection &
print(set1 & set2)

# difference -
print(set1 - set2)
print(set2 - set1)

# mixing types in a set sometimes re
set3 = {2,True,'a'}
print(set3)