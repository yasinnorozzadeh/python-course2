from termcolor import colored
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
def enter_choice(player, board, char1, char2):
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
        board[player_r - 1][player_c - 1] = char1
    if player == 2:
        board[player_r - 1][player_c - 1] = char2
def check_game(board, player1, player2):
    for i in range(3):
        s1c = 0
        s2c = 0
        if board[0][i] == player1 and board[1][i] == player1 and board[2][i] == player1:
            s1c += 3
        elif board[0][i] == player2 and board[1][i] == player2 and board[2][i] == player2:
            s2c += 3
    for r in range(3):
        s1r = 0
        s2r = 0
        for c in range(3):
            if  board[r][c] == player1:
                s1r += 1
            elif board[r][c] == player2:
                s2r += 1

        if s1r == 3 or s1c == 3:
            print("palyer one wins", "\nTime out is:")
            exit()
        elif s2r == 3 or s2c == 3:
            print("player two wins", "\nTime out is:")
            exit()
    if board[0][0] == player1 and board[1][1] == player1 and board[2][2] == player1 or board[0][2] == player1 and board[1][1] == player1 and board[2][0] == player1:
        print("player one wins", "\nTime out is:")
        exit()
    elif board[0][0] == player2 and board[1][1] == player2 and board[2][2] == player2 or board[2][0] == player2 and board[1][1] == player2 and board[0][2] == player2:
        print("player two wins", "\nTime out is:")
        exit()

board = [["_", "_", "_"], ["_", "_", "_"], ["_", "_", "_"]]
player1_char = input("player1 enter your charcter:\t")
player2_char = input("player2 enter your character:\t")
while True:
    show_board(board)
    enter_choice(1, board, player1_char, player2_char)
    show_board(board)
    enter_choice(2, board, player1_char, player2_char)