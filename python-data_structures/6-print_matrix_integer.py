#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        line = ""
        for integer in row:
            line += "{:d}".format(integer)
            if integer != row[-1]:
                line += " "
        print(line)
