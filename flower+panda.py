# -*- coding: utf-8 -*-
"""
Bye Reine :(
@author: m.siddharthan
"""
#To close turtle window type turtle.bye()
import turtle
from random import randint
import time

screen = turtle.Screen()
screen.setup(700, 700)
screen.bgcolor("#f7f7f7")
turtle.speed(1)
turtle.title('Farewell Reine!')

messages = {'Meena':['Hi Reine', 'Thank you for imparting some of your knowledge', 'onto us! We used it to make this E-card', 'We hope you like it! Keep in touch!'], 
            'Li Tong':['All the best at your new job.','Take care'], 
            'Esther':['All the best at your new job.','Take care'], 
            'Prof Annabel':['Dear Reine,','Thanks for your good efforts and contributions', 'to our project. Your creative ideas are most','appreciated. All the very best for your','new job and future endeavours.'],
            'Tiffany':['Dear Reine,','It\'s been very nice to meet you although', 'it has only been a few months, I’m glad' ,'that I had chance to work with you :)', 'Wish you all the best in your new job and future!'],
            'Alicia':['Dear Reine,', 'Thank you for your hard work and creativity', 'throughout this project. It has been a pleasure', 'working with you and I wish you all the best', 'in your future endeavours.'],
            'Shien':['Enjoyed talking to you and I\'ll miss','your cheerfulness. All the best :)']}

def text(turtle, i, color, x, y):
    turtle.penup()
    turtle.color(color)
    turtle.goto(x,y)
    a = len(messages[i])
    txt=''
    while a > 0:
        txt = txt+str(messages[i][0]+'\n')
        del messages[i][0]
        a-=1
    txt = txt+str('~'+i)
    turtle.write(txt, font=("Exo", 12, "italic"))
    turtle.hideturtle()
    
#messages
turtle.colormode(255)
for i in messages.keys():
    x=randint(-280,60)
    y=randint(-280,250)
    print(x,y)
    color=(randint(0, 150), randint(0, 150), randint(0, 150))
    text(turtle, i, color, x, y)
    time.sleep(6)
    turtle.clear()
    
turtle.speed(0)
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
turtle.write("All the best at your new job, we will miss you!!", font=("Exo", 25, "bold"))
turtle.penup()
turtle.color("Black")
turtle.goto(-250, -330)
turtle.write("~Love, CRADLE", font=("Exo", 20, "italic"))
turtle.hideturtle()  

turtle.Screen().exitonclick()