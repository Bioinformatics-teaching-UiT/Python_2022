"""
Small for-loop exercise
"""
# i implicitly initialized here!
name = input('Give me your name: ')
for letter in name:
    print(letter)

# how to arrange a for loop such that you
# print out 1 to your num, instead of 0 to your num
# since python is 0-based
for i in range(0,num):
    print(i+1)

for i in range(1,num+1):
    print(i)
