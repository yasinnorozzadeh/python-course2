from termcolor import colored
import pyfiglet
# 😎
# 😘
def show_board(board):
    for i in range(3):
        for j in range(3):
            print(colored(board[i][j], "cyan"), end=" ")
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
            if check_replace(board, player_r - 1, player_c - 1) == True:
                break
            else:
                continue
        else:
            print("index out off range!")
            continue
    if player == 1:
        board[player_r - 1][player_c - 1] = char1
    if player == 2:
        board[player_r - 1][player_c - 1] = char2
def check_game(board, player1, player2):
    winer = ""
    for r in range(3):
        s1r = 0
        s2r = 0
        s1c = 0
        s2c = 0
        for c in range(3):
            if  board[r][c] == player1:
                s1r += 1
            elif board[r][c] == player2:
                s2r += 1
            elif  board[c][r] == player1:
                s1c += 1
            elif board[c][r] == player2:
                s2c += 1

        if s1r == 3 or s1c == 3:
            winer = "player1"
        elif s2r == 3 or s2c == 3:
            winer = "player2"
    if board[0][0] == player1 and board[1][1] == player1 and board[2][2] == player1 or board[0][2] == player1 and board[1][1] == player1 and board[2][0] == player1:
        winer = "player1"
    elif board[0][0] == player2 and board[1][1] == player2 and board[2][2] == player2 or board[2][0] == player2 and board[1][1] == player2 and board[0][2] == player2:
        winer = "player2"
    c = 0
    for i in range(3):
        for j in range(3):
            if not(board[i][j] == "_"):
                c += 1
    if c == 9 and winer == "":
        winer = "equal"
    return winer

text = pyfiglet.figlet_format("welcome to Tic Tac Toe game", font="bubble")
print(colored(text, "green"))
board = [["_", "_", "_"], ["_", "_", "_"], ["_", "_", "_"]]
player1_char = colored(input("player1 enter your charcter:\t"), "red")
player2_char = colored(input("player2 enter your character:\t"), "red")
winer = check_game(board, player1_char, player2_char)
while winer == "" and winer != "equal":
    show_board(board)
    enter_choice(1, board, player1_char, player2_char)
    winer = check_game(board, player1_char, player2_char)
    if winer != "":
        continue
    show_board(board)
    enter_choice(2, board, player1_char, player2_char)
    winer = check_game(board, player1_char, player2_char)  
show_board(board)
if winer == "equal":
    text = "equal"
else:
    text = f"{winer} is winer"
print(colored(text, "yellow"))
text = pyfiglet.figlet_format("good bye!", font="doh")
print(colored(text, "blue"))
