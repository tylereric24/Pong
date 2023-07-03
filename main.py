from turtle import *
from paddle import Paddle
from ball import Ball
import time
from playsound import playsound
from scoreboard import Scoreboard


screen = Screen()
screen.tracer(0)
screen.setup(width=800, height=600)
bgcolor("black")
screen.title("Pong")

rpaddle = Paddle((350, 0))
lpaddle = Paddle((-350, 0))
ball = Ball()
score = Scoreboard()


screen.listen()
screen.onkey(rpaddle.up, "Up")
screen.onkey(rpaddle.down, "Down")
screen.onkey(lpaddle.up, "w")
screen.onkey(lpaddle.down, "s")

game_on = True
playsound("theme.mp3", False)

while game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    #wall collision
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_wall()
    #paddle collision
    if ball.distance(rpaddle) < 50 and ball.xcor() > 320 or ball.distance(lpaddle) < 50 and ball.xcor() < -320:
        ball.bounce_paddle()
    #score
    if ball.distance(rpaddle) > 50 and ball.xcor() > 380:
        time.sleep(0.9)
        score.l_point()
        ball.reset_ball()
    if ball.distance(lpaddle) > 50 and ball.xcor() < -380:
        time.sleep(0.9)
        score.r_point()
        ball.reset_ball()

screen.exitonclick()