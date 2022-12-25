import tkinter
from tkinter import Frame, Label, Button
from PIL.ImageDraw import Draw
from PIL.ImageTk import PhotoImage
from PIL import Image

ALPHABET = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
            'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

class Board():
    def __init__(self, size):
        self.place_holder = None
        self.bitmap = None
        self.draw = None
        self.playing_field = None
        self.drawing_board = True
        self.grid = None
        self.x = 0
        self.y = 0
        self.size = size
        self.possible_moves = {}

        self.SCALE = 150
        if size == 6:
            self.SCALE= 100
        if size == 8:
            self.SCALE = 75
        if size == 10:
            self.SCALE = 60

        self.BLACK = "Black"
        self.WHITE = "White"
        self.EMPTY = "empty"

        self.active_player = "Black"

        self.frame = Frame()
        self.active_player_display = Label()
        self.score_tracker = Label()
        self.create_grid(size)
        self.create_board(size)

    # Create Grid/Array
    def create_grid(self, size):
        self.grid = []
        for column in range(0, size):
            self.grid.append([])
            for row in range(0, size):
                self.grid[column].append(self.EMPTY)

    # Checks how many black and white discs there are
    def score(self):
        zwart = 0
        wit = 0
        for i in range(0, len(self.grid)):
            for j in range(0, len(self.grid)):
                if self.grid[i][j] == self.BLACK:
                    zwart += 1
                elif self.grid[i][j] == self.WHITE:
                    wit += 1
                else:
                    self.draw.ellipse(((i * self.SCALE + 5, j * self.SCALE + 5)
                                       ,( i* self.SCALE + self.SCALE - 5, j * self.SCALE + self.SCALE - 5)), (46, 139, 87))

        self.score_tracker.configure(text=f"{self.BLACK}: {zwart} Discs\n {self.WHITE}: {wit} Discs")

    # Creating the board, using a Frame and Label class, also putting in the new game button and creating the starting pieces
    def create_board(self, size):
        self.drawing_board = True
        self.frame.master.title("Reversi")
        self.frame.configure(width=(size * self.SCALE *1.3), height=(size * self.SCALE *1.3))
        self.frame.pack()
        self.bitmap = Image.new(mode="RGBA", size=(size *self.SCALE, size *self.SCALE))
        self.draw = Draw(self.bitmap)

        self.playing_field = Label(self.frame)
        self.playing_field.place(x=50, y=50)
        self.playing_field.configure(width=size * self.SCALE, height=size * self.SCALE, background="sea green")

        # Create Grid Image
        for x in range(0, size *self.SCALE, self.SCALE):
            for y in range(0, size *self.SCALE, self.SCALE):
                self.draw.rectangle(((x ,y), ( x +self.SCALE, y+ self.SCALE)), outline=self.BLACK)

        # Place Center Pieces
        self.place_disc(int(size / 2 - 1), int(size / 2 - 1), self.BLACK)
        self.place_disc(int(size / 2), int(size / 2 - 1), self.WHITE)
        self.place_disc(int(size / 2), int(size / 2), self.BLACK)
        self.place_disc(int(size / 2 - 1), int(size / 2), self.WHITE)

        # Creating Player Display
        self.active_player_display = Label(self.frame, text=f"{self.active_player}'s turn.")
        self.active_player_display.place(x=(size * self.SCALE) / 2, y=size * self.SCALE + self.SCALE)

        self.score_tracker = Label(self.frame, text=f"{self.BLACK}: 2 Discs\n {self.WHITE}: 2 Discs")
        self.score_tracker.place(x=0, y=0)

        new_game_button = Button(self.frame, text="New Game", height=2, command=self.create_buttons,background="Yellow")
        new_game_button.place(x=100, y=0)

        help_button = Button(self.frame, text="Help", height=2, background="Yellow", command=self.help)
        help_button.place(x=175, y=0)

        self.update_possible_moves()
        self.update_playing_field()

        self.playing_field.bind("<Button-1>", self.mouseclick)
        self.frame.mainloop()

    # Tries to place a grey disk on every single square, but only does so if discs of the opponent can be flipped (if its a legal move)
    def help(self):
        for key in self.possible_moves.keys():
            self.place_disc(key[0], key[1], "grey")

    def update_possible_moves(self):
        ## Fills the dict possible moves with the possible move coordinates as key
        # and the pieces the move will flip as array of coordinates
        self.possible_moves.clear()
        for i in range(0, len(self.grid)):
            for j in range(0, len(self.grid)):
                pieces_to_flip = self.pieces_to_flip(i, j).copy()
                # If pieces to flip > 0 its a legal move
                if len(pieces_to_flip) > 0:
                    self.possible_moves[(i, j)] = pieces_to_flip

    def pieces_to_flip(self, h_pos, v_pos):
        # Returns pieces to be flipped with current move as a list
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1], [1, 1], [-1, -1], [1, -1], [-1, 1]]
        pieces_to_flip = []
        if self.grid[h_pos][v_pos] == self.EMPTY:
            # One Method for All Directions
            for direction in directions:
                current_position = [h_pos + direction[0], v_pos + direction[1]]
                temporary_pieces_to_flip = []
                try:
                    while True:
                        if current_position[0] < 0 or current_position[1] < 0:
                            break
                        # Als je aan het einde jezelf tegen komt, dan wordt de temp lijst van die ENE richting toegevoegd aan de echte lijst
                        if self.grid[current_position[0]][current_position[1]] == self.active_player:
                            for piece in temporary_pieces_to_flip:
                                pieces_to_flip.append(piece)
                            break
                        elif self.grid[current_position[0]][current_position[1]] != self.active_player and \
                                self.grid[current_position[0]][current_position[1]] != self.EMPTY:
                            temporary_pieces_to_flip.append(current_position.copy())
                            # Verder in huidige richting en vijand toevoegen aan temporary pieces to flip lijst
                            current_position[0] += direction[0]
                            current_position[1] += direction[1]
                            # Continue zodat de loop doorgaat in dezelfde richting als de loop een vijand vindt.
                            continue
                        else:
                            break
                # Als de functie uit ge grid breekt dan stopt ie en gaat hij door naar de volgende richting
                except IndexError:
                    continue
        return pieces_to_flip

    def place_disc(self, h_pos, v_pos, color):
        ## Places disk on board
        if color == "grey":
            self.draw.ellipse(((h_pos * self.SCALE + 5, v_pos * self.SCALE + 5),
                               (h_pos * self.SCALE + self.SCALE - 5, v_pos * self.SCALE + self.SCALE - 5)),
                              outline=color, width=5)
        else:
            self.grid[h_pos][v_pos] = color
            self.draw.ellipse(((h_pos * self.SCALE + 5, v_pos * self.SCALE + 5),
                               (h_pos * self.SCALE + self.SCALE - 5, v_pos * self.SCALE + self.SCALE - 5)),color)

    def try_placing_disc(self, h_pos, v_pos):
        print(h_pos, v_pos)
        try:
            if self.grid[h_pos][v_pos] == self.EMPTY:
                # One Method for All Directions
                pieces_to_flip = self.possible_moves.get((h_pos, v_pos))
                if len(pieces_to_flip) > 0:
                    # The coordinate of the mouse is transferred to the grid, transforming the "empty" value into a player value
                    self.place_disc(h_pos, v_pos, self.active_player)
                    # For every piece that was registered that had to be flipped, flip their value in the grid and color in the GUI
                    for piece in pieces_to_flip:
                        self.place_disc(piece[0], piece[1], self.active_player)
                    self.score()
                    if self.active_player == self.BLACK:
                        self.active_player = self.WHITE
                    else:
                        self.active_player = self.BLACK
        except TypeError:
            print("Can't place here.")
        self.update_playing_field()
        self.update_possible_moves()

    def update_playing_field(self):
        self.place_holder = PhotoImage(self.bitmap)
        self.playing_field.configure(image=self.place_holder)
        self.active_player_display.configure(text=f"{self.active_player}'s turn")

    def mouseclick(self, ea):
        # Defining the X and Y coordinate of the mouse
        self.x = ea.x // self.SCALE
        self.y = ea.y // self.SCALE
        print(self.x, self.y)
        self.try_placing_disc(self.x, self.y)

    def new_game(self, size):
        self.frame.destroy()
        self.__init__(size)

    def create_buttons(self):
        button4 = Button(self.frame, text="4x4", height=2, width=20, background="yellow",
                         command=lambda: self.new_game(4))
        button4.place(x=0, y=100)

        button6 = Button(self.frame, text="6x6", height=2, width=20, background="yellow",
                         command=lambda: self.new_game(6))
        button6.place(x=0, y=150)

        button8 = Button(self.frame, text="8x8", height=2, width=20, background="yellow",
                         command=lambda: self.new_game(8))
        button8.place(x=0, y=200)

        button10 = Button(self.frame, text="10x10", height=2, width=20, background="yellow",
                          command=lambda: self.new_game(10))
        button10.place(x=0, y=250)


board = Board(6)
