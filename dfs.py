import sys
import os
import numpy as np
from queue import LifoQueue
from gui import Board

grid = []
pacmanPath = []
foodFound = False
fringe = LifoQueue()


def pushFringes(x, y, vis):
    # possible fringes = [left, down, right, up]
    coords = [[x, y-1], [x+1, y], [x, y+1], [x-1, y]]
    for i in range(4):
        newX = coords[i][0]
        newY = coords[i][1]
        if ((newX >= 0 and newX < n) and (newY >= 0 and newY < m) and
                (vis[newX][newY] == 0) and
                (grid[newX][newY] != 0)):
            fringe.put([newX, newY])
            print("PUSH", newX, newY)


def dfsTravel(x, y, vis):
    print("POP ", x, y)
    vis[x][y] = 1
    pacmanPath.append([x, y])

    if (grid[x][y] == 2):
        global foodFound
        foodFound = True
        print("Food found at: ", x, y)
        return

    pushFringes(x, y, vis)


def sortToGrid(lines):
    for line in lines:
        row = list(map(int, line.split()))
        grid.append(row)


def main():
    pacman = list(map(int, input().split()))
    sortToGrid(sys.stdin.readlines())

    global n, m
    n = len(grid)
    m = len(grid[0])
    vis1 = np.zeros((n, m), dtype=int)

    fringe.put(pacman)
    while (not fringe.empty() and not foodFound):
        next = fringe.get()
        dfsTravel(next[0], next[1], vis1)
    if (not foodFound):
        print("Food not found")
    print(pacmanPath)

    Board(grid, pacmanPath)


if __name__ == '__main__':
    if not os.environ.get("ONLINE_JUDGE"):
        sys.stdin = open('./input.txt', 'r')
        sys.stdout = open('./output.txt', 'w')
    main()
