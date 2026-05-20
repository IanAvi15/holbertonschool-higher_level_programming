#!/usr/bin/python3
"""Module for matrix division operations.

This module provides a function to divide all elements of a matrix by a divisor.
"""


def matrix_divided(matrix, div):
    """Divides all elements of a matrix by a number.

    Args:
        matrix: A list of lists of integers or floats
        div: A number (integer or float) to divide by

    Returns:
        A new matrix with all elements divided by div, rounded to 2 decimal places

    Raises:
        TypeError: If matrix is not a list of lists of integers/floats,
                   if rows have different sizes, or if div is not a number
        ZeroDivisionError: If div is equal to 0
    """
    if not isinstance(matrix, list) or not matrix:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    
    if not isinstance(matrix[0], list):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    
    for row in matrix:
        if not isinstance(row, list):
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        for element in row:
            if not isinstance(element, (int, float)) or isinstance(element, bool):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    
    row_size = len(matrix[0])
    for row in matrix:
        if len(row) != row_size:
            raise TypeError("Each row of the matrix must have the same size")
    
    if not isinstance(div, (int, float)) or isinstance(div, bool):
        raise TypeError("div must be a number")
    
    if div == 0:
        raise ZeroDivisionError("division by zero")
    
    new_matrix = []
    for row in matrix:
        new_row = [round(element / div, 2) for element in row]
        new_matrix.append(new_row)
    
    return new_matrix
