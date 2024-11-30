#Olivia Darlington - OD
#Evan Hoste - EH

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


def tap(x, y): #Function that deals with when the user clicks the screen to guess sequence - EH
    """Respond to screen tap."""
    onscreenclick(None)
    x = floor(x, 200)
    y = floor(y, 200)
    tile = vector(x, y) #Determines which tile the user clicked - EH 
    index = len(guesses) #Gets the index of the user's guess - EH

    if tile != pattern[index]: #Exits game if user clicks on wrong tile - EH
        exit()

    guesses.append(tile) #Adds user's input to the guesses list and flashes square if guess is correct - EH
    flash(tile)

    if len(guesses) == len(pattern): #Starts sequence with a new addition once user has guessed entire sequence - EH
        grow()

    onscreenclick(tap) #Restarts function if there are still tiles in the sequence that the user has to guess - EH


def start(x, y):
    """Start game."""
    grow()
    onscreenclick(tap)


setup(420, 420, 370, 0) #Creates game window - EH
hideturtle() #Hides arrow from screen - EH
tracer(False) #Prevents tracing of tiles from being displayed - EH
grid() #Creates tiles on screen - EH
onscreenclick(start) #Starts game when user clicks screen - EH
done() #Closes window once game has ended - EH
