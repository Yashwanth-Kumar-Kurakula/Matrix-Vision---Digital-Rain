import pygame as pg
import numpy as np
import pygame.camera
import sys
import customtkinter as ctk
from tkinter import filedialog

class Matrix:
    def __init__(self, app, font_size=8):
        self.app = app
        self.FONT_SIZE = font_size
        self.SIZE = self.ROWS, self.COLS = app.HEIGHT // font_size, app.WIDTH // font_size
        self.katakana = np.array([chr(int('0x30a0', 16) + i) for i in range(96)] + ['' for _ in range(10)])
        self.font = pg.font.SysFont('ms mincho', font_size, bold=True)

        self.matrix = np.random.choice(self.katakana, self.SIZE)
        self.char_intervals = np.random.randint(25, 50, size=self.SIZE)
        self.cols_speed = np.random.randint(1, 500, size=self.SIZE)
        self.prerendered_chars = self.get_prerendered_chars()

        self.image = None

    def get_frame(self):
        image = self.app.cam.get_image()
        image = pg.transform.scale(image, self.app.RES)
        pixel_array = pg.pixelarray.PixelArray(image)
        return pixel_array

    def get_image(self, path_to_file):
        image = pg.image.load(path_to_file)
        image = pg.transform.scale(image, self.app.RES)
        pixel_array = pg.pixelarray.PixelArray(image)
        return pixel_array

    def get_prerendered_chars(self):
        char_colors = [(0, green, 0) for green in range(256)]
        prerendered_chars = {}
        for char in self.katakana:
            prerendered_char = {(char, color): self.font.render(char, True, color) for color in char_colors}
            prerendered_chars.update(prerendered_char)
        return prerendered_chars

    def run(self):
        frames = pg.time.get_ticks()
        self.change_chars(frames)
        self.shift_column(frames)
        if self.app.option == 1:
            self.option_one()
        elif self.app.option == 2:
            self.option_two()
        elif self.app.option == 3:
            self.option_three()

    def shift_column(self, frames):
        num_cols = np.argwhere(frames % self.cols_speed == 0)
        num_cols = num_cols[:, 1]
        num_cols = np.unique(num_cols)
        self.matrix[:, num_cols] = np.roll(self.matrix[:, num_cols], shift=1, axis=0)

    def change_chars(self, frames):
        mask = np.argwhere(frames % self.char_intervals == 0)
        new_chars = np.random.choice(self.katakana, mask.shape[0])
        self.matrix[mask[:, 0], mask[:, 1]] = new_chars
    
    def option_one(self):
        for y, row in enumerate(self.matrix):
            for x, char in enumerate(row):
                pos = x * self.FONT_SIZE, y * self.FONT_SIZE
                char = self.font.render(char, False, (0, 170, 0))
                self.app.surface.blit(char, pos)
    
    def option_two(self):
        for y, row in enumerate(self.matrix):
            for x, char in enumerate(row):
                if char:
                    pos = x * self.FONT_SIZE, y * self.FONT_SIZE
                    try:
                        pixel_color = self.image[pos[0]][pos[1]]
                        red = pixel_color >> 16 & 255
                        green = pixel_color >> 8 & 255
                        blue = pixel_color & 255
                        if red and green and blue:
                            color = (red + green + blue) // 3
                            color = 220 if 160 < color < 220 else color
                            char = self.prerendered_chars[(char, (0, color, 0))]
                            char.set_alpha(color + 60)
                            self.app.surface.blit(char, pos)
                    except IndexError:
                        continue

    def option_three(self):
        self.image = self.get_frame()
        for y, row in enumerate(self.matrix):
            for x, char in enumerate(row):
                if char:
                    pos = x * self.FONT_SIZE, y * self.FONT_SIZE
                    _, red, green, blue = pg.Color(self.image[pos])
                    if red and green and blue:
                        color = (red + green + blue) // 3
                        color = 220 if 160 < color < 220 else color
                        char = self.prerendered_chars[(char, (0, color, 0))]
                        char.set_alpha(color + 60)
                        self.app.surface.blit(char, pos)


