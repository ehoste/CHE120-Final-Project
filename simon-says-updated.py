from random import choice
from time import sleep
from turtle import *

from freegames import floor, square, vector

pattern = []
guesses = []
lives = 3 

tiles = {
    vector(0, 0): ('red', 'dark red'),
    vector(0, -200): ('blue', 'dark blue'),
    vector(-200, 0): ('green', 'dark green'),
    vector(-200, -200): ('yellow', 'khaki'),
}


def grid():
    """Draw grid of tiles."""
    square(0, 0, 200, 'dark red')
    square(0, -200, 200, 'dark blue')
    square(-200, 0, 200, 'dark green')
    square(-200, -200, 200, 'khaki')
    update()


def flash(tile):
    """Flash tile in grid."""
    glow, dark = tiles[tile]
    square(tile.x, tile.y, 200, glow)
    update()
    sleep(0.5)
    square(tile.x, tile.y, 200, dark)
    update()
    sleep(0.5)
    
def grow():
    """Grow pattern and flash tiles."""
    tile = choice(list(tiles))
    pattern.append(tile)
    global pattern_reversed
    pattern_reversed = list(reversed(pattern))

    for tile in pattern:
        flash(tile)

    print('Pattern length:', len(pattern))
    guesses.clear()

def show_lives(): 
    clear()
    penup()
    goto(-200,200)
    color ('black')
    write(f'Lives: {lives}', font=('Arial', 18, 'bold'))
    grid()

def tap(x, y):
    """Respond to screen tap."""
    global lives 
    onscreenclick(None)
    x = floor(x, 200)
    y = floor(y, 200)
    tile = vector(x, y)
    index = len(guesses)

    if tile != pattern_reversed[index]: 
        lives -=1
        show_lives()
        if lives == 0: 
            print ("Game over!")
            exit()
        else: 
            onscreenclick(tap)
            return 

    guesses.append(tile)
    flash(tile)

    if len(guesses) == len(pattern):
        grow()

    onscreenclick(tap)


def start(x, y):
    """Start game."""
    grow()
    onscreenclick(tap)


setup(420, 475, 370, 0)
hideturtle()
tracer(False)
grid()
show_lives()
onscreenclick(start)
done()