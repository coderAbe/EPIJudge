from typing import List

from test_framework import generic_test

def getTopEdge(square_matrix):
    return square_matrix[0][0:-1]

def getBottomEdge(square_matrix):
    return square_matrix[-1][1:-1][::-1]

def getLeftEdge(square_matrix):
    left = []
    for i in range( 1, len(square_matrix)):
        left.append(square_matrix[i][0])
    return left[::-1]

def getRightEdge(square_matrix):
    right = []
    for i in range(len(square_matrix)):
        right.append(square_matrix[i][-1])
    return right

def getRemainingMatrix(square_matrix):
    new_matrix = []
    for i in range(1, len(square_matrix)-1):
        new_matrix.append(square_matrix[i][1:-1])
    return new_matrix
        
def matrix_in_spiral_order(square_matrix: List[List[int]]) -> List[int]:
    if len(square_matrix) == 0:
        return [] 

    if len(square_matrix) == 1:
        return square_matrix[0]

    if len(square_matrix) == 2:
        return square_matrix[0] + square_matrix[1][::-1]

    top = getTopEdge(square_matrix)
    right = getRightEdge(square_matrix)
    bottom = getBottomEdge(square_matrix)
    left = getLeftEdge(square_matrix)

    remaining_matrix = getRemainingMatrix(square_matrix)

    return top + right + bottom + left + matrix_in_spiral_order(remaining_matrix)

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('spiral_ordering.py',
                                       'spiral_ordering.tsv',
                                       matrix_in_spiral_order))
