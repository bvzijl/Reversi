from tkinter import Frame, Label

from PIL import Image
from PIL.ImageDraw import Draw
from PIL.ImageTk import PhotoImage

scherm = Frame()
scherm.master.title("Reversi 2 player game")
scherm.configure(width=650, height=700)
scherm.pack()
Bitmap = Image.new(mode="RGBA", size=(600, 600))
draw = Draw(Bitmap)

Board = Label(scherm)
Board.place(x=50, y=50)
Board.configure(width=600, height=600)
Board.configure(background="sea green")

# tekenen van labels voor 1-6 & a-f
labA = Label(scherm, text="A");
labA.place(x=100, y=25)
labB = Label(scherm, text="B");
labB.place(x=200, y=25)
labC = Label(scherm, text="C");
labC.place(x=300, y=25)
labD = Label(scherm, text="D");
labD.place(x=400, y=25)
labE = Label(scherm, text="E");
labE.place(x=500, y=25)
labF = Label(scherm, text="F");
labF.place(x=600, y=25)

lab1 = Label(scherm, text="0");
lab1.place(x=25, y=100)
lab2 = Label(scherm, text="1");
lab2.place(x=25, y=200)
lab3 = Label(scherm, text="2");
lab3.place(x=25, y=300)
lab4 = Label(scherm, text="3");
lab4.place(x=25, y=400)
lab5 = Label(scherm, text="4");
lab5.place(x=25, y=500)
lab6 = Label(scherm, text="5");
lab6.place(x=25, y=600)

player_counter = Label(scherm, text="Black has to lay");
player_counter.place(x=300, y=660)
score_tracker = Label(scherm, text="Black: 2 discs\nWhite: 2 discs");
score_tracker.place(x=0, y=0)
HEIGHT = 6
WIDTH = 6

def score():
    global grid
    zwart = 0
    wit = 0
    # Checks how many black and white discs there are
    for x in grid:
        for n in x:
            if n == -1:
                zwart += 1
            elif n == 2:
                wit += 1
    score_tracker.configure(text=f"Black: {zwart} discs\nWhite: {wit} discs")
    zwart = 0
    wit = 0


def links():
    global Y
    global X
    global n
    check = []
    flag = True
    x = 1
    coord = grid[Y][X]
    try:
        print("Begin Links")
        if (X - x) > 0:
            while flag:
                if grid[Y][X - x] != coord and grid[Y][X - x] != 0:
                    print("Vijand!")
                    x += 1
                    check.append("Vijand")
                elif grid[Y][X - x] == coord:
                    print("Vriend!\nEinde Links\n")
                    flag = False
                    check.append("Vriend")
                elif grid[Y][X - x] == 0:
                    print("Niemands-Land!\nEinde Links\n")
                    flag = False
                    check.append("Niemands-Land")
            x = 1
            # flipping enemy discs if flanking on left is true
            if len(check) > 1 and check[-1] == "Vriend":
                insluiting = True
                while insluiting:
                    if n == -1:
                        if len(check) > 1 and check[-1] == "Vriend":
                            if grid[Y][X - x] != coord and grid[Y][X - x] != 0:
                                grid[Y][X - x] = coord
                                draw.ellipse((((X - x) * 100 + 5, Y * 100 + 5), ((X - x) * 100 + 95), (Y * 100 + 95)),
                                             "black")
                                x += 1
                            elif grid[Y][X - x] == coord:
                                insluiting = False
                    elif n == 2:
                        if len(check) > 1 and check[-1] == "Vriend":
                            if grid[Y][X - x] != coord and grid[Y][X - x] != 0:
                                grid[Y][X - x] = coord
                                draw.ellipse((((X - x) * 100 + 5, Y * 100 + 5), ((X - x) * 100 + 95), (Y * 100 + 95)),
                                             "white")
                                x += 1
                            elif grid[Y][X - x] == coord:
                                insluiting = False
    except IndexError:
        print("Geen Linkerzijde\n")


