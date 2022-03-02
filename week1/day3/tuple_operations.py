"""
Tuple operations:

A tuple is basically a collection of objects that is:
1) ordered
2) immutable
3) allows duplicate members
4) allows mixing of types
"""

# how to declare a tuple
tup1 = (1,2,3,4)
print(tup1)

# how to subset a tuple, i.e. get certain elements
# out of it with indexes
print(tup1[:3])

# how to make a tuple a list (you can also make a list a tuple)
tuplist = list(tup1)
print(tuplist)

# tuples allow for mixing of data types
mixedtuple = ('a', 1, 1, 'a', 3, 4, False)
print(mixedtuple)

# not possible to add or remove elements from a tuple because it is immutable!


