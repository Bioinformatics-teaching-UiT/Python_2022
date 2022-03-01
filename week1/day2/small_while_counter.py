"""
This script has a while loop to count until a certain number.
The loop exits once the number has been reached.
"""
# basic while loop
num = int(input('Please enter a positive number < 30: '))
count = 0
while count < num:
    count += 1
    print(count)