#!/usr/bin/python3
"""2D matrix rotator"""


def rotate_2d_matrix(matrix):
    """rotates a 2d matrix"""
    m = len(matrix)
    for i in range(m):
        for y in range(i, m):
            matrix[i][y], matrix[y][i] = matrix[y][i], matrix[i][y]

    for i in range(m):
        matrix[i] = matrix[i][::-1]
