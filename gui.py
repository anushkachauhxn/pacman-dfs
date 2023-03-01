from tkinter import Tk, Canvas, Frame, BOTH
import time


class Board(Frame):
    def __init__(self, grid, pacmanPath):
        super().__init__()
        self.grid = grid
        self.pacmanPath = pacmanPath
        self.initUI()

    def initUI(self):
        n = len(self.grid)
        m = len(self.grid[0])

        self.master.title("Pacman | DFS")
        self.master.geometry(f"{50*m}x{50*n}")
        self.pack(fill=BOTH, expand=1)
        self.canvas = Canvas(self)

        create_grid(self.canvas, self.grid)  # grid maze

        progress = 0
        while (progress != len(self.pacmanPath)-1):
            pacman = create_pacman(
                self.canvas, self.pacmanPath[progress][0], self.pacmanPath[progress][1])
            self.canvas.pack(fill=BOTH, expand=1)
            self.master.update()
            time.sleep(0.5)

            for i in range(progress+1, len(self.pacmanPath)):
                x = self.pacmanPath[i][0]
                px = self.pacmanPath[i-1][0]
                y = self.pacmanPath[i][1]
                py = self.pacmanPath[i-1][1]

                if (x == px-1):
                    movePacman(self.canvas, 'up')  # x dec
                elif (x == px+1):
                    movePacman(self.canvas, 'down')  # x inc
                elif (y == py-1):
                    movePacman(self.canvas, 'left')  # y dec
                elif (y == py+1):
                    movePacman(self.canvas, 'right')  # y inc
                else:
                    self.canvas.delete(pacman)
                    break
                self.master.update()
                time.sleep(0.5)
            progress = i


def create_grid(canvas, grid):
    n = len(grid)
    m = len(grid[0])
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
    return canvas.create_rectangle(50*x, 50*y, 50*x+50, 50*y+50,
                                   tags="pacman", outline="#fff", fill="#fb0")


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


def main():
    grid = [
        [0, 0, 0, 0, 0, 0, 0],
        [0, 1, 1, 1, 1, 1, 0],
        [0, 1, 0, 0, 0, 1, 0],
        [0, 1, 0, 2, 0, 1, 0],
        [0, 1, 1, 1, 0, 1, 0],
        [0, 1, 0, 0, 0, 1, 0],
        [0, 1, 1, 1, 1, 1, 0],
        [0, 0, 0, 0, 0, 0, 0],
    ]
    pacmanPath = [[6, 1], [5, 1], [4, 1], [3, 1], [2, 1], [1, 1],
                  [1, 2], [1, 3], [1, 4], [1, 5],
                  [2, 5], [3, 5], [4, 5], [5, 5], [6, 5],
                  [6, 4], [6, 3], [6, 2],
                  [4, 2], [4, 3], [3, 3]]

    gui = Tk()
    screen = Board(grid, pacmanPath)
    gui.mainloop()


if __name__ == '__main__':
    main()
