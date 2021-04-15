# -*- coding: utf-8 -*-
"""
Bye Reine :(
@author: m.siddharthan
"""
#To close turtle window type turtle.bye()
import turtle
from random import randint

screen = turtle.Screen()
screen.setup(700, 700)
screen.bgcolor("#f7f7f7")
turtle.speed(-50)
turtle.title('Farewell Reine!')

messages = {'Meena':['All the best at your new job.',' Take care'], 
            'Litong':['All the best at your new job.',' Take care'], 
            'Esther':['All the best at your new job.',' Take care'], 
            'Alicia':['All the best at your new job.',' Take care'],
            'Zhan Jie':['All the best at your new job.',' Take care']}

def text(turtle, i, color, x, y):
    turtle.penup()
    turtle.color(color)
    turtle.goto(x,y)
    txt = str(messages[i][0]+'\n'+messages[i][1]+'\n'+'~'+i)
    turtle.write(txt, font=("Exo", 12, "italic"))
    turtle.hideturtle()
    
##flower
#def draw_flower (turtle, color, x, y):
#    for i in range(5): #no of petals
#        turtle.penup()
#        turtle.color(color)
#        turtle.goto(x,y)
#        turtle.pendown()    
#        turtle.begin_fill()
#        heading = turtle.heading()
#        turtle.circle(10, 90)
#        turtle.left(90)
#        turtle.circle(10, 90)
#        turtle.setheading(heading)
#        turtle.left(72) #360/no of petals
#        turtle.end_fill()
#        turtle.hideturtle()  
#flower rain
turtle.colormode(255)
color=(randint(0, 255), randint(0, 255), randint(0, 255))
for i in messages.keys():
    x=randint(-350,250)
    y=randint(-280,350)
    print(x,y)
    color=(randint(0, 255), randint(0, 255), randint(0, 255))
    text(turtle, i, color, x, y)
    
#while a > 0:
#    print(messages[a]+'\n'+'~'+)
#    x=randint(-350,350)
#    y=randint(-350,350)
#    print(x,y)
#    a-=1
#    color=(randint(0, 255), randint(0, 255), randint(0, 255))

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
turtle.speed(0)
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