def print_board(board):
    for row in board:
        print(" ".join(row))
    print()


def check_e(board, row, col):
    for i in range(row):
        if board[i][col] == 'Q':
            return False

    i, j = row, col

    while i >= 0 and j >= 0:
        if board[i][j] == 'Q':
            return False
        i -= 1
        j -= 1

    i, j = row, col

    while i >= 0 and j < len(board):
        if board[i][j] == 'Q':
            return False
        i -= 1
        j += 1

    return True


def solve_queens(board, row, n):
    if row == n:
        print_board(board)
        return True

    for col in range(n):
        if check_e(board, row, col):
            board[row][col] = 'Q'

            if solve_queens(board, row + 1, n):
                return True

            board[row][col] = '.'

    return False


def queens():
    n = int(input("Enter value of N: "))
    board = []

    for i in range(n):
        row = []

        for j in range(n):
            row.append(".")

        board.append(row)

    if not solve_queens(board, 0, n):
        print("No Solution found")


queens()