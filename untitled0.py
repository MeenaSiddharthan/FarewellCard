# -*- coding: utf-8 -*-
"""
Bye Reine :(
@author: m.siddharthan
"""
from turtle import *

width = 700
height = 700
screen = Screen()
screen.setup(width, height)
speed(0)

#Background
penup()
goto(0, -170)
pendown()
color("magenta")
begin_fill()
circle(300)
end_fill()

#Panda
penup()
goto(0, -100)
pendown()
color("white")
begin_fill()
circle(100)
end_fill()

penup()
goto(0,-50)
pendown()
color("white")
begin_fill()
circle(75)
end_fill()
