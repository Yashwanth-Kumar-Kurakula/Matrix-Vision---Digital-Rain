import sys
import pygame as pg
from random import choice, randrange

RES = WIDTH, HEIGHT = 1600, 900
FONT_SIZE = 40
alpha_value = 0

COLOR_DICT = {
    "crimson fury": lambda: ((randrange(160, 255), 0, 0), (255, 153, 153)),
    "neon jungle": lambda: ((randrange(0, 50), randrange(160, 255), randrange(0, 50)), (150, 255, 150)),
    "cosmic blue": lambda: ((randrange(0, 50), randrange(0, 50), randrange(160, 255)), (0, 255, 255)),
    "aqua blaze": lambda: ((randrange(0, 90), randrange(204, 255), randrange(204, 255)), (255, 255, 255)),
    "misty meadow": lambda: ((randrange(0, 190), randrange(150, 255), randrange(0, 140)), (255, 255, 255)),
    "starlit twilight": lambda: ((randrange(85, 178), randrange(0, 135), randrange(120, 255)), (190, 145, 255)),
    "shadow pulse": lambda: ((randrange(96, 224), randrange(96, 224), randrange(96, 224)), (255, 255, 255)),
    "solar flare": lambda: ((randrange(204, 255), randrange(204, 255), randrange(0, 130)), (255, 255, 140)),
    "ember mystic": lambda: ((randrange(200, 255), randrange(100, 200), randrange(0, 125)), (255, 255, 255)),
    "bubblegum storm": lambda: ((randrange(180, 255), randrange(0, 135), randrange(180, 255)), (255, 255, 255)),
    "nebula spectrum": lambda: ((randrange(0, 255), randrange(0, 255), randrange(0, 255)), (255, 255, 255))
}

def katakana_generator(color, spl=False):
    if spl:
        return COLOR_DICT[color]()[1]
    else:
        return COLOR_DICT[color]()[0]



class Symbol:
    def __init__(self, x, y, speed):
        self.x, self.y = x, y
        self.speed = speed
        self.value = choice(normal_katakana)
        self.interval = randrange(5, 30)

    def draw(self, color):
        frames = pg.time.get_ticks()
        if not frames % self.interval:
            self.value = choice(normal_katakana if color == 'green' else special_katakana)
        self.y = self.y + self.speed if self.y < HEIGHT else -FONT_SIZE
        surface.blit(self.value, (self.x, self.y))


class SymbolColumn:
    def __init__(self, x, y):
        self.column_height = randrange(8, 24)
        self.speed = randrange(3, 7)
        self.symbols = [Symbol(x, i, self.speed) for i in range(y, y - FONT_SIZE * self.column_height, -FONT_SIZE)]

    def draw(self):
        [symbol.draw('green') if i else symbol.draw('lightgreen') for i, symbol in enumerate(self.symbols)]



options = input(f"Choose a Theme for the Matrix Fall, available themes are:\n{'\n'.join(i for i in COLOR_DICT.keys())}\nEnter your selection:  ").lower()


pg.init()
pg.display.set_caption("Matrix Fall by Yashwanth Kumar")
screen = pg.display.set_mode(RES)
surface = pg.Surface(RES)
surface.set_alpha(alpha_value)
clock = pg.time.Clock()

katakana = [chr(int('0x30a0', 16) + i) for i in range(96)]
font = pg.font.SysFont('ms mincho', FONT_SIZE, bold=True)

normal_katakana = [font.render(char, True, katakana_generator(options)) for char in katakana]
special_katakana = [font.render(char, True, katakana_generator(options, spl=True)) for char in katakana]

symbol_columns = [SymbolColumn(x, randrange(-HEIGHT, 0)) for x in range(0, WIDTH, FONT_SIZE)]

while True:
    screen.blit(surface, (0, 0))
    surface.fill(pg.Color('black'))

    [symbol_column.draw() for symbol_column in symbol_columns]

    if not pg.time.get_ticks() % 20 and alpha_value < 170:
        alpha_value += 6
        surface.set_alpha(alpha_value)

    for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_ESCAPE:
                        pg.quit()
                        sys.exit()
    pg.display.flip()
    clock.tick(60)