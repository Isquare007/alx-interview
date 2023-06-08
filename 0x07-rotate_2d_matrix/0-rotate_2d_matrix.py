#!/usr/bin/python3
"""2D matrix rotator"""
from typing import List


def rotate_2d_matrix(matrix: List[list]) -> None:
    """rotates a 2d matrix"""
    n = len(matrix[0])

    for i in range(n - 1, -1, -1):
        for j in range(0, n):
            matrix[j].append(matrix[i].pop(0))
