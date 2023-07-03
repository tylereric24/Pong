from turtle import *
import random
from playsound import playsound
lscore = 0
rscore = 0




class Ball(Turtle):


    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        #self.shapesize(stretch_wid=1, stretch_len=1)
        self.color("blue")
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1



    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)


    def bounce_wall(self):
      playsound("wall.mp3", False)
      self.y_move *= -1

    def bounce_paddle(self):
        playsound("paddle.mp3", False)
        self.x_move *= -1
        self.move_speed *= 0.9
        r = random.randint(0, 255)
        b = random.randint(0, 255)
        g = random.randint(0, 255)
        colormode(255)
        self.color(r, g, b)


    def reset_ball(self):
        self.goto(0,0)
        self.move_speed = 0.1
        self.bounce_paddle()


