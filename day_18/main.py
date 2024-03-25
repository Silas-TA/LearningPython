from turtle import *  # Turtle, Screen
import random
import colorgram as cg

timmy = Turtle()
timmy.shape('turtle')
timmy.color('purple')


# dashed lines
# for line in range(100):
#     timmy.forward(10)
#     timmy.penup()
#     timmy.forward(10)
#     timmy.pendown()
# write code to divide by 360 until 10
# for shape in range(3, 11):
#     for i in range(shape):
#         timmy.forward(100)
#         timmy.right((360/shape))

# Random walk


# def random_color():
#     colormode(255)
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     ran_color = (r, g, b)
#     return ran_color
#

#
# def walk():
#     directions = [0, 90, 180, 270]
#     return random.choice(directions)
#
#
# for i in range(1000):
#     timmy.pensize(5)
#     timmy.color(random_color())
#     timmy.forward(30)
#     timmy.speed('fastest')
#     timmy.setheading(walk())

# spirogram or sumn like that
# for i in range(1, 101):
#     timmy.speed('fastest')
#     timmy.color(random_color())
#     timmy.circle(50, 360)
#     timmy.right(50)
#


# generating colors from colorgram
# def extract(photo, num):
#     colors = cg.extract(photo, num)
#     print(colors)
#     rgb_values = []
#
#     for color in colors:
#         r = color.rgb.r
#         g = color.rgb.g
#         b = color.rgb.b
#         rgb_values.append((r, g, b))
#     return rgb_values
#
#
#
# photo = r'damien.jpg'
# length = 88

def forward_move(colors):
    colormode(255)
    print(timmy.position())
    for i in range(0, 9):
        timmy.dot(10, colors[i])
        timmy.penup()
        timmy.forward(40)
        timmy.pendown()
    print(timmy.position())


def backward():
    timmy.penup()
    timmy.left(90)
    timmy.forward(40)
    timmy.left(90)
    for i in range(0, 9):
        timmy.forward(40)
    timmy.right(180)
    timmy.pendown()

def generate_color_list(num_colors):
    colors = []
    while len(colors) < num_colors:
        # Generate a random RGB color
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)

        # Check if the color is not close to white
        if r > 200 and g > 200 and b > 200:
            continue

        # Add the color to the list
        colors.append((r, g, b))

    return colors


colors = generate_color_list(20)
print(colors)
for i in range(0, 6):
    forward_move(colors)
    backward()
    random.shuffle(colors)

screen = Screen()
screen.exitonclick()
