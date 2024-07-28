from turtle import Screen, Turtle
from ball import Ball
import time
from scoreboard import Scoreboard



ball = Ball()
r_paddle = Turtle()  # Right paddle
l_paddle = Turtle()  # Left paddle
screen = Screen()

# Setup screen
screen.bgcolor('black')
screen.setup(height=600, width=800)
screen.title("Pong")
screen.tracer(0)

# Setup right paddle
r_paddle.shape("square")
r_paddle.color("white")
r_paddle.shapesize(stretch_wid=5, stretch_len=1, outline=0)
r_paddle.penup()
r_paddle.goto(350, 0)

# Setup left paddle
l_paddle.shape("square")
l_paddle.color("white")
l_paddle.shapesize(stretch_wid=5, stretch_len=1, outline=0)
l_paddle.penup()
l_paddle.goto(-350, 0)

scoreboard = Scoreboard()


# Paddle movements
def go_up():
    new_y = r_paddle.ycor() + 20
    r_paddle.goto(r_paddle.xcor(), new_y)

def go_down():
    new_y = r_paddle.ycor() - 20
    r_paddle.goto(r_paddle.xcor(), new_y)

def go_up2():
    new_y = l_paddle.ycor() + 20
    l_paddle.goto(l_paddle.xcor(), new_y)

def go_down2():
    new_y = l_paddle.ycor() - 20
    l_paddle.goto(l_paddle.xcor(), new_y)

screen.listen()
screen.onkey(go_up, "Up")
screen.onkey(go_down, "Down")
screen.onkey(go_up2, "w")
screen.onkey(go_down2, "s")

# Game loop
game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Wall collision
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Paddle collision
    if ball.distance(r_paddle) < 50 and ball.xcor() > 340:
        ball.bounce_x()
    if ball.distance(l_paddle) < 50 and ball.xcor() < -340:
        ball.bounce_x()

    #detecting right paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()
    #detecting left paddle misses
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()



    #updating scoreboard

    # if ball.xcor



screen.exitonclick()
