import turtle
shelly = turtle.Turtle()
turtle.bgcolor("black") 
for n in range(6): 
    colors = ["red", "green","blue", "gold", "purple",
"yellow"]
    shelly.color(colors[n]) 
    for i in range(4): 
        shelly.forward(25)
        shelly.left(90)
    shelly.penup() 
    shelly.forward(30)
    shelly.pendown()
    shelly.hideturtle()