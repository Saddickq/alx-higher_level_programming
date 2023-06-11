#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        x = 0
        for num in row:
            x += 1
            print("{:d}".format(num), end="")
            if (x < len(row)):
                print(" ", end="")
        print()
