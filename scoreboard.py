from turtle import Turtle
from playsound import playsound

class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.goto(-100, 200)
        self.write(self.l_score, align="center", font=("Comic Sand", 80, "bold"))
        self.goto(100, 200)
        self.write(self.r_score, align="center", font=("Comic Sand", 80, "bold"))
        self.goto(0,260)
        for i in range(0, 17):
            self.shape("square")
            self.setheading(270)
            self.stamp()
            self.penup()
            self.forward(40)





    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, align="center", font=("Comic Sans", 80, "bold"))
        self.goto(100, 200)
        self.write(self.r_score, align="center", font=("Comic Sans", 80, "bold"))

    def l_point(self):
        playsound("score.mp3", False)
        self.l_score += 1
        self.update_scoreboard()

    def r_point(self):
        playsound("score.mp3", False)
        self.r_score += 1
        self.update_scoreboard()
        



