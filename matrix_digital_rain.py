import sys
import pygame as pg
from random import choice, randrange
import customtkinter as ctk

# RES = WIDTH, HEIGHT = 1600, 900
RES = WIDTH, HEIGHT = 1920, 1080
FONT_SIZE = 40
alpha_value = 0

COLOR_DICT = {
    "crimson fury": lambda: ((randrange(160, 255), 0, 0), (255, 153, 153)),
    "neon jungle": lambda: ((randrange(0, 50), randrange(160, 255), randrange(0, 50)), (150, 255, 150)),
    "cosmic blue": lambda: ((randrange(0, 50), randrange(0, 50), randrange(160, 255)), (0, 255, 255)),
    "aqua blaze": lambda: ((randrange(0, 90), randrange(204, 255), randrange(204, 255)), (255, 255, 255)),
    "misty meadow": lambda: ((randrange(0, 190), randrange(150, 255), randrange(0, 140)), (255, 255, 255)),
    "starlit twilight": lambda: ((randrange(85, 178), randrange(0, 135), randrange(120, 255)), (190, 145, 255)),
    "saturated nebula": lambda: ((randrange(96, 224), randrange(96, 224), randrange(96, 224)), (255, 255, 255)),
    "solar flare": lambda: ((randrange(204, 255), randrange(204, 255), randrange(0, 130)), (255, 255, 255)),
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
        self.column_height = randrange(8, 22)
        self.speed = randrange(3, 7)
        self.symbols = [Symbol(x, i, self.speed) for i in range(y, y - FONT_SIZE * self.column_height, -FONT_SIZE)]

    def draw(self):
        [symbol.draw('green') if i else symbol.draw('lightgreen') for i, symbol in enumerate(self.symbols)]

class ThemeSelector(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Matrix Fall by Yashwanth Kumar")
        self.geometry("400x500")
        self.iconbitmap("logo.ico")
        
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("green")
        
        self.selected_theme = ctk.StringVar()
        
        main_frame = ctk.CTkFrame(self)
        main_frame.pack(pady=20, padx=20, fill="both", expand=True)
        
        label = ctk.CTkLabel(main_frame, text="Choose a Matrix Theme:", font=("Arial", 16, "bold"))
        label.pack(pady=(0, 10))
        
        for theme in COLOR_DICT.keys():
            rb = ctk.CTkRadioButton(main_frame, text=theme.title(), variable=self.selected_theme, value=theme)
            rb.pack(pady=5, padx=20, anchor="w")
        
        button = ctk.CTkButton(main_frame, text="Start Matrix", command=self.start_matrix, font=("Arial", 14, "bold"))
        button.pack(pady=20)
    
    def start_matrix(self):
        self.quit()

def main():
    global alpha_value, normal_katakana, special_katakana, surface
    
    app = ThemeSelector()
    app.mainloop()
    
    selected_theme = app.selected_theme.get()
    app.destroy()
    
    if not selected_theme:
        print("No theme selected. Exiting.")
        return
    
    pg.init()
    pg.display.set_caption("Matrix Digital Rain by Yashwanth Kumar")
    screen = pg.display.set_mode(RES)
    surface = pg.Surface(RES)
    surface.set_alpha(alpha_value)
    clock = pg.time.Clock()

    katakana = [chr(int('0x30a0', 16) + i) for i in range(96)]
    font = pg.font.SysFont('ms mincho', FONT_SIZE, bold=True)

    normal_katakana = [font.render(char, True, katakana_generator(selected_theme)) for char in katakana]
    special_katakana = [font.render(char, True, katakana_generator(selected_theme, spl=True)) for char in katakana]

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

if __name__ == "__main__":
    main()