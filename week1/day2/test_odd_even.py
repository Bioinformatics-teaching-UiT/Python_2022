#!/usr/bin/env python3
"""
test_odd_even.py

Takes in an integer.
Tests if it is odd or even.
Prints out answer.
"""

print('Please enter a number: ')

num = int(input())

print('You have entered: ', num)

if num % 2 == 0:
    print(f'{num} is EVEN')
else:
    print(f'{num} is ODD')
