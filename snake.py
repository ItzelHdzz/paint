"""Snake, classic arcade game.
Ana Itzel Hernández García 
Paola Rojas Domínguez 

Exercises
The food can move with the snake.
The snake and the food can change the color.
"""


from random import randrange, choice
from turtle import *

from freegames import square, vector

# Define a list of 5 colors (excluding red)
colors = ['blue', 'green', 'yellow', 'orange', 'purple']

# Initialize snake and food
food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)

# Assign random colors to snake and food
snake_color = choice(colors)
food_color = choice([color for color in colors if color!= snake_color])

# Set aim direction to (x, y)
def change(x, y):
    """Change snake direction."""
    aim.x = x
    aim.y = y
    food.x = max(min(food.x + randrange(-1, 2) * 10, 190), -200)
    food.y = max(min(food.y + randrange(-1, 2) * 10, 190), -200)

# Check if head position is within boundaries
def inside(head):
    """Return True if head inside boundaries."""
    return -200 < head.x < 190 and -200 < head.y < 190


def move():
    """Move snake forward one segment."""
    head = snake[-1].copy()
    head.move(aim)

    # Check if the head is inside boundaries and not colliding with itself
    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return

    snake.append(head)

    # Check if the head has reached the food
    if head == food:
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    else:
        snake.pop(0)

    # Clear the screen and draw the snake and food
    clear()

    for body in snake:
        square(body.x, body.y, 9, snake_color)

    square(food.x, food.y, 9, food_color)
    update()
    ontimer(move, 100)


setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
move()
done()