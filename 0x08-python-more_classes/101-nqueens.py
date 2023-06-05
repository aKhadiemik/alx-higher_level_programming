#!/usr/bin/python3
import sys
'''
    Module solves the N queens problem
'''


def is_safe(board, row, col):
    """
    Checks if it is safe to place a queen at the given position on the board.

    Args:
        board (list): The chessboard.
        row (int): The row position to check.
        col (int): The column position to check.

    Returns:
        bool: True if it is safe to place a queen, False otherwise.
    """
    # Check the left side of the current row
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on the left side
    i = row
    j = col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # Check lower diagonal on the left side
    i = row
    j = col
    while i < len(board) and j >= 0:
        if board[i][j] == 1:
            return False
        i += 1
        j -= 1

    return True


def solve_nqueens(n):
    """
    Solves the N-queens problem and prints all possible solutions.

    Args:
        n (int): The size of the chessboard and the number of queens.
    """
    board = [[0 for _ in range(n)] for _ in range(n)]
    solutions = []
    solve_nqueens_util(board, 0, solutions)
    print_solutions(solutions)


def solve_nqueens_util(board, col, solutions):
    """
    Recursive helper function to solve the N-queens problem.

    Args:
        board (list): The chessboard.
        col (int): The current column to consider.
        solutions (list): List to store the solutions.
    """
    if col >= len(board):
        # All queens are successfully placed, add the solution
        solution = []
        for row in range(len(board)):
            for col in range(len(board)):
                if board[row][col] == 1:
                    solution.append([row, col])
        solutions.append(solution)
        return

    for row in range(len(board)):
        if is_safe(board, row, col):
            board[row][col] = 1
            solve_nqueens_util(board, col + 1, solutions)
            board[row][col] = 0


def print_solutions(solutions):
    """
    Prints all solutions of the N-queens problem.

    Args:
        solutions (list): List of solutions.
    """
    for solution in solutions:
        print(solution)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    solve_nqueens(n)
