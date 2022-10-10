from turtle import Turtle, Screen

timmy_turtle = Turtle()

timmy_turtle.shape('turtle')
timmy_turtle.color('#42d7f5')
timmy_turtle.pencolor('#000000')

for i in range(0, 5):
    timmy_turtle.right(36)
    timmy_turtle.forward(100)
    timmy_turtle.left(252)
    
timmy_turtle.goto(30.90,-95.11)  
    
timmy_turtle.circle(50)    
                 
screen = Screen()
screen.exitonclick()