#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    return list(map(lambda matrix_elements: list(map(lambda x:x**2,matrix_elements)), matrix))

