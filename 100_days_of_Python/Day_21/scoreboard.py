from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.l_score = 0
        self.r_score = 0
        self.color('white')
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.updatescore()

    def updatescore(self):
        self.pendown()
        self.goto(-400, 270)
        self.goto(400, 270)
        self.penup()
        self.goto(0, -270)
        self.pendown()
        self.goto(-400, -270)
        self.goto(400, -270)
        self.penup()
        self.goto(0, 270)
        self.write(f"{self.l_score} |ScoreBoard| {self.r_score}", align='center', font=('Ariel', 18, 'bold'))

    def l_scorecount(self):
        self.l_score+=1
        self.clear()
        self.updatescore()
    def r_scorecount(self):
        self.r_score +=1
        self.clear()
        self.updatescore()


    def lost(self):
        self.goto(0,0)
        self.clear()
        self.write(f"Score: {self.l_score}|{self.r_score}\nYou lost", align='center', font=('Ariel', 50, 'bold'))

