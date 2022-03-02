"""
This script calculates the factorial of a given number
(The factorial of n equals (1 * 2 * … * n-1 * n)
"""

# calculation of factorial in a while loop
def factorial_whileloop(n):
    num = 1
    while n > 0:
        num = num * n
        n = n - 1
    return num

print(factorial_whileloop(0))

# calculation of the factorial in a for loop
def factorial_forloop(n):
    re = 1
    for i in range(1, n+1):
        re = re * i
    return re

print(factorial_forloop(10))
