import time
import tkinter
from tkinter import Frame, Label

from PIL import Image
from PIL.ImageDraw import Draw
from PIL.ImageTk import PhotoImage


class Board:

    def __init__(self, size):
        self.frame = Frame()
        self.bitmap = None
        self.draw = None
        self.playing_field = None
        self.foto = None
        self.drawing_board = True

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
        self.frame.configure(width=size * self.SCALE * 1.1, height=size * self.SCALE * 1.1)
        self.frame.pack()

        self.bitmap = Image.new(mode="RGBA", size=(size * self.SCALE, size * self.SCALE))
        self.draw = Draw(self.bitmap)

        self.playing_field = Label(self.frame)
        self.playing_field.place(x=50, y=50)
        self.playing_field.configure(width=size * self.SCALE, height=size * self.SCALE, background="sea green")
        # Create rooster image
        for x in range(0, size * self.SCALE, self.SCALE):
            for y in range(0, size * self.SCALE, self.SCALE):
                self.draw.rectangle(((x, y), (x + self.SCALE, y + self.SCALE)), outline="black")

        # Place center pieces
        self.place_disk(int(size / 2 - 1), int(size / 2 - 1))
        self.place_disk(int(size / 2 - 1), int(size / 2))
        self.place_disk(int(size / 2), int(size / 2))
        self.place_disk(int(size / 2), int(size / 2 - 1))
        self.drawing_board = False

    def place_disk(self, horizontal_position, vertical_position):
        try:
            if self.grid[horizontal_position][vertical_position] == self.EMPTY:
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1], [1, 1], [1, -1], [-1, 1], [-1, -1]]
                pieces_to_flip = []
                try:
                    for direction in directions:
                        temporary_pieces_to_flip = []
                        current_position = [horizontal_position + direction[0], vertical_position + direction[1]]
                        while True:
                            if self.grid[current_position[0]][current_position[1]] == self.active_player:
                                for piece in temporary_pieces_to_flip:
                                    pieces_to_flip.append(piece)
                                break
                            elif self.grid[current_position[0]][current_position[1]] != self.EMPTY and self.grid[current_position[0]][current_position[1]] != self.active_player:
                                temporary_pieces_to_flip.append(current_position.copy())
                                current_position[0] += direction[0]
                                current_position[1] += direction[1]
                                continue
                            else:
                                break
                except IndexError:
                    print("Nope")

                if len(pieces_to_flip) > 0 or self.drawing_board:
                    self.grid[horizontal_position][vertical_position] = self.active_player
                    self.draw.ellipse(((horizontal_position * self.SCALE + 5, vertical_position * self.SCALE + 5), (horizontal_position * self.SCALE) + self.SCALE - 5, (vertical_position * self.SCALE) + self.SCALE - 5), self.active_player)
                    for piece in pieces_to_flip:
                        self.grid[piece[0]][piece[1]] = self.active_player
                        self.draw.ellipse(((piece[0] * self.SCALE + 5, piece[1] * self.SCALE + 5),(piece[0] * self.SCALE) + self.SCALE - 5,(piece[1] * self.SCALE) + self.SCALE - 5), self.active_player)
                    if self.active_player == self.BLACK:
                        self.active_player = self.WHITE
                    else:
                        self.active_player = self.BLACK
                    self.update_board()
        except IndexError:
            print("Nope!")

    def update_board(self):
        self.foto = PhotoImage(self.bitmap)
        self.playing_field.configure(image=self.foto)

    def mouse_click(self, event_arguments):
        self.place_disk(event_arguments.x//self.SCALE, event_arguments.y//self.SCALE)


board = Board(8)
board.playing_field.bind("<Button-1>", board.mouse_click)

board.frame.mainloop()
