"""
FizzBuzz problem:

1. print out sequence of numbers
2. if number is divisible by 3, print Fizz instead
3. if number is divisible by 5, print Buzz instead
4. if number is divisible by 3 and 5, print FizzBuzz
5. else just print the number
"""
num = int(input('Please give a number: '))

# careful when you reason through the logic of if and elif
# make sure you catch and evaluate statements in the
# correct conditions
for i in range(1, num + 1):
    if i % 3 == 0 and i % 5 == 0:
        print('FizzBuzz')
    elif i % 3 == 0:
        print('Fizz')
    elif i % 5 == 0:
        print('Buzz')
    else:
        print(i)