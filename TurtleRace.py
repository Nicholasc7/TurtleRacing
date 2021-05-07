import turtle
import time
import random

COLORS = ['brown', 'black', 'blue', 'cyan', 'red',
          'yellow', 'orange', 'purple', 'pink', 'gray']

WIDTH, HEIGHT = 500, 500


def init_turtle():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.title("Turtle Racing")


def get_number_of_racers():
    turtles = 0
    while True:
        turtles = input("How many turtles are racing (2-10): ")

        if turtles.isdigit():
            turtles = int(turtles)
        else:
            print("\nPlease enter a valid number!... Try again\n")
            continue

        if turtles > 10 or turtles < 2:
            print("\nPlease enter a number between 2 - 10... Try again!\n")
            continue
        else:
            return turtles


def create_turtles(colors):
    turtle_list = []
    turtle_spacing = WIDTH // (len(colors) + 1)
    turtle_xpos = -250 + turtle_spacing
    racer_list = ["racer"] * turtles
    for i, colors in enumerate(colors):
        racer_list[i] = turtle.Turtle()
        racer_list[i].shape("turtle")
        racer_list[i].left(90)
        racer_list[i].penup()
        racer_list[i].goto(turtle_xpos, -230)
        turtle_xpos = turtle_xpos + turtle_spacing
        racer_list[i].pendown()
        racer_list[i].color(colors)
        turtle_list.append(racer_list[i])

    return turtle_list


def turtle_run(colors):
    turtles = create_turtles(colors)

    while True:
        for racer in turtles:
            step = random.randint(0,5)
            racer.forward(step)

            x, y = racer.pos()
            if y == 200:
                time.sleep(3)
                return colors[i]
                return False

turtles = get_number_of_racers()

random.shuffle(COLORS)

# Create an array of random colors that's the size of the number of turtles.
colors = COLORS[:turtles]

# Initiate the screen
init_turtle()

# Spawns turtles and moves then to their x pos
turtle_run(colors)
