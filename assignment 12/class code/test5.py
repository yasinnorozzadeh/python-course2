def show_board(board):
    for i in range(3):
        for j in range(3):
            print(board[i][j], end=" ")
        print()
def check_replace(board, r, c):
    if board[r][c] != "_":
        print("this box is full!")
        return False
    else:
        return True
def enter_choice(player, board):
    while True:
        player_r = int(input(f"player{player} row: "))
        player_c = int(input(f"player{player} colum: "))
        if (0 < player_r < 4) and (0 < player_c < 4):
            break
        if check_replace(board, player_r - 1, player_c - 1) == True:
            pass
        else:
            print("this box is full!")
            continue
        print("index out off range!")
    if player == 1:
        board[player_r - 1][player_c - 1] = "X"
    if player == 2:
        board[player_r - 1][player_c - 1] = "O"


board = [["_", "_", "_"]
, ["_", "_", "_"]
, ["_", "_", "_"]]

while True:
    show_board(board)
    enter_choice(1)
    show_board(board)
    enter_choice(2)