#!/usr/bin/python3
"""Method for pascal's triangle"""


def pascal_triangle(n):
    """ returns a list of lists of integers representing
    the Pascal’s triangle of n"""
    if n < 1 or not isinstance(n, int):
        print("Input must be positive and an integer!")
        return None
    if n == 1:
        return [[1]]
    if n == 2:
        return [[1], [1, 1]]
    triangle = [[1], [1, 1]]
    for i in range(3, n + 1):
        row = [1] + [0] * (i - 2) + [1]
        prev_row = triangle[-1]
        for j in range(1, len(prev_row)):
            row[j] = prev_row[j - 1] + prev_row[j]
        triangle.append(row)
    return triangle
