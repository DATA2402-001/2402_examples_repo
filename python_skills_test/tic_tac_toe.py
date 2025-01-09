
def check_for_win(board: list[list]) -> int:

    # check rows
    for row in board:
        if sum(row) == 3:
            return 1
        elif sum(row) == -3:
            return -1
    
    # check columns
    for column_index in range(3):
        column_sum = 0
        for row_index in range(3):
            column_sum += board[row_index][column_index]

        if column_sum == 3:
            return 1
        elif column_sum == -3:
            return -1
    
    # easy diagonal
    diagonal_sum = 0
    for index in range(3):
        diagonal_sum += board[index][index]
    if diagonal_sum == 3:
            return 1
    elif diagonal_sum == -3:
        return -1
    
    # hard diagonal
    diagonal_sum = 0
    for index in range(3):
        diagonal_sum += board[2-index][index]
    if diagonal_sum == 3:
            return 1
    elif diagonal_sum == -3:
        return -1
    
    return 0


board = [
    [1, 0, 0],
    [0, 1, 0],
    [-1,-1,1],
]

print(check_for_win(board))