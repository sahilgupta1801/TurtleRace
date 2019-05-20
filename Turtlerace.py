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
akash=Turtle()
akash.color('Green')
akash.shape('turtle')
akash.penup()
sum1=0
sum2=0
sum3=0
akash.goto(-160,40)
for turn in range(100):

	pos1=randint(1,5)
	sum1=sum1+pos1
	ada.forward(pos1)

	pos2=randint(1,5)
	sum2=sum2+pos2
	bob.forward(pos2)

	pos3=randint(1,5)
	sum3=sum3+pos3
	akash.forward(pos3)

if(sum1>sum2 and sum1 >sum3):
	ada.write('Red Wins !')
elif(sum2>sum1 and sum2>sum3):
	bob.write('Blue Wins !')
elif(sum3>sum1 and sum3>sum2):
	akash.write('Green Wins !')
elif(sum1==sum2 and sum1>sum3):
	ada.write('Tie between Red and Blue')
elif(sum1==sum3 and sum1>sum2):
	ada.write('Tie between Red and Green')
elif(sum2==sum3 and sum2>sum1):
	ada.write('Tie between Blue and Green')
elif(sum1==sum2 and sum1==sum3):
	ada.write('All Tie')

win=ada.getscreen()
win.exitonclick();
