#!/usr/bin/python3
"""
An n x n 2D matrix, rotate it 90 degrees clockwise.
"""

def rotate_2d_matrix(matrix):
    """rotate two dimension matrix 90 degrees clockwise
    Args:
        matrix (list[[list]]): a matrix
    """
    n = len(matrix)
    for i in range(int(n // 2)):
        y = (n - i - 1)
        for j in range(i, n -i - 1):
            tmp = matrix[i][j]
            # change top for left
            matrix[i][j] = matrix[n - j - 1][i]
            # change left for bottom
            matrix[n - j - 1][i]= matrix[n - i -1][n - j - 1]
            # change bottom for right
            matrix[n - i -1][n - j - 1] = matrix[j][n - i -1]
            # change right for top
            matrix[j][n - i -1] = tmp
