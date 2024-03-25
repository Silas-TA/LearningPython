from turtle import Turtle, Screen, colormode
import random


screen = Screen()

# using event listenerxxxxxxxxxxxxx

# timmy = Turtle().color('purple')
# screen = Screen()
#

# def forward_move():
#     timmy.forward(10)
#
# def backward():
#     timmy.backward(10)
#
# def turn_right():
#     timmy.right(10)
#
# def turn_left():
#     timmy.left(10)
#
# def clear():
#     timmy.clear()
#     timmy.penup()
#     timmy.home()
#     timmy.pendown()
#
# screen.listen()
# screen.onkey(key = "w", fun = forward_move)
# screen.onkey(key = "s", fun = backward)
# screen.onkey(key = "a", fun = turn_left)
# screen.onkey(key = "c", fun = clear)
# screen.onkey(key = "d", fun = turn_right)

# turtle game setup xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
screen.setup(width=500, height=400)
timmy = Turtle(shape = 'turtle')
tom= Turtle(shape = 'turtle')
tum= Turtle(shape = 'turtle')
tam = Turtle(shape = 'turtle')
ten= Turtle(shape = 'turtle')

turtles=[]
turtles.append(timmy)
turtles.append(tom)
turtles.append(tum)
turtles.append(tam)
turtles.append(ten)
x_start_position = -220
y_start_position = 90

colors = ['red', 'blue', 'black', 'purple', 'green']
color_index = 0
for turtle in turtles:
    colormode(255)
    turtle.color(colors[color_index])
    color_index += 1
random.shuffle(colors)
for turtle in turtles:
    turtle.penup()
    turtle.goto(x=x_start_position, y=y_start_position)
    y_start_position += -40


def turtle_game():
    scoreline = 0
    random.randint(5, 15)
    while scoreline < 41:
        timmy.forward(random.randint(5, 15))
        tam.forward(random.randint(5, 15))
        ten.forward(random.randint(5, 15))
        tom.forward(random.randint(5, 15))
        tum.forward(random.randint(5, 15))
        scoreline +=1

def results():
    scores = []
    for turtle in turtles:
        scores.append(turtle.xcor())
    for turtle in turtles:
        if turtle.xcor() == max(scores):
            return turtle
# screen setup and text input
user_bet = screen.textinput(title = "Place your bets!", prompt="Which turtle will dominate??? Enter a color: ")
turtle_game()
turtle_color = results().color()
if turtle_color == user_bet.lower():
    tum.write(f"Congratulations, the winning turtle is {results()}", align ='center', font=('ariel', 14, 'bold'))
else:
    screen.textinput(title = 'loss', prompt= f"You lost, {turtle_color[0]} won this round")
screen.exitonclick()