import turtle as t
from turtle import Turtle, Screen
import random
import threading

def move_turtle(turtle):
    numbers = [-90, 90]
    while True:
        turtle.fd(random.randint(-90, 90))
        turtle.right(random.choice(numbers))
        turtle.fd(random.randint(-90, 90))
        turtle.left(random.choice(numbers))

herbert = Turtle()
erika = Turtle()
pepa = Turtle()
gege = Turtle()
screen = Screen()

herbert.color("green")
erika.color("yellow")
pepa.color("orange")
gege.color("blue")

herbert.hideturtle()
erika.hideturtle()
pepa.hideturtle()
gege.hideturtle()

herbert.pensize(5)
erika.pensize(5)
pepa.pensize(5)
gege.pensize(5)

herbert.speed(3)
erika.speed(3)
pepa.speed(3)
gege.speed(3)

screen.bgcolor("black")

# Create two threads to move the turtles
herbert_thread = threading.Thread(target=move_turtle, args=(herbert,))
erika_thread = threading.Thread(target=move_turtle, args=(erika,))
pepa_thread = threading.Thread(target=move_turtle, args=(pepa,))
gege_thread = threading.Thread(target=move_turtle, args=(gege,))

# Start the threads
herbert_thread.start()
erika_thread.start()
pepa_thread.start()
gege_thread.start()

screen.exitonclick()
