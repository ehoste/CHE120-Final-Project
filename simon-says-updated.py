from random import choice
from time import sleep
from turtle import *

from freegames import floor, vector

pattern = []
guesses = []
lives = 3
score = 0  # Initialize score

# Define tiles with letters and their associated colors
tiles = {
    vector(0, 0): ('C', 'red', 'dark red'),
    vector(0, -200): ('H', 'blue', 'dark blue'),
    vector(-200, 0): ('E', 'green', 'dark green'),
    vector(-200, -200): ('M', 'yellow', 'khaki'),
}

def grid():
    """Draw grid of tiles with letters."""
    for position, (letter, glow, dark) in tiles.items():
        draw_tile(position, letter, dark)
    update()

def draw_tile(position, letter, tile_color):
    """Draw a tile with a letter at a given position."""
    penup()
    goto(position.x + 50, position.y + 70)  # Center letter in the tile
    color(tile_color)  # Use tile_color to avoid conflict with color()
    write(letter, align='center', font=('Arial', 48, 'bold'))

def flash(tile):
    """Flash tile in grid."""
    letter, glow, dark = tiles[tile]
    draw_tile(tile, letter, glow)
    update()
    sleep(0.5)
    draw_tile(tile, letter, dark)
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

def show_status():
    """Display lives and score."""
    clear()
    penup()
    goto(-200, 200)
    color('black')
    write(f'Lives: {lives}    Score: {score}', font=('Arial', 18, 'bold'))
    grid()

def tap(x, y):
    """Respond to screen tap."""
    global lives, score
    onscreenclick(None)
    x = floor(x, 200)
    y = floor(y, 200)
    tile = vector(x, y)
    index = len(guesses)

    if tile != pattern_reversed[index]:
        lives -= 1
        show_status()
        if lives == 0:
            print("Game over!")
            exit()
        else:
            onscreenclick(tap)
            return

    guesses.append(tile)
    flash(tile)

    if len(guesses) == len(pattern):
        score += 1  # Increase score when a pattern is correctly completed
        show_status()
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
show_status()
onscreenclick(start)
done()
