"""
Module: name_drawer

A program to draw a name using one (or more) turtles.

Authors:
1) Name - USD Email Address
2) Name - USD Email Address
"""
import turtle

screen = turtle.Screen()
t = turtle.Turtle()

# Draw 'S'
t.penup()
t.goto(-200, 0)
t.pendown()
t.left(90)
t.forward(50)
t.right(90)
t.forward(30)
t.right(90)
t.forward(25)
t.right(90)
t.forward(30)
t.left(90)
t.forward(25)
t.left(90)
t.forward(30)

# Move to next letter
t.penup()
t.right(90)
t.forward(10)
t.right(90)
t.forward(50)
t.left(90)
t.pendown()

# Draw 'O'
t.circle(25)

# Move to next letter
t.penup()
t.left(90)
t.forward(60)
t.right(90)
t.pendown()

# Draw 'P'
t.forward(50)
t.right(90)
t.circle(-15, 180)

# Move to next letter
t.penup()
t.left(90)
t.forward(30)
t.pendown()

# Draw 'H'
t.left(90)
t.forward(50)
t.penup()
t.backward(25)
t.right(90)
t.pendown()
t.forward(30)
t.left(90)
t.pendown()
t.forward(25)
t.backward(50)

# Move to next letter
t.penup()
t.right(90)
t.forward(40)
t.left(90)
t.pendown()

# Draw 'I'
t.forward(50)
t.backward(25)
t.right(90)
t.forward(15)
t.left(90)
t.forward(25)
t.backward(50)

# Move to next letter
t.penup()
t.right(90)
t.forward(30)
t.left(90)
t.pendown()

# Draw 'A'
t.left(75)
t.forward(53)
t.right(150)
t.forward(53)
t.backward(26)
t.right(105)
t.forward(20)

# Keep window open
screen.mainloop()
