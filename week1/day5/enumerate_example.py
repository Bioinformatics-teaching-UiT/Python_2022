"""
Example of how to iterate using the enumerate function
Allows you to unpack a collection of items (like a list)
into index and element
"""

str_list = ['a', 'b', 'c', 'd']
# so let's say you need this type of info per iteration:
# 1 a
# 2 b
# 3 c
# 4 d
# use enumerate is clearer than indexing below
for i, elem in enumerate(str_list):
    print(i+1, elem)

# this is equivalent but harder to read
for i in range(len(str_list)):
    print(i+1, str_list[i])