#Olivia Darlington - OD
#Evan Hoste - EH
#Karan Bajwa - KB
#Tom Si - TS

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


def grid(): #creates a grid of tiles for gameplay for the drawn tiles - TS
    """Draw grid of tiles."""
    square(0, 0, 200, 'dark red')
    square(0, -200, 200, 'dark blue')
    square(-200, 0, 200, 'dark green')
    square(-200, -200, 200, 'khaki')
    update()


def flash(tile): #flashes tile when user clicks on tile or when the pattern is being shown - TS
    """Flash tile in grid."""
    glow, dark = tiles[tile] #refers to the colours established in tiles list such that the first colour (e.g. red) is glow, and the second is dark (e.g. dark red) - TS
    square(tile.x, tile.y, 200, glow)
    update()
    sleep(0.5) #prolongs flash so user can see it - TS
    square(tile.x, tile.y, 200, dark)
    update()
    sleep(0.5) #creates buffer between each flash of the tile - TS


def grow(): # Grows pattern and displays it to the player KB 
   # Randomly select a tile from the available options (red, blue, green, yellow). KB
   # This new tile makes the pattern longer and more challenging. KB
    tile = choice(list(tiles))
    pattern.append(tile) # Add the selected tile to the pattern list. KB

    # Flash all the tiles in the updated pattern sequentially. KB
    # This visually shows the full pattern to the player. KB
    for tile in pattern:
        flash(tile) # Briefly light up the tile on the screen. KB

    # Print the pattern length to the console for debugging or feedback. KB
   
    # Clear the guesses list to prepare for the next round of user input. KB
    # This ensures the player starts fresh without leftover data from previous rounds. KB
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
    """Initialize the game when the player clicks to begin."""
    
    # Begin the game by calling grow() to generate the first tile in the pattern. KB
    # This establishes the initial sequence that the player must memorize. KB
    grow()
    
    # Enable the tap handler to allow the player to start entering guesses. KB
    # The tap function will handle tile clicks and verify the player's input. KB
    onscreenclick(tap)


setup(420, 420, 370, 0) #Creates game window - EH
hideturtle() #Hides arrow from screen - EH
tracer(False) #Prevents tracing of tiles from being displayed - EH
grid() #Creates tiles on screen - EH
onscreenclick(start) #Starts game when user clicks screen - EH
done() #Closes window once game has ended - EH
