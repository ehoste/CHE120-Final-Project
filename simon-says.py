#Olivia Darlington - OD

from random import choice #import choice function, which allows you to pick a random tile from the list of tiles OD
from time import sleep #import sleep function, which allows the time for the tiles to glow and for there too be time between flashes OD 
from turtle import * #import turtle module which allows the grid shapes to be drawn

from freegames import floor, square, vector #import floor, which allows the user's guess to be placed in a tile, square, which draws the tiles, and vector, which allows vectors to be used to mark tile and guess locaitons on the plane OD

pattern = [] #creates list of tiles in the pattern in order OD
guesses = [] #creates list of the users guesses in order OD
tiles = { #creating a set of the four tiles to use for flashing, guesses, and pattern OD
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

    for tile in pattern:
        flash(tile)

    print('Pattern length:', len(pattern))
    guesses.clear()


def tap(x, y):
    """Respond to screen tap."""
    onscreenclick(None)
    x = floor(x, 200)
    y = floor(y, 200)
    tile = vector(x, y)
    index = len(guesses)

    if tile != pattern[index]:
        exit()

    guesses.append(tile)
    flash(tile)

    if len(guesses) == len(pattern):
        grow()

    onscreenclick(tap)


def start(x, y):
    """Start game."""
    grow()
    onscreenclick(tap)


setup(420, 420, 370, 0)
hideturtle()
tracer(False)
grid()
onscreenclick(start)
done()
