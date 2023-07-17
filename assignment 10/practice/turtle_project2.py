import os
import time
import turtle
import random
# Turtle Window
win = turtle.Screen()
win.setup(600,600)
fireworks = ['fireworks/'+file for file in os.listdir('fireworks/')]
for firework in fireworks:
    win.addshape(firework)
colors = ["gold", "red", "skyblue", "purple", "green", "turquoise"]
# Animations
win.tracer(False)

f1 = turtle.Turtle()
f1.speed(0)
f1.up()
f1.goto(200,-220)  

f2 = turtle.Turtle()
f2.speed(0)
f2.up()
f2.left(45)
f2.goto(-200,260)

# stars 
pen = turtle.Turtle()
pen.width(2)
pen.speed(0)
for i in range (5):
    pen.color(random.choice(colors))
    for i in range(8):
        pen.fd(50)
        pen.lt(225)	
    pen.up()
    pen.goto((random.randint(-150, 200), random.randint(-200, 100)))
    pen.down()

# Spirals
pen.up()
pen.goto(-280,-270)
pen.color(random.choice(colors))
pen.down()
for i in range(30):
    pen.rt(i*2)
    pen.fd(i)
    pen.circle(i*1.5)

pen.up()
pen.goto(280,270)
pen.color(random.choice(colors))
pen.down()
for i in range(30):
    pen.rt(i*2)
    pen.fd(i)
    pen.circle(i*1.5)

findex = 1
while True:
    win.update()
    f1.shape(f'fireworks/firework{findex}.gif')
    f2.shape(f'fireworks/firework{findex}.gif')
    findex = (findex + 1) % 12
    if findex == 0:
        findex = 1
    time.sleep(0.05)