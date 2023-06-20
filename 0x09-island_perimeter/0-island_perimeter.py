#!/usr/bin/python3
"""island_perimeter module"""


def island_perimeter(grid):
    """grid is a list of list of integers:
        0 represents water
        1 represents land
        Each cell is square, with a side length of 1
        Cells are connected horizontally/vertically (not diagonally)."""
    row = len(grid)
    col = len(grid[0])

    p = 0
    connect = 0

    for r in range(0, row):
        for c in range(0, col):
            if grid[r][c] == 1:
                p += 4

                if r != 0 and grid[r-1][c] == 1:
                    connect += 1
                if c != 0 and grid[r][c-1] == 1:
                    connect += 1

    connect = connect * 2

    return p - connect


if __name__ == "__main__":
    grid = [
        [0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0]
    ]
    print(island_perimeter(grid))
