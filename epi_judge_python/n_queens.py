from typing import List

from test_framework import generic_test

def is_valid_pos(row, col, board, n):
    # validate row
    for curr_col in range(len(board)):
        if board[row][curr_col]:
            return False
    # validate col
    for curr_row in range(len(board)):
        if board[curr_row][col]:
            return False

    for k in range(n):
        for l in range(n):
            if (k+l) == (row+col) or (k-l) == (row-col):
                if board[k][l] == 1:
                    return False
    # validate diagonals
    return True

        

def flat_board(board):
    print('resul board', board)
    flatted_board = []
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 1:
                flatted_board.append(j)
    return flatted_board


def n_queens(n: int) -> List[List[int]]:
    results = []

    def get_queen_pos(row, board):
        if row == n:
            results.append(flat_board(board))
        else:
            for i in range(0, n):
                if is_valid_pos(row, i, board, n):
                    print('valid')
                    board[row][i] = 1
                    get_queen_pos(row + 1, board)

    board = [[0 for x in range(n)] for y in range(n)] 

    get_queen_pos(0, board)

    return results


def comp(a, b):
    return sorted(a) == sorted(b)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('n_queens.py', 'n_queens.tsv', n_queens,
                                       comp))
