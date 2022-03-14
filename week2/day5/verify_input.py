"""
This script takes user input, prints it out,
and only accepts the right type of input

Can only take in numbers

input()
"""

#while True:
#    user_input = input("Please input a number: ")
#    if user_input.isnumeric():
#        break
#    else:
#        print("Please give a valid number!")

#print('You have entered: ', user_input)

# second way to write this
while True:
    user_input = input("Please input a number: ")
    if not user_input.isnumeric():
        print("Please give a valid number!")
        continue
    break

print('You have entered: ', int(user_input))