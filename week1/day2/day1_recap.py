"""
Recap with short exercises from Day 1
"""

# input exercise - what is your name, how old are you,
# and how old will you be in 10 years?

#name = input('Please give your name: ')
#age = int(input('Please give your age: '))
#print(f'Hello {name}, you are now {age} years old, and will be {age+10} in 10 years.')


# string exercise - count the number of occurrences of A in the following string:
str1 = "feiojsACqjicjlkjAAAAwijejflweifjijkA"

print(f"A occurs {str1.count('A')} times in your string")

# Does the string "wije" occur in this string? If so, at which index?
print(f"'wije' occurs at {str1.find('wije')}")
print(str1.find('blabla'))

# Reverse the string
print(str1[::-1])
# Split the string at every "j"

split_str1 = str1.split('j')
print(split_str1)
print(type(split_str1))


