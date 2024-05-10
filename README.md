<h1>Evidencia de proyecto</h1>
Alumnas: </br>
  Ana Itzel Hernández García A01737526 </br>
  Paola Rojas Domínguez A01737136 </br>
<h2>Paint</h2>
<h3>Descripción</h3>
Dibuja líneas y formas en la pantalla. Haga clic para marcar el inicio de una forma y haga clic nuevamente para marcar su final. Se pueden seleccionar diferentes formas y colores mediante el teclado.
<h3>Cambios realizados</h3>
Se añadió el color rosa

```python
onkey(lambda: color('pink'), 'P')
```
Se completo la función para diujar un círculo

```python
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
```
Se completó la función para dibujar un rectángulo
```python
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
```
Se completó la función para dibujar un triángulo
```python
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
```
<h2>Snake</h2>
<h3>Descripción</h3>
Clásico juego de arcade. Utilice las teclas de flecha para navegar y comer la comida. Cada vez que se consuma, la serpiente crece un segmento más. ¡Evita comerte o salirte de los límites!
<h3>Cambios realizados</h3>
La comida se mueve un espacio cada vez que la serpiente cambia de dirección
```python
```
La serpiente y la comida cambian de color cada vez que se inicia el juego
```python
```
<h2>Pacman</h2>
<h3>Descripción</h3>
Clásico juego de arcade. Usa las teclas de flecha para navegar y comer toda la comida blanca. Cuidado con los fantasmas rojos que deambulan por el laberinto.
<h3>Cambios realizados</h3>
Los fantasmas siguen de mejor forma a pacman
```python
```
El tablero fue modigficado
```python
```
Los fantasmas son más rápidos
```python
```
<h2>Cannon</h2>
<h3>Descripción</h3>
Movimiento de proyectiles. Haz clic en la pantalla para disparar tu bala de cañón. La bala de cañón hace estallar globos azules a su paso. Explota todos los globos antes de que puedan cruzar la pantalla.
<h3>Cambios realizados</h3>
La velocidad de la bala es mayor
```python
```
Los globos se mueven más rápido
```python
```
El juego es infinito
```python
```
<h2>Memory</h2>
<h3>Descripción</h3>
Juego de rompecabezas de pares de números. Haga clic en un mosaico para revelar un número. Haga coincidir dos números y las fichas desaparecerán para revelar una imagen.
<h3>Cambios realizados</h3>
Se añadió con contador de taps

```python
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
```
Los dígitos están centrados

```python
if mark is not None and hide[mark]:
        x, y = xy(mark)
        up()
        goto(x + 10, y + 10)
        color('black')
        write(letters[mark], font=('Arial', 30, 'normal'))
```
Se notifica cuando se desbloquearon todos los cuadros

```python
if not any(hide) and not state['won']:
        up()
        goto(-200, 100)
        color('red')
        write("Congratulations! You have found all the pairs", font=('Arial', 15, 'normal'))
        #state['won'] = True
```

Se usan letras en lugar de números
```python
letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'Ñ', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'aa', 'bb', 'cc', 'dd', 'ee']  * 2
```
