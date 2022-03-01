"""
Script to test if an input number is even or odd
"""
num = int(input('Please enter a number: '))
if num % 2 == 0:
    print(f'{num} is EVEN!')
else:
    print(f'{num} is ODD!')