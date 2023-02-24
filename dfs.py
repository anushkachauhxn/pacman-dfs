import sys
import os
import numpy as np
from queue import LifoQueue

fringe = LifoQueue()
pacmanPath = []


def pushFringes(x, y, vis, grid):
    # possible fringes = [left, down, right, up]
    coords = [[x, y-1], [x+1, y], [x, y+1], [x-1, y]]
    for i in range(4):
        newX = coords[i][0]
        newY = coords[i][1]
        if ((newX >= 0 and newX < n) and (newY >= 0 and newY < m) and
                (vis[newX][newY] == 0) and
                (grid[newX][newY] != 0)):
            fringe.put([newX, newY])


def dfsTravel(x, y, vis, grid):
    vis[x][y] = 1
    pacmanPath.append([x, y])

    if (grid[x][y] == 2):
        global foodFound
        foodFound = True
        print("Food found at: ", x, y)
        return

    pushFringes(x, y, vis, grid)


def sortToGrid(lines):
    grid = []
    for line in lines:
        row = list(map(int, line.split()))
        grid.append(row)
    return grid


def main():
    pacman = list(map(int, input().split()))
    grid = sortToGrid(sys.stdin.readlines())

    fringe.put(pacman)

    global n, m, foodFound
    n = len(grid)  # num of rows = 8
    m = len(grid[0])  # num of columns = 7
    foodFound = False

    vis1 = np.zeros((n, m), dtype=int)
    while (not fringe.empty() and not foodFound):
        next = fringe.get()
        dfsTravel(next[0], next[1], vis1, grid)

    print(pacmanPath)


if __name__ == '__main__':
    if not os.environ.get("ONLINE_JUDGE"):
        sys.stdin = open('./input.txt', 'r')
        sys.stdout = open('./output.txt', 'w')
    main()