def rechts():
    global Y
    global X
    global n
    check = []
    coord = grid[Y][X]
    flag = True
    x = 1
    # Grid is made with range function, so farthest grid Coordinate is (WIDTH -1, HEIGHT -1)
    try:
        print("Begin Rechts")
        while flag:
            if grid[Y][X + x] != coord and grid[Y][X + x] != 0:
                print("Vijand!")
                x += 1
                check.append("Vijand")
            elif grid[Y][X + x] == coord:
                print("Vriend!\nEinde Rechts\n")
                flag = False
                check.append("Vriend")
            elif grid[Y][X + x] == 0:
                print("Niemands-Land!\nEinde Rechts\n")
                flag = False
                check.append("Niemands-Land")
        x = 1
        # Flipping all disks if flanking enemy discs on right is true
        if len(check) > 1 and check[-1] == "Vriend":
            insluiting = True
            while insluiting:
                if n == -1:
                    if len(check) > 1 and check[-1] == "Vriend":
                        if grid[Y][X + x] != coord and grid[Y][X + x] != 0:
                            grid[Y][X + x] = coord
                            draw.ellipse((((X + x) * 100 + 5, Y * 100 + 5), ((X + x) * 100 + 95), (Y * 100 + 95)),
                                         "black")
                            x += 1
                        elif grid[Y][X + x] == coord:
                            insluiting = False
                elif n == 2:
                    if len(check) > 1 and check[-1] == "Vriend":
                        if grid[Y][X + x] != coord and grid[Y][X + x] != 0:
                            grid[Y][X + x] = coord
                            draw.ellipse((((X + x) * 100 + 5, Y * 100 + 5), ((X + x) * 100 + 95), (Y * 100 + 95)),
                                         "white")
                            x += 1
                        elif grid[Y][X + x] == coord:
                            insluiting = False
                            x = 1
        x = 1
    except IndexError:
        print("Rechter Flip Niet Mogelijk")


def boven():
    global Y
    global X
    global n
    coord = grid[Y][X]
    check = []
    x = 1
    flag = True
    try:
        print("Begin Boven")
        if (Y - x) > 0:
            while flag:
                if grid[Y - x][X] != coord and grid[Y - x][X] != 0:
                    print("Vijand!")
                    x += 1
                    check.append("Vijand")
                elif grid[Y - x][X] == coord:
                    print("Vriend!\nEinde Boven\n")
                    flag = False
                    check.append("Vriend")
                elif grid[Y - x][X] == 0:
                    print("Niemands-Land!\nEinde Boven\n")
                    flag = False
                    check.append("Niemands-Land")
            x = 1
            # Flipping all disks if flanking enemy discs on right is true
            if len(check) > 1 and check[-1] == "Vriend":
                insluiting = True
                while insluiting:
                    if n == -1:
                        if len(check) > 1 and check[-1] == "Vriend":
                            if grid[Y - x][X] != coord and grid[Y - x][X] != 0:
                                grid[Y - x][X] = coord
                                draw.ellipse(((X * 100 + 5, (Y - x) * 100 + 5), (X * 100 + 95, (Y - x) * 100 + 95)),
                                             "black")
                                x += 1
                            elif grid[Y - x][X] == coord:
                                insluiting = False
                    elif n == 2:
                        if len(check) > 1 and check[-1] == "Vriend":
                            if grid[Y - x][X] != coord and grid[Y - x][X] != 0:
                                grid[Y - x][X] = coord
                                draw.ellipse(((X * 100 + 5, (Y - x) * 100 + 5), (X * 100 + 95, (Y - x) * 100 + 95)),
                                             "white")
                                x += 1
                            elif grid[Y - x][X] == coord:
                                insluiting = False
                                x = 1
    except IndexError:
        print("Geen Bovenkant\n")


