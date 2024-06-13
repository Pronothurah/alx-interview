#!/usr/bin/python3
"""2D matrix Module"""


def rotate_2d_matrix(matrix):
    """Rotates a 2D matrix 90 degrees"""
    n = len(matrix)
    # Transpose the matrix
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    # Reverse each row
    for row in matrix:
        row.reverse()
