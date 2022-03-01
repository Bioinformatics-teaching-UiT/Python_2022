"""
Exercises with list comprehensions
"""

# How you would normally get cubes into a list
# with a for loop
cubes = []
for i in range(1,21):
    icubed = i**3
    cubes.append(icubed)

print(cubes)

# But you can do this in one line as a list comprehension
cubes = [i**3 for i in range(1,21)]
print(cubes)

# Dict comprehensions also exist!!
cubedict = {i:i**3 for i in range(1,21)}
print(cubedict)