class MatrixVision:
    def __init__(self, option, path_to_file=None):
        self.RES = self.WIDTH, self.HEIGHT = 960, 720 # Change the Resolution here 
        # self.RES = self.WIDTH, self.HEIGHT = 1920, 1080
        pg.init()
        self.screen = pg.display.set_mode(self.RES)
        pg.display.set_caption("Matrix Vision by Yashwanth Kumar")
        self.surface = pg.Surface(self.RES)
        self.clock = pg.time.Clock()
        self.matrix = Matrix(self)
        
        pygame.camera.init()
        self.cam = pygame.camera.Camera(pygame.camera.list_cameras()[0])
        self.cam.start()
        self.option = option
        if option == 2:
            self.matrix.image = self.matrix.get_image(path_to_file)

    def draw(self):
        self.surface.fill(pg.Color('black'))
        self.matrix.run()
        self.screen.blit(self.surface, (0, 0))

    def run(self):
        while True:
            self.draw()
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_ESCAPE:
                        pg.quit()
                        sys.exit()

            pg.display.flip()
            self.clock.tick(30)


def run_matrix_vision(option, path_to_file=None):
    app = MatrixVision(option, path_to_file)
    app.run()


def open_file_dialog():
    file_path = filedialog.askopenfilename()
    return file_path


def start_gui():
    def on_option_select():
        option = option_var.get()
        if option == 2:
            file_path = open_file_dialog()
            if file_path:
                root.destroy()
                run_matrix_vision(option, file_path)
        elif option == 1 or option == 3:
            root.destroy()
            run_matrix_vision(option)

    root = ctk.CTk()
    root.geometry("500x400")
    root.iconbitmap("logo.ico")
    root.title("Matrix Vision by Yashwanth Kumar")

    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("green")

    frame = ctk.CTkFrame(root)
    frame.pack(padx=20, pady=20, fill="both", expand=True)

    label = ctk.CTkLabel(frame, text="Choose an option:", font=("Arial", 24, "bold"))
    label.pack(pady=(20, 30))

    option_var = ctk.IntVar()

    options = [
        ("Matrix Fall", 1),
        ("Image to Matrix Vision", 2),
        ("Webcam to Matrix Vision", 3)
    ]

    for text, value in options:
        option = ctk.CTkRadioButton(frame, text=text, variable=option_var, value=value, font=("Arial", 14))
        option.pack(pady=10)

    button = ctk.CTkButton(frame, text="Start", command=on_option_select, font=("Arial", 16, "bold"))
    button.pack(pady=(30, 20))

    # Center the frame contents
    frame.pack_configure(anchor="center")
    for child in frame.winfo_children():
        child.pack_configure(anchor="center")

    root.mainloop()
    
    def on_option_select():
        option = option_var.get()
        if option == 2:
            file_path = open_file_dialog()
            if file_path:
                root.destroy()
                run_matrix_vision(option, file_path)
        elif option == 1 or option == 3:
            root.destroy()
            run_matrix_vision(option)

    root = ctk.CTk()
    root.geometry("500x250")
    root.iconbitmap("logo.ico")
    root.title("Matrix Vision by Yashwanth Kumar")

    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("green")

    frame = ctk.CTkFrame(root, width=800, height=600)
    frame.pack(padx=20, pady=20, fill = "both", expand =True)

    label = ctk.CTkLabel(frame, text="Choose an option:")
    label.pack(pady=10)

    option_var = ctk.IntVar()

    option1 = ctk.CTkRadioButton(frame, text="Matrix Fall", variable=option_var, value=1)
    option1.pack(anchor='w', pady=5)

    option2 = ctk.CTkRadioButton(frame, text="Image to Matrix Vision", variable=option_var, value=2)
    option2.pack(anchor='w', pady=5)

    option3 = ctk.CTkRadioButton(frame, text="Webcam to Matrix Vision", variable=option_var, value=3)
    option3.pack(anchor='w', pady=5)

    button = ctk.CTkButton(frame, text="Start", command=on_option_select)
    button.pack(pady=20)

    root.mainloop()


if __name__ == '__main__':
    start_gui()
