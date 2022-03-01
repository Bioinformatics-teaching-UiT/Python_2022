#!/usr/bin/python3
import turtle

bob = turtle.Turtle()

print(bob)
bob.speed(10)
bob.fd(100)
bob.lt(36)

for i in range(180):
    bob.lt(2)
    for i in range(10):
        bob.fd(100)
        bob.lt(36)
turtle.mainloop()