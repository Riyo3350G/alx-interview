#!/usr/bin/python3
""""N-queens problem Module"""
import sys


def is_safe(board, row, col, n):
    """Check if a queen can be placed on board[row][col]"""
    for i in range(col):
        if board[row][i] == 1:
            return False
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    for i, j in zip(range(row, n, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    return True


def solverNQ(board, col, n):
    """Use backtracking to solve N-queens problem"""
    if col == n:
        printIt(board)
        return True
    result = False
    for i in range(n):
        if is_safe(board, i, col, n):
            board[i][col] = 1
            result = solverNQ(board, col + 1, n) or result
            board[i][col] = 0
    return result


def printIt(board):
    """Print the result board"""
    result = []
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 1:
                result.append([i, j])
    print(result)


def nqueens(n):
    """Solve the N-queens problem"""
    board = [[0 for i in range(n)] for j in range(n)]
    if not solverNQ(board, 0, n):
        sys.exit(1)
    return


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if not sys.argv[1].isdigit():
        print("N must be a number")
        sys.exit(1)
    n = int(sys.argv[1])
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)
    nqueens(n)
