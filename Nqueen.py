def print_solution(board, N):
    for i in range(N):
        for j in range(N):
            print(board[i][j], end=' ')
        print()

def is_safe(board, row, col, N):
    # Check this row on left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on left side
    for i, j in zip(range(row, N, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

def solve_nq_util(board, col, N):
    if col >= N:
        return True

    for i in range(N):
        if is_safe(board, i, col, N):
            board[i][col] = 1
            if solve_nq_util(board, col + 1, N):
                return True
            board[i][col] = 0  # backtrack

    return False

def solve_nq(N):
    board = [[0 for _ in range(N)] for _ in range(N)]

    if not solve_nq_util(board, 0, N):
        print("Solution does not exist")
        return False

    print_solution(board, N)
    return True

def main():
    N = int(input("Enter the number of queens: "))  # Get the number of queens from the user
    solve_nq(N)

if __name__ == "__main__":
    main()
