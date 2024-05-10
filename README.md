<h1>Evidencia de proyecto</h1>
Alumnas: </br>
  Ana Itzel Hernández García A01737526 </br>
  Paola Rojas Domínguez A01737136 </br>
<h2>Paint</h2>

```python
"""Paint, for drawing shapes.
    Ana Itzel Hernandez Garcia A01737526
    Paola Rojas Dominguez A01737136

Changes made:
    -Pink color added
    -Circle function completed
    -Rectangle function completed
    -Triangle function completed
"""

#Import libraries
from turtle import *
from freegames import vector
import math

def line(start, end):
    """Draw line from start to end."""
    up()
    goto(start.x, start.y)
    down()
    goto(end.x, end.y)


def square(start, end):
    """Draw square from start to end."""
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    for count in range(4):
        forward(end.x - start.x)
        left(90)

    end_fill()


def circle(start, end):
    """Draw circle from start to end."""
    up()
    goto(start.x, start.y)
    down()
    begin_fill()
    radius = abs(end - start) / 2
    circ = 2 * math.pi * radius
    step = circ / 360
    angle = 360
    while angle > 0:
        forward(step)
        left(1)
        angle -= 1
    end_fill()


def rectangle(start, end):
    """Draw rectangle from start to end."""
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    for count in range(2):
        forward(end.x - start.x)
        left(90)
        forward(end.y - start.y)
        left(90)

    end_fill()


def triangle(start, end):
    """Draw triangle from start to end."""
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    # Length of the line segment between start and end
    length = math.sqrt((end.x - start.x)**2 + (end.y - start.y)**2)

    # Angle of the line segment
    angle = math.atan2(end.y - start.y, end.x - start.x)

    # Coordinates of the third vertex (assuming equilateral triangle)
    third_x = end.x + length * math.cos(angle + (2 * math.pi / 3))
    third_y = end.y + length * math.sin(angle + (2 * math.pi / 3))

    # Draw the triangle
    goto(end.x, end.y)
    goto(third_x, third_y)
    goto(start.x, start.y)

    end_fill()


def tap(x, y):
    """Store starting point or draw shape."""
    start = state['start']

    if start is None:
        state['start'] = vector(x, y)
    else:
        shape = state['shape']
        end = vector(x, y)
        shape(start, end)
        state['start'] = None


def store(key, value):
    """Store value in state at key."""
    state[key] = value


state = {'start': None, 'shape': line}
setup(420, 420, 370, 0)
onscreenclick(tap)
listen()
onkey(undo, 'u')
#Colors you can draw with
onkey(lambda: color('black'), 'K')
onkey(lambda: color('white'), 'W')
onkey(lambda: color('green'), 'G')
onkey(lambda: color('blue'), 'B')
onkey(lambda: color('red'), 'R')
onkey(lambda: color('pink'), 'P') #New color added
#Figures that can be drawn
onkey(lambda: store('shape', line), 'l')
onkey(lambda: store('shape', square), 's')
onkey(lambda: store('shape', circle), 'c')
onkey(lambda: store('shape', rectangle), 'r')
onkey(lambda: store('shape', triangle), 't')
done()
```

<h2>Snake</h2>
```python
```
<h2>Pacman</h2>
```python
```
<h2>Cannon</h2>
```python
```
<h2>Memory</h2>

```python
"""Memory, puzzle game of number pairs.
    Ana Itzel Hernandez Garcia A01737526
    Paola Rojas Dominguez A01737136

Changes made:
    -The number of taps are counted and displayed
    -Detect when all boxes have been uncovered
    -The digit is centered in the box
    -Letters are used instead of numbers
"""

#Import libraries
from random import shuffle
from turtle import *
from freegames import path

#Variables are set
car = path('car.gif')
#List of letters
letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'Ñ', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'aa', 'bb', 'cc', 'dd', 'ee']  * 2
state = {'mark': None, 'won' : False}
hide = [True] * 64
counter = 0 #variable that keeps the tap count

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
        write(letters[mark], font=('Arial', 30, 'normal'))

    if not any(hide) and not state['won']:
        up()
        goto(-200, 100)
        color('red')
        write("Congratulations! You have found all the pairs", font=('Arial', 15, 'normal')) # The message appears when all the boxes have been uncovered
        #state['won'] = True

    up()
    goto(200, 200)
    color('red')
    write(counter, font=('Arial', 20, 'normal')) #The counter is displayed
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
```
