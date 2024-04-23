from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color('white')
        self.penup()
        self.goto(0, 300)
        self.hideturtle()
        self.updatescore()

    def updatescore(self):
        self.pendown()
        self.goto(-350, 300)
        self.goto(350, 300)
        self.penup()
        self.goto(0, 300)
        self.write(f"Score: {self.score}", align='center', font=('Ariel', 24, 'bold'))

    def scorecount(self):
        self.score +=1
        self.clear()
        self.updatescore()


    def lost(self):
        self.goto(0,0)
        self.clear()
        self.write(f"Score: {self.score}\nYou lost", align='center', font=('Ariel', 50, 'bold'))

