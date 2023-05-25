#!/usr/bin/python3
"""N queens Algorithm (interview question)"""
import sys


def print_solutions():
    """gets n for cli and prints the solution nicely"""

    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    solutions = solve_queen(n)
    for solution in solutions:
        queen_pos = []
        for i, row in enumerate(solution):
            for j, char in enumerate(row):
                if char == "Q":
                    queen_pos.append([i, j])
        print(queen_pos)


def solve_queen(n):
    """ creates a set for column, updiagonal and downdiagonal of the board,
    the backtracking make use of them. they contain all the
    diagonal, left and right movement of a position
    Also populates the board with "."

    Args:
        n (int): number of queens, row and columms

    Returns:
        list: list of possible solutions
    """
    col = set()
    upDiag = set()  # positive diagonal
    downDiag = set()  # negative diagonal

    result = []
    board = [["."] * n for i in range(n)]

    def backtrack(r):
        """backtracking algorithm that checks for the column, updiagonal
        and downdiagonal, places the queen there if pos doesn't have
        a queen that can attack it, else it changes the position of the queen

        Args:
            r (int): the starting row (0)
        """
        if r == n:
            copy = ["".join(row) for row in board]
            result.append(copy)
            return
        for c in range(n):
            if c in col or (r + c) in upDiag or (r - c) in downDiag:
                continue
            col.add(c)
            upDiag.add(r + c)
            downDiag.add(r - c)
            board[r][c] = "Q"

            backtrack(r + 1)

            col.remove(c)
            upDiag.remove(r + c)
            downDiag.remove(r - c)
            board[r][c] = "."

    backtrack(0)
    return result


if __name__ == '__main__':
    print_solutions()
