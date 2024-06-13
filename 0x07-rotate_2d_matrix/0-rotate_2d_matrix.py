#!/usr/bin/env python3
"""2D matrix Module"""


def rotate_2d_matrix(matrix):
    """Rotates a 2D matrix 90 degrees"""
    n = len(matrix)

    for i in range(n):
        for j in range(i, n):
            matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]

    for i in range(n):
        matrix[i] = matrix[i][::-1]
