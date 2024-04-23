from turtle import Screen, Turtle
import time
# always try to implement constants before the class to ensure easy changes instead of going through the code
positions = [(0, 0), (-20, 0), (-40, 0)]
move = 20


class Snake:

    def __init__(self):
        self.snakes = []
        self.create_snake()
        self.head = self.snakes[0]

    def create_snake(self):
        for position in positions:
            self.grow(position)

    def move(self):
        index = 1
        for num in range((len(self.snakes) - 1), 0, -1):
            new_xcor = self.snakes[num-1].xcor()
            new_ycor = self.snakes[num - 1].ycor()
            self.snakes[num].goto(new_xcor, new_ycor)
        #     put this in a function

        self.snakes[0].forward(move)


    def grow(self, position):
        snake = Turtle('square')
        snake.color('white')
        snake.penup()
        snake.goto(position)
        self.snakes.append(snake)

    def extendsnake(self):
        self.grow(self.snakes[-1].position())

    def up(self):
        if self.snakes[0].heading() != 270:
            self.snakes[0].setheading(90)

    def left(self):
        if self.snakes[0].heading() != 0:
            self.snakes[0].setheading(180)

    def down(self):
        if self.snakes[0].heading() != 90:
            self.snakes[0].setheading(270)

    def right(self):
        if self.snakes[0].heading() != 180:
            self.snakes[0].setheading(0)