def beneden():
    global n
    global Y
    global X
    coord = grid[Y][X]
    check = []
    flag = True
    x = 1
    try:
        print("Begin Beneden")
        while flag:
            if grid[Y + x][X] != coord and grid[Y + x][X] != 0:
                print("Vijand!")
                x += 1
                check.append("Vijand")
            elif grid[Y + x][X] == coord:
                print("Vriend!\nEinde Beneden\n")
                flag = False
                check.append("Vriend")
            elif grid[Y + x][X] == 0:
                print("Niemands-Land!\nEinde Beneden\n")
                flag = False
                check.append("Niemands-Land")
        x = 1
        # Flipping all disks if flanking enemy discs on right is true
        if len(check) > 1 and check[-1] == "Vriend":
            insluiting = True
            while insluiting:
                if n == -1:
                    if len(check) > 1 and check[-1] == "Vriend":
                        if grid[Y + x][X] != coord and grid[Y + x][X] != 0:
                            grid[Y + x][X] = coord
                            draw.ellipse(((X * 100 + 5, (Y + x) * 100 + 5), (X * 100 + 95, (Y + x) * 100 + 95)),
                                         "black")
                            x += 1
                        elif grid[Y + x][X] == coord:
                            insluiting = False
                elif n == 2:
                    if len(check) > 1 and check[-1] == "Vriend":
                        if grid[Y + x][X] != coord and grid[Y + x][X] != 0:
                            grid[Y + x][X] = coord
                            draw.ellipse(((X * 100 + 5, (Y + x) * 100 + 5), (X * 100 + 95, (Y + x) * 100 + 95)),
                                         "white")
                            x += 1
                        elif grid[Y + x][X] == coord:
                            insluiting = False
                            x = 1
    except IndexError:
        print("Flip via onder niet mogelijk\n")


def check_links_boven():
    global n
    global Y
    global X
    coord = grid[Y][X]
    check = []
    flag = True
    x = 1
    try:
        if (Y - x) >= 0 and (X - x) >= 0:
            print("Check Links Boven")
            while flag:
                if grid[Y - x][X - x] != coord and grid[Y - x][X - x] != 0:
                    print("Vijand!")
                    check.append("Vijand")
                    x += 1
                elif grid[Y - x][X - x] == coord:
                    print("Vriend!\nEinde Links Boven\n")
                    check.append("Vriend")
                    flag = False
                elif grid[Y - x][X - x] == 0:
                    print("Niemands-Land!\nEinde Links Boven\n")
                    check.append("Niemands-Land")
                    flag = False
            x = 1
            if len(check) > 1 and check[-1] == "Vriend":
                insluiting = True
                while insluiting:
                    if n == -1:
                        if len(check) > 1 and check[-1] == "Vriend":
                            if grid[Y - x][X - x] != coord and grid[Y - x][X - x] != 0:
                                grid[Y - x][X - x] = coord
                                draw.ellipse(
                                    (((X - x) * 100 + 5, (Y - x) * 100 + 5), ((X - x) * 100 + 95, (Y - x) * 100 + 95)),
                                    "black")
                                x += 1
                            elif grid[Y - x][X - x] == coord:
                                insluiting = False
                    elif n == 2:
                        if len(check) > 1 and check[-1] == "Vriend":
                            if grid[Y - x][X - x] != coord and grid[Y - x][X - x] != 0:
                                grid[Y - x][X - x] = coord
                                draw.ellipse(
                                    (((X - x) * 100 + 5, (Y - x) * 100 + 5), ((X - x) * 100 + 95, (Y - x) * 100 + 95)),
                                    "white")
                                x += 1
                            elif grid[Y - x][X - x] == coord:
                                insluiting = False
                                x = 1
    except  IndexError:
        print("Geen Links Boven")


