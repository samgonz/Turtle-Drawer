from random import randint
from turtle import Screen, Turtle, colormode

colormode(255)
timmy_turtle = Turtle()

def get_degree_turn(sides):
    return 360 / sides

min_sides = 3
max_sides = 11
for sides in range(min_sides, max_sides):
    degree_turn = get_degree_turn(sides)
    timmy_turtle.color(randint(0,255), randint(0,255), randint(0,255))
    #Draw Shape
    for i in range(1, sides+1):
        timmy_turtle.right(degree_turn)
        timmy_turtle.forward(50)        

screen = Screen()
screen.exitonclick()