#!/bin/python3
from turtle import *
from random import randint
penup()
goto(-140,140)
for step in range(15):
  speed(0)
  write(step, align='center')
  right(90)
  forward(10)
  pendown()
  forward(150)
  penup()
  backward(160)
  left(90)
  forward(20)

ada=Turtle()
ada.color('Red')
ada.shape('turtle')
ada.penup()
ada.goto(-160,100)
bob=Turtle()
bob.color('Blue')
bob.shape('turtle')
bob.penup()
bob.goto(-160,70)
for turn in range(100):
  
  ada.forward(randint(1,5))
  bob.forward(randint(1,5))
