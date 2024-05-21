from turtle import *
from paddle import *
from ball import *
import time
from scoreboard import Scoreboard


screen = Screen()


screen.setup(800, 600)
screen.bgcolor('black')
screen.tracer(0)
screen.listen()

l_paddle= Paddles((-350, 0))
r_paddle= Paddles((350, 0))
ball = Ball()
score= Scoreboard()
speed = 0.1
screen.onkey(r_paddle.up, 'Up')
screen.onkey(r_paddle.down, 'Down')
screen.onkey(l_paddle.up, 'w')
screen.onkey(l_paddle.down, 's')

gameOn = True
while gameOn:
    time.sleep(abs(speed))
    screen.update()
    score.updatescore()
    ball.move()

    if ball.ycor() > 250 or ball.ycor() < -250:
        ball.y_bounce()
    if ball.distance(l_paddle) < 50 and ball.xcor() < -320 or ball.distance(r_paddle) < 50 and ball.xcor() > 320:
        ball.x_bounce()
        speed-=0.005

    if ball.xcor() < -380:
        score.r_scorecount()
        ball.reset()
    elif ball.xcor() > 380:
        score.l_scorecount()
        ball.reset()


screen.exitonclick()