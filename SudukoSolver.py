#!/usr/bin/python3
import csv
import sys
N = 9

def skrivaUt(a):
    for i in range(N):
        for j in range(N):
            print(a[i][j],end = " ")
        print()


def solve(grid, rad, kol, num):
    for x in range(9):
        if grid[rad][x] == num:
            return False

    for x in range(9):
        if grid[x][kol] == num:
            return False

    startRad = rad - rad % 3
    startKol = kol - kol % 3

    for i in range(3):
        for j in range(3):
            if grid[i + startRad][j + startKol] == num:
                return False
    return True

def Suduko(grid, rad, kol):
    if (rad == N - 1 and kol == N):
        return True
    if kol == N:
        rad += 1
        kol = 0

    if grid[rad][kol] > 0:
        return Suduko(grid, rad, kol + 1)

    for num in range(1, N + 1, 1):
        if solve(grid, rad, kol, num):
            grid[rad][kol] = num
            if Suduko(grid, rad, kol + 1):
                return True
        grid[rad][kol] = 0
    return False


grid =[]

with open(sys.argv[1]) as f:
    for line in f:
        line = line.split(",")
        for i in range(len(line)):
            line[i] = line[i].strip()
        grid.append(line)
    grid = [list(map(int,i)) for i in grid]


if (Suduko(grid, 0, 0)):
    skrivaUt(grid)
else:
   print("Solution doesn't exist")

with open('solved.csv', 'w', newline = '') as solved:
      writer = csv.writer(solved)
      for line in range(9):
         p = grid[line]
         writer.writerow(p)
