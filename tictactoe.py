
def utility(board):

    for row in board:
        if row == ["X", "X", "X"]:

            return 1
        elif row == ["O", "O", "O"]:

            return -1


    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i] == "X":
            return 1
        elif board[0][i] == board[1][i] == board[2][i] == "O":
            return -1


    if board[0][0] == board[1][1] == board[2][2] == "X" or board[0][2] == board[1][1] == board[2][0] == "X":
        return 1
    elif board[0][0] == board[1][1] == board[2][2] == "O" or board[0][2] == board[1][1] == board[2][0] == "O":
        return -1


    if all(board[i][j] != "" for i in range(3) for j in range(3)):
        return 0


    return None



def max_value(board):
    result = utility(board)
    if result is not None:
        return result

    v = float("-inf")
    for i in range(3):
        for j in range(3):
            if board[i][j] == "":
                board[i][j] = "X"
                v = max(v, min_value(board))
                board[i][j] = ""

    return v


def min_value(board):
    result = utility(board)
    if result is not None:
        return result

    v = float("inf")
    for i in range(3):
        for j in range(3):
            if board[i][j] == "":
                board[i][j] = "O"
                v = min(v, max_value(board))
                board[i][j] = ""

    return v



def minimax(board):
    best_value = float("-inf")
    best_move = None
    for i in range(3):
        for j in range(3):
            if board[i][j] == "":
                board[i][j] = "X"
                move_value = min_value(board)
                board[i][j] = ""
                if move_value > best_value:
                    best_value = move_value
                    best_move = (i, j)

    return best_move


board = [["", "", ""],
         ["", "", ""],
         ["", "", ""]]
while utility(board) is None:
    i, j = minimax(board)
    board[i][j] = "X"  

    print(board)
    if utility(board) is not None:
        break
    i, j = map(int, input("Enter your move: 0 for row and 1 for column): ").split())
    board[i][j] = "O"
    print(board)
