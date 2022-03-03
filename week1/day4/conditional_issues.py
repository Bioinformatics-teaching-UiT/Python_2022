"""
Some issues I've seen with conditional statements
"""
# say you have some string of characters
someseq = "ABBCCDDDDAAAB"

# you want to count the occurrences of AB
num_ABs = 0
for char in someseq:
    if char == 'A' or char == 'B':
        num_ABs += 1
print(num_ABs)

num_ABs = 0
for char in someseq:
    if char == 'A' or 'B': # think about why this does not work
        num_ABs += 1
print(num_ABs)