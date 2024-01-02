from turtle import Turtle, Screen
import turtle as t
import random

timmy_the_turtle = Turtle()
t.colormode(255)
timmy_the_turtle.shape("classic")
timmy_the_turtle.color("black")
timmy_the_turtle.pensize(10)
timmy_the_turtle.speed('fastest')

direction = [0,90,180,270]

def draw_path():
    direction_picked = random.choice(direction)
    angle = direction_picked
    timmy_the_turtle.forward(10)
    timmy_the_turtle.setheading(angle)


def pen_colour():
    timmy_the_turtle.color((random.randint(0,255), random.randint(0,255), random.randint(0,255)))


for i in range(200):
    pen_colour()
    draw_path()





    

screen = Screen()
screen.exitonclick()