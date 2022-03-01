#!/usr/bin/env python3
"""
This script takes in your name and
outputs a greeting with your name.
"""

#name = input("Hello there. What is your name?") #user input name

#print(f"Hello {name}, nice to meet you.")

# add to this a way to split your first and last name with indexing using []
# then print this out

fullname = input('Hello. Please give your full name')
firstname = fullname[0:3]
print(f'Your first name is {firstname}')
lastname = fullname[4:]
print(f'Your last name is {lastname}')

fn_split = fullname.split(' ')
print('Your first name is', fn_split[0])
print('Your last name is', fn_split[1])


# addition of strings

