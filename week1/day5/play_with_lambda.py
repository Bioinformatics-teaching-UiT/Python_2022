"""
Test out anonymous functions
Quick and dirty ways to calculate something
or do a small operation without having
to go through the whole function naming procedure
def bla():
   blabla
"""
def squared(x):
    return x * x

square = lambda x : x * x

print(square(2))