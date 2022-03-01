"""
This script contains common string operations
"""
str1 = 'its sunny outside'
# length function to print length of string
print(len(str1))

# slicing strings
first5letters = str1[0:5]
print(first5letters)

# string methods, print all letters in uppercase
print(str1.upper())
str2 = str1.replace(' ', '-')
print(str2)
print(str1)

# f-strings
str3 = f'The length of your string is "{len(str1)}!"'
print(str3)

# string indexing with jumps or strides
# which one flips the string?
str4 = 'abc deg hij klm 768'
print(str4[-1::-1])
print(str4[::-1])
print(str4[:-1:])

# how can you split a string by whitespace without needing to index
str4_split = str4.split(' ')
print(str4_split)
print(str4_split[::-1][0][::-1])