"""Memory, puzzle game of number pairs.

Exercises:

1. Count and print how many taps occur.
2. Decrease the number of tiles to a 4x4 grid.
3. Detect when all tiles are revealed.
4. Center single-digit tile.
5. Use letters instead of tiles.
"""

from random import shuffle
from turtle import *

from freegames import path

car = path('car.gif')
<<<<<<< HEAD
letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'Ñ', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '1', '2', '3', '4', '5']  * 2
state = {'mark': None}
=======
tiles = list(range(32)) * 2
state = {'mark': None, 'won' : False}
>>>>>>> origin/memorI
hide = [True] * 64
counter = 0

def square(x, y):
    """Draw white square with black outline at (x, y)."""
    up()
    goto(x, y)
    down()
    color('black', 'white')
    begin_fill()
    for _ in range(4):
        forward(50)
        left(90)
    end_fill()


def index(x, y):
    """Convert (x, y) coordinates to tiles index."""
    return int((x + 200) // 50 + ((y + 200) // 50) * 8)


def xy(count):
    """Convert tiles count to (x, y) coordinates."""
    return (count % 8) * 50 - 200, (count // 8) * 50 - 200


def tap(x, y):
    """Update mark and hidden tiles based on tap."""
    global counter
    counter += 1
    spot = index(x, y)
    mark = state['mark']

    if mark is None or mark == spot or letters[mark] != letters[spot]:
        state['mark'] = spot
    else:
        hide[spot] = False
        hide[mark] = False
        state['mark'] = None


def draw():
    """Draw image and tiles."""
    clear()
    goto(0, 0)
    shape(car)
    stamp()

    for count in range(64):
        if hide[count]:
            x, y = xy(count)
            square(x, y)

    mark = state['mark']

    if mark is not None and hide[mark]:
        x, y = xy(mark)
        up()
        goto(x + 10, y + 10)
        color('black')
<<<<<<< HEAD
        write(letters[mark], font=('Arial', 30, 'normal'))
    
    up()
    goto(200, 200)
    color('red')
    write(counter, font=('Arial', 20, 'normal'))
=======
        write(tiles[mark], font=('Arial', 20, 'normal'))

    if not any(hide) and not state['won']:
        up()
        goto(-200, 100) # Mueve el cursor al centro de la pantalla
        color('red')
        write("¡Felicidades! Has encontrado todos los pares", font=('Arial', 15, 'normal'))
        #state['won'] = True

>>>>>>> origin/memorI
    update()
    ontimer(draw, 100)

shuffle(letters)
setup(420, 420, 370, 0)
addshape(car)
hideturtle()
tracer(False)
onscreenclick(tap)
draw()
done()