def check_rechts_boven():
    global n
    global Y
    global X
    coord = grid[Y][X]
    check = []
    flag = True
    x = 1
    try:
        print("Check Rechts Boven")
        while flag:
            if grid[Y - x][X + x] != coord and grid[Y - x][X + x] != 0:
                print("Vijand!")
                check.append("Vijand")
                x += 1
            elif grid[Y - x][X + x] == coord:
                print("Vriend!\nEinde Rechts Boven\n")
                check.append("Vriend")
                flag = False
            elif grid[Y - x][X + x] == 0:
                print("Niemands-Land!\nEinde Rechts Boven\n")
                check.append("Niemands-Land")
                flag = False
        x = 1
        if len(check) > 1 and check[-1] == "Vriend":
            insluiting = True
            while insluiting:
                if n == -1:
                    if len(check) > 1 and check[-1] == "Vriend":
                        if grid[Y - x][X + x] != coord and grid[Y - x][X + x] != 0:
                            grid[Y - x][X + x] = coord
                            draw.ellipse(
                                (((X + x) * 100 + 5, (Y - x) * 100 + 5), ((X + x) * 100 + 95, (Y - x) * 100 + 95)),
                                "black")
                            x += 1
                        elif grid[Y - x][X + x] == coord:
                            insluiting = False
                elif n == 2:
                    if len(check) > 1 and check[-1] == "Vriend":
                        if grid[Y - x][X + x] != coord and grid[Y - x][X + x] != 0:
                            grid[Y - x][X + x] = coord
                            draw.ellipse(
                                (((X + x) * 100 + 5, (Y - x) * 100 + 5), ((X + x) * 100 + 95, (Y - x) * 100 + 95)),
                                "white")
                            x += 1
                        elif grid[Y - x][X + x] == coord:
                            insluiting = False
                            x = 1
    except IndexError:
        print("Geen Rechts Boven")


def check_rechts_onder():
    global n
    global Y
    global X
    coord = grid[Y][X]
    check = []
    flag = True
    x = 1
    try:
        print("Check Rechts Onder")
        while flag:
            if grid[Y + x][X + x] != coord and grid[Y + x][X + x] != 0:
                print("Vijand!")
                check.append("Vijand")
                x += 1
            elif grid[Y + x][X + x] == coord:
                print("Vriend!\nEinde Rechts Onder\n")
                check.append("Vriend")
                flag = False
            elif grid[Y + x][X + x] == 0:
                print("Niemands-Land!\nEinde Rechts Onder\n")
                check.append("Niemands-Land")
                flag = False
        x = 1
        if len(check) > 1 and check[-1] == "Vriend":
            insluiting = True
            while insluiting:
                if n == -1:
                    if len(check) > 1 and check[-1] == "Vriend":
                        if grid[Y + x][X + x] != coord and grid[Y + x][X + x] != 0:
                            grid[Y + x][X + x] = coord
                            draw.ellipse(
                                (((X + x) * 100 + 5, (Y + x) * 100 + 5), ((X + x) * 100 + 95, (Y + x) * 100 + 95)),
                                "black")
                            x += 1
                        elif grid[Y + x][X + x] == coord:
                            insluiting = False
                elif n == 2:
                    if len(check) > 1 and check[-1] == "Vriend":
                        if grid[Y + x][X + x] != coord and grid[Y + x][X + x] != 0:
                            grid[Y + x][X + x] = coord
                            draw.ellipse(
                                (((X + x) * 100 + 5, (Y + x) * 100 + 5), ((X + x) * 100 + 95, (Y + x) * 100 + 95)),
                                "white")
                            x += 1
                        elif grid[Y + x][X + x] == coord:
                            insluiting = False
                            x = 1
    except IndexError:
        print("Geen Rechts Onder")


