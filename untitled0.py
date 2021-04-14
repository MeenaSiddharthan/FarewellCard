# -*- coding: utf-8 -*-
"""
Bye Reine :(
@author: m.siddharthan
"""
#To close turtle window type turtle.bye()
import turtle

screen = turtle.Screen()
screen.setup(700, 700)
screen.bgcolor("#f7f7f7")
turtle.speed(20)
turtle.title('Farewell Reine!')

#Background
turtle.penup()
turtle.goto(0, -300)
turtle.pendown()
turtle.color("#d9337a")
turtle.begin_fill()
turtle.circle(450)
turtle.end_fill()

#Panda
#nose
turtle.penup()
turtle.goto(-60,0)
turtle.pendown()
turtle.color("white")
def draw_triangle(length):
    for i in range(3):
        turtle.forward(length)
        turtle.right(120)
turtle.begin_fill()
draw_triangle(120)
turtle.end_fill()

#right eye
turtle.penup()
turtle.goto(150,50)
turtle.pendown()
turtle.color("white")
turtle.begin_fill()
turtle.circle(90)
turtle.end_fill()

turtle.penup()
turtle.goto(150,50)
turtle.pendown()
turtle.color("#c5c5c5")
turtle.begin_fill()
turtle.circle(50)
turtle.end_fill()

turtle.penup()
turtle.goto(150,70)
turtle.pendown()
turtle.color("white")
turtle.begin_fill()
turtle.circle(10)
turtle.end_fill()

#left eye
turtle.penup()
turtle.goto(-150,50)
turtle.pendown()
turtle.color("white")
turtle.begin_fill()
turtle.circle(90)
turtle.end_fill()

turtle.penup()
turtle.goto(-150,50)
turtle.pendown()
turtle.color("#c5c5c5")
turtle.begin_fill()
turtle.circle(50)
turtle.end_fill()

turtle.penup()
turtle.goto(-150,70)
turtle.pendown()
turtle.color("white")
turtle.begin_fill()
turtle.circle(10)
turtle.end_fill()

#smile left
turtle.penup()
turtle.goto(0,-90)
turtle.pendown()
turtle.pensize(10)
turtle.color("white")
turtle.setheading(90)
turtle.circle(100,-130)

#smile right
turtle.penup()
turtle.goto(0,-90)
turtle.pendown()
turtle.pensize(10)
turtle.color("white")
turtle.setheading(-90)
turtle.circle(100,130)

#insert textbox
turtle.penup()
turtle.color("Black")
turtle.goto(-300, -300)
turtle.write("We will miss you give us food!!", font=("Exo", 25, "bold"))
turtle.penup()
turtle.color("Black")
turtle.goto(-250, -330)
turtle.write("~Love, CRADLE", font=("Exo", 20, "italic"))
turtle.hideturtle()  

turtle.Screen().exitonclick()