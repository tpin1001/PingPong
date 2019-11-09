# Simple Pon in Python 3.7 for beginners
# By @t_pin1001
# Part 1: Getting Started

import turtle

wn = turtle.Screen()
wn.title("Pong by @t_pin1001")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.penup()
paddle_a.goto(-350, 0)

# Paddle B

# Main game loop
while True:
    wn.update()