def check_links_onder():
    global n
    global Y
    global X
    coord = grid[Y][X]
    check = []
    flag = True
    x = 1
    try:
        print("Check Links Onder")
        while flag:
            if grid[Y + x][X - x] != coord and grid[Y + x][X - x] != 0:
                print("Vijand!")
                check.append("Vijand")
                x += 1
            elif grid[Y + x][X - x] == coord:
                print("Vriend!\nEinde Links Onder\n")
                check.append("Vriend")
                flag = False
            elif grid[Y + x][X - x] == 0:
                print("Niemands-Land!\nEinde Links Onder\n")
                check.append("Niemands-Land")
                flag = False
        x = 1
        if len(check) > 1 and check[-1] == "Vriend":
            insluiting = True
            while insluiting:
                if n == -1:
                    if len(check) > 1 and check[-1] == "Vriend":
                        if grid[Y + x][X - x] != coord and grid[Y + x][X - x] != 0:
                            grid[Y + x][X - x] = coord
                            draw.ellipse(
                                (((X - x) * 100 + 5, (Y + x) * 100 + 5), ((X - x) * 100 + 95, (Y + x) * 100 + 95)),
                                "black")
                            x += 1
                        elif grid[Y + x][X - x] == coord:
                            insluiting = False
                elif n == 2:
                    if len(check) > 1 and check[-1] == "Vriend":
                        if grid[Y + x][X - x] != coord and grid[Y + x][X - x] != 0:
                            grid[Y + x][X - x] = coord
                            draw.ellipse(
                                (((X - x) * 100 + 5, (Y + x) * 100 + 5), ((X - x) * 100 + 95, (Y + x) * 100 + 95)),
                                "white")
                            x += 1
                        elif grid[Y + x][X - x] == coord:
                            insluiting = False
                            x = 1
    except IndexError:
        print("Geen Links Onder")


# tekenen van rectangles met step=100
def Rooster():
    for x in range(0, 600, 100):
        for y in range(0, 600, 100):
            draw.rectangle(((x, y), (x + 100, y + 100)), outline="black")


Rooster()

grid = []
for row in range(HEIGHT):
    # Add an empty array that will hold each cell
    # in this row
    grid.append([])
    for column in range(WIDTH):
        grid[row].append(0)  # Append a cell


def StartPosition():
    grid[2][2] = -1
    grid[2][3] = 2
    grid[3][2] = 2
    grid[3][3] = -1

    draw.ellipse(((205, 205), 295, 295), "black")
    draw.ellipse(((305, 305), 395, 395), "black")
    draw.ellipse(((305, 205), 395, 295), "white")
    draw.ellipse(((205, 305), 295, 395), "white")


StartPosition()

Y = 0
X = 0
n = 2


def MouseClick(ea):
    global Y
    global X
    global n
    x_ellips = (ea.x // 100) * 100
    y_ellips = (ea.y // 100) * 100

    column = ea.x // (100)
    row = ea.y // (100)
    Y = row
    X = column
    # Set that location to one
    print(f"Click {ea.x},{ea.y}", "Grid coordinates: ", column, row)
    if grid[row][column] > 0 or grid[row][column] < 0:
        print("There's already a disc here")
    else:
        n = 1 - n
        grid[row][column] = n
        if grid[row][column] == 2:
            draw.ellipse(((x_ellips + 5, y_ellips + 5), x_ellips + 95, y_ellips + 95), "white")
            grid[row][column] = 2
            player_counter.configure(text="Black Has to Lay")

            print(f"{grid[0]}\n{grid[1]}\n{grid[2]}\n{grid[3]}\n{grid[4]}\n{grid[5]}\n")
            print(f"n: {n}")
            links()
            rechts()
            boven()
            beneden()
            check_links_boven()
            check_links_onder()
            check_rechts_boven()
            check_rechts_onder()
            score()
        if grid[row][column] == -1:
            draw.ellipse(((x_ellips + 5, y_ellips + 5), x_ellips + 95, y_ellips + 95), "black")
            grid[row][column] = -1
            player_counter.configure(text="White Has to Lay")
            print(f"{grid[0]}\n{grid[1]}\n{grid[2]}\n{grid[3]}\n{grid[4]}\n{grid[5]}\n")
            print(f"n: {n}")
            links()
            rechts()
            boven()
            beneden()
            check_links_boven()
            check_links_onder()
            check_rechts_boven()
            check_rechts_onder()
            score()

    global foto
    foto = PhotoImage(Bitmap)
    Board.configure(image=foto)


omgezetPlaatje = PhotoImage(Bitmap)
Board.configure(image=omgezetPlaatje)
Board.bind("<Button-1>", MouseClick)

scherm.mainloop()
