from turtle import Screen, Turtle
from food import Food
from snake import Snake
from scoreboard import Scoreboard
import time
screen = Screen()
screen.setup(width=700, height=700)


# function for difficulty the more difficult the faster the snake (smaller time.sleep)


def restart():
    time.sleep(2)
    return screen.textinput("Would you like to play again?", 'Enter Y to continue and N to end')



def snakegame():
    screen.bgcolor('black')
    screen.title('Ultimate Snake')
    screen.tracer(0)

    snake = Snake()
    food = Food()
    scoreboard = Scoreboard()

    screen.listen()
    screen.onkey(snake.up, 'Up')
    screen.onkey(snake.down, 'Down')
    screen.onkey(snake.left, 'Left')
    screen.onkey(snake.right, 'Right')
    isRunning = True
    # keep game running
    while isRunning:
        screen.update()
        time.sleep(0.1)
        snake.move()
        # detect Collision with wall/restart option
        if snake.head.xcor() >= 350 or snake.head.ycor() >= 310 or snake.head.xcor() <= -350 or snake.head.ycor() <= -350:
            isRunning = False
            scoreboard.lost()
            if restart().lower() == 'y':
                screen.clear()
                snakegame()
            else:
                screen.clear()
        # Growing the snake
        if snake.head.distance(food) < 15:
            food.change()
            snake.extendsnake()
            scoreboard.scorecount()
        # detect Collision with body
        for segment in snake.snakes[1:]:
            if snake.head.distance(segment) < 7:
                isRunning = False
                scoreboard.lost()


    # time.sleep(1)


snakegame()


screen.exitonclick()

