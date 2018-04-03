import time
from os import system, name
from itertools import product
from config import *

def main():
    global board
    system(clear)
    while True:
        printGrid(board)
        time.sleep(timeDelay)
        system(clear)
        board = update(board)


def update(grid):
    newGrid = [[0 for a in range(50)] for b in range(50)]
    for i, item in enumerate(grid):
        for j in range(len(item)):
            if isAlive(i, j):
                if amountAlive(i, j) < 2:
                    newGrid[i][j] = 0
                elif amountAlive(i, j) > 3:
                    newGrid[i][j] = 0
                elif amountAlive(i, j) in [2, 3]:
                    newGrid[i][j] = 1
            else:
                if amountAlive(i, j) == 3:
                    newGrid[i][j] = 1
                else:
                    newGrid[i][j] = 0
    return newGrid

def amountAlive(xPos, yPos):
    global board
    alive = 0
    for i in list(neighbours(xPos, yPos)):
        x, y = i
        if isAlive(x, y):
            alive += 1
    return alive

def neighbours(x, y):
    grid = (x, y)
    for c in product(*(range(n-1, n+2) for n in grid)):
        if c != grid and all(0 <= n < 50 for n in c):
            yield c

def printGrid(grid):
    print "_"*101
    for i in grid:
        print "{0}{1}{0}".format("|", " ".join([str(x) for x in i])).replace("0", deadBlock).replace("1", aliveBlock)
    print "{0}{1}{0}".format("|", "_"*99)

isAlive = lambda x, y: bool(board[x][y])
if __name__ == "__main__":
    clear = "clear" if name == "posix" else "cls"
    main()