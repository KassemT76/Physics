import turtle;

scrn = turtle.Screen()
scrn.bgcolor(0,0,0)
scrn.title("Physcis")

circle = turtle.Turtle()
circle.shape("circle")
circle.color("red")
circle.penup()

circle.speed(0)
circle.goto(0,100)
circle.dy = 0

floor = turtle.Turtle()
floor.shape("square")
floor.color("white")
floor.shapesize(10,100)
floor.penup()
floor.speed(0)
floor.sety(-410)

g = 1

circle.dy -= g
circle.sety(circle.ycor()+circle.dy)

while True:
    
    #bounce
    if circle.ycor() < -300:
        if circle.ycor() + circle.dy < -300:
            circle.dy = -circle.dy
    #gravity
    circle.dy -= g
    circle.sety(circle.ycor()+circle.dy)

    if (circle.ycor() < -300) & (circle.dy is 0):
        print("STOPSTOPSTOPSTOPSTOPSTOPSTOPSTOPSTOPSTOPSTOPSTOPSTOPSTOPSTOPSTOPSTOPSTOPSTOPSTOPSTOPSTOPSTOPSTOPSTOPSTOPSTOPSTOPSTOPSTOP")
        break


    print("coordinates = ", circle.ycor())
    print("speed = ", circle.dy)

    


scrn.mainloop()