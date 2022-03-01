#!/usr/bin/python3
import turtle
keyword = input("Please insert a keyword:")

if keyword == "eye":
    color_inside = input("Farbe:")  
    color_middle = "grey"
    color_outside = "grey"
    color_kern = "black"
elif keyword == "earth":
    color_inside = "red"
    color_middle = "brown"
    color_outside = "green"
    color_kern = "orange"
else:
    color_inside = "grey"



bob = turtle.Turtle()

print(bob)
bob.speed(10)
bob.lt(72)

for i in range(180):
    bob.lt(2)
    for i in range(1):
        bob.pencolor(color_kern)
        bob.forward(50)
        bob.pencolor(color_inside)
        bob.forward(50)
        bob.lt(72)
    for i in range(1):
        bob.pencolor(color_middle)
        bob.forward(100)
        bob.lt(72)
    for i in range(1):
        bob.pencolor(color_outside)
        bob.forward(100)
        bob.lt(72)
    for i in range(1):
        bob.pencolor(color_middle)
        bob.forward(100)
        bob.lt(72)
    for i in range(1):
        bob.pencolor(color_inside)
        bob.forward(50)
        bob.pencolor(color_kern)
        bob.forward(50)
        bob.lt(72)

turtle.mainloop()