#!/usr/bin/python3
"""
Create a function def pascal_triangle(n): that returns a list of lists of
integers representing the Pascal’s triangle of n:

 Returns an empty list if n <= 0
 You can assume n will be always an integer

"""

def pascal_triangle(n):
    """
    Creates a list of lists of integers representing Pascal's triangle.

    Parameters:
        n (int): The number of rows of Pascal's triangle to recreate.

    Returns:
        List[List[int]]: Representation of Pascal's triangle.
    """
    if type(n) is not int:
        raise TypeError("n must be an integer")

    if n <= 0:
        return []

    triangle = [[1]]  # Start with the first row

    for row_index in range(1, n):
        row = [1]  # Every row starts with 1
        for i in range(1, row_index):
            row.append(triangle[row_index-1][i-1] + triangle[row_index-1][i])
        row.append(1)  # Every row ends with 1
        triangle.append(row)

    return triangle

