import time
import tkinter
from tkinter import Frame, Label

from PIL import Image
from PIL.ImageDraw import Draw
from PIL.ImageTk import PhotoImage
class Board():

    def __init__(self, size):
        self.frame = Frame()
        self.bitmap = None
        self.draw = None
        self.playing_field = None
        self.BLACK = "black"
        self.WHITE = "white"
        self.EMPTY = "empty"
        self.SCALE = 100
        self.active_player = self.BLACK
        self.grid = self.create_grid(size)
        self.draw_board(size)

    def create_grid(self, size):
        # Create empty grid
        grid = []
        for column in range(0, size):
            grid.append([])
            for row in range(0, size):
                grid[column].append(self.EMPTY)
        return grid

    def draw_board(self, size):
        self.frame.master.title("Reversi 2 player game")
        self.frame.configure(width=size*self.SCALE*1.1, height=size*self.SCALE*1.1)
        self.frame.pack()
        self.bitmap = Image.new(mode="RGBA", size=(size*self.SCALE, size*self.SCALE))
        self.draw = Draw(self.bitmap)

        self.playing_field = Label(self.frame)
        self.playing_field.place(x=50, y=50)
        self.playing_field.configure(width=size*self.SCALE, height=size*self.SCALE, background="sea green")
        # Create rooster image
        for x in range(0, size*self.SCALE, self.SCALE):
            for y in range(0, size*self.SCALE, self.SCALE):
                self.draw.rectangle(((x, y), (x + self.SCALE, y + self.SCALE)), outline="black")

        self.playing_field.configure(image=PhotoImage(self.bitmap))

    def place_disk(self, horizontal_position, vertical_position):
        try:
            if self.grid[horizontal_position][vertical_position] != self.EMPTY:
                self.grid[horizontal_position][vertical_position] = self.active_player
                if self.active_player == self.BLACK:
                    self.active_player = self.WHITE
                else:
                    self.active_player = self.BLACK
        except IndexError:
            print("Nope!")


board = Board(8)
tkinter.mainloop()
