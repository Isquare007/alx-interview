#!/usr/bin/python3
"""2D matrix rotator"""
from typing import List


def rotate_2d_matrix(matrix: List[list]) -> None:
    """rotates a 2d matrix"""
    m = len(matrix[0])
    for i in range(m):
        for y in range(i, m):
            matrix[i][y], matrix[y][i] = matrix[y][i], matrix[i][y]

    for i in range(m):
        matrix[i] = matrix[i][::-1]
