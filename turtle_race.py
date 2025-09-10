import turtle
import random 
t1=turtle.Turtle()
#no_of_turtles=int(input("enter the total no of turtle : "))

#for finish point

finish_point=turtle.Turtle()

finish_point.width(10)
finish_point.up()
finish_point.goto(-350,250)
finish_point.down()
finish_point.color("green")
finish_point.forward(700)

# for starting point
start_point=turtle.Turtle()

start_point.width(10)
start_point.up()
start_point.goto(-350,-250)
start_point.down()
start_point.color("green")
start_point.forward(700)

#for single turtle code
t1.color("red")
t1.width(2)
t1.shape("turtle")
t1.up()
t1.goto(0,-250)
t1.down()
t1.left(90)

#race start
start=0
while True:
    random_no=random.randint(1,3)
    start+=random_no
    if(start==500):
        break
    else:
        t1.forward(random_no)
    





turtle.done()