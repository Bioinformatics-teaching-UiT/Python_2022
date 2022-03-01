#!/usr/bin/python3
"""
This is the turtle drawing exercise
to illustrate how looping works.
"""
import turtle

bob = turtle.Turtle()

print(bob)
bob.speed(10)
bob.fd(100) # forward direction
bob.lt(36) # left turn angle

for i in range(100):
    bob.lt(2)
    bob.fd(10)
    for i in range(10):
        bob.fd(100)
        bob.lt(36)
turtle.mainloop()