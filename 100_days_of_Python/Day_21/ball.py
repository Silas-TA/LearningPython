from turtle import *


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.penup()
        self.shapesize(1)
        self.x_move = 10
        self.y_move = 10

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def y_bounce(self):
        self.y_move *= -1

    def x_bounce(self):
        self.x_move *= -1

    def reset(self):
        self.goto(0,0)
        self.move()
    def lost(self):
        self.goto(0, 0)
        self.clear()
        self.write(f"Status: You lost", align='center', font=('Ariel', 50, 'bold'))
