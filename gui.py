from tkinter import Tk, Canvas, Frame, BOTH
import time


grid = [
    [0, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 1, 1, 0],
    [0, 1, 0, 0, 0, 1, 0],
    [0, 1, 0, 2, 0, 1, 0],
    [0, 2, 0, 1, 0, 1, 0],
    [0, 1, 0, 0, 0, 1, 0],
    [0, 1, 1, 1, 1, 1, 0],
    [0, 0, 0, 0, 0, 0, 0],
]
n = len(grid)  # n=8
m = len(grid[0])  # n=7
pacmanPath = [[6, 1], [5, 1], [4, 1]]


class Board(Frame):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.master.title("Pacman | DFS")
        self.master.geometry(f"{50*m}x{50*n}")
        self.pack(fill=BOTH, expand=1)
        canvas = Canvas(self)

        create_grid(canvas, n, m)  # grid maze
        create_pacman(canvas, 6, 1)  # pacman image
        canvas.pack(fill=BOTH, expand=1)

        for i in range(1, len(pacmanPath)):
            x = pacmanPath[i][0]
            px = pacmanPath[i-1][0]
            y = pacmanPath[i][1]
            py = pacmanPath[i-1][1]

            if (x < px):
                movePacman(canvas, 'up')  # x dec
            elif (x > px):
                movePacman(canvas, 'down')  # x inc
            if (y < py):
                movePacman(canvas, 'left')  # y dec
            elif (y > py):
                movePacman(canvas, 'right')  # y inc
            self.master.update()
            time.sleep(0.5)


def create_grid(canvas, n, m):
    # create a grid with n rows and m columns
    for i in range(0, n):
        for j in range(0, m):
            if (grid[i][j] == 1):
                color = "#0000FF"
            elif (grid[i][j] == 2):
                color = "#f50"
            else:
                color = "#333"
            canvas.create_rectangle(
                50*j, 50*i, 50*j+50, 50*i+50, outline="#fff", fill=color)


def create_pacman(canvas, y, x):
    # create pacman at position (x, y)
    canvas.create_rectangle(50*x, 50*y,
                            50*x+50, 50*y+50, tags="pacman", outline="#fff", fill="#fb0")
    # pacman = Image.open("./pacman.png"); pacman = pacman.resize((47, 47), Image.ANTIALIAS); img = ImageTk.PhotoImage(pacman); label = tkinter.Label(image=img); label.image = img; label.place(x=pacmanPath[0][0], y=pacmanPath[0][1])


def movePacman(canvas, direction):
    # move pacman in given direction
    if (direction == 'up'):
        canvas.move('pacman', 0, -50)
    elif (direction == 'down'):
        canvas.move('pacman', 0, 50)
    elif (direction == 'left'):
        canvas.move('pacman', -50, 0)
    elif (direction == 'right'):
        canvas.move('pacman', 50, 0)


def move_pacman(window, canvas, pacman):
    for i in range(0, len(pacmanPath)):
        newX = pacmanPath[i][0]
        newY = pacmanPath[i][1]
        canvas.move(pacman, 50*newX, 50*newY)
        print(newX, newY)
        window.update()
        time.sleep(1)


def main():
    gui = Tk()
    screen = Board()
    gui.mainloop()


if __name__ == '__main__':
    main()
