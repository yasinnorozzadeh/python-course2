
import turtle

form = turtle.Turtle()
turtle.getscreen().bgcolor("blue")

form.shape("circle")
form.speed("normal")
form.color("yellow")
size = 360
form.begin_fill()
for i in range(5):
    form.forward(size)
    for i in range(5):
        form.forward(size/3)
        form.left(216)
        for i in range(5):
            form.forward((size/3)/3)
            form.left(216)
            for i in range(5):
                form.forward(((size/3)/3)/3)
                form.left(216)
    form.left(216)
# form.end_fill()

turtle.mainloop()