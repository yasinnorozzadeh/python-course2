import random 
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import *

class Logic:
    def __init__(self):pass
    def start_game(self):
        board = []
        for i in range(4):
            board.append([0] * 4)
        board = self.add_new_2(board)

        return board
    
    def add_new_2(self, board):
        while True:
            row = random.randint(0, 3)
            column = random.randint(0, 3)
            if board[row][column] == 0:
                board[row][column] = 2
                break

        return board
    def get_current_state(self, board):
        for i in range(4):
            for j in range(4):
                if board[i][j] == 2048:
                    return "WON"
        
        for i in range(4):
            for j in range(4):
                if board[i][j] == 0:
                    return "Game Not Over"

        for i in range(3):
            for j in range(3):
                if (board[i][j] == board[i+1][j]) or (board[i][j] == board[i][j+1]):
                    return "Game Not Over"

        for i in range(3):
            if board[3][i] == board[3][i+1]:
                return "Game Not Over"

        for i in range(3):
            if board[i][3] == board[i+1][3]:
                return "Game Not Over"

        return "Lose"

    def compress(self, board):
        flag = False
        new_board = []

        for i in range(4):
            new_board.append([0]*4)

        for i in range(4):
            p = 0
            for j in range(4):
                if board[i][j] != 0:
                    new_board[i][p] = board[i][j]
                    if j != p:
                        flag = True

                    p+=1

        return new_board, flag

    def merge(self, board):
        flag = False
        for i in range(4): 
            for j in range(3): 
                if board[i][j] == board[i][j+1] and board[i][j] != 0 and board[i][j+1] != 0:
                    board[i][j] = board[i][j] + board[i][j+1]
                    board[i][j+1] = 0
                    flag = True

        return board, flag 

    def reverse(self, board):
        new_board = []
        for i in range(4):
            new_board.append([])
            for j in range(4):
                new_board[i].append(board[i][3-j])

        return new_board

    def reverse_2(self, board):
        new_board = []
        for i in range(4):
            new_board.append([])
            for j in range(4):
                new_board[i].append(board[3-i][j])

        return new_board

    def transpose(self, board):
        new_board = []

        for i in range(4):
            new_board.append([])
            for j in range(4):
                new_board[i].append(board[j][i])

        return new_board

    def move_left(self, board):
        new_grid, flag_1 = self.compress(board)
        new_grid, flag_2 = self.merge(new_grid)
        flag = flag_1 or flag_2
        new_grid, _ = self.compress(new_grid)
        status = self.get_current_state(board)
        return new_grid, flag, status

    def move_right(self, board):
        new_grid = self.reverse(board)
        new_grid, flag, _ = self.move_left(new_grid)
        new_grid = self.reverse(new_grid)
        status = self.get_current_state(board)

        return new_grid, flag, status

    def move_up(self, board):
        new_grid = self.transpose(board)
        new_grid, flag, _ = self.move_left(new_grid)
        new_grid = self.transpose(new_grid)
        status = self.get_current_state(board)
        return new_grid, flag , status

    def move_down(self, board):
        new_g = self.reverse_2(board)
        new_g, flag, _ = self.move_up(new_g)
        new_g = self.reverse_2(new_g)
        status = self.get_current_state(board)

        return new_g, flag, status

class Game(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.ui = QUiLoader().load("2048.ui")
        self.ui.show()
        self.logic = Logic()
        self.game_board = self.logic.start_game()
        self.btns = [[self.ui.btn_0_0, self.ui.btn_0_1, self.ui.btn_0_2, self.ui.btn_0_3],
                        [self.ui.btn_1_0, self.ui.btn_1_1, self.ui.btn_1_2, self.ui.btn_1_3],
                        [self.ui.btn_2_0, self.ui.btn_2_1, self.ui.btn_2_2, self.ui.btn_2_3],
                        [self.ui.btn_3_0, self.ui.btn_3_1, self.ui.btn_3_2, self.ui.btn_3_3]]
        self.show_ui()
        self.ui.btn_up.setShortcut(app.tr("up"))
        self.ui.btn_down.setShortcut(app.tr("down"))
        self.ui.btn_right.setShortcut(app.tr("right"))
        self.ui.btn_left.setShortcut(app.tr("left"))
        self.ui.btn_up.clicked.connect(self.up)
        self.ui.btn_down.clicked.connect(self.down)
        self.ui.btn_left.clicked.connect(self.left)
        self.ui.btn_right.clicked.connect(self.right)
        self.ui.btn_help.clicked.connect(self.help)
    def show_ui(self):
        colors = {2:"255, 255, 255", 4:"255, 255, 200", 8:"255, 190, 110", 16:"255, 150, 110", 32:"255, 100, 110", 64:"255, 50, 50", 128:"255, 255, 130", 256:"255, 255, 90", 512:"255, 255, 70", 1024:"255, 255, 40", 2048:"255, 255, 0", 4096:"0, 85, 255"}
        for i in range(4):
            for j in range(4):
                if self.game_board[i][j] == 0:
                    self.btns[i][j].setStyleSheet("background-color: rgb(0, 0, 0);")
                    self.btns[i][j].setText("⬜")
                else:
                    self.btns[i][j].setStyleSheet("")
                    self.btns[i][j].setText(str(self.game_board[i][j]))
                    self.btns[i][j].setStyleSheet(f"background-color: rgb({colors[self.game_board[i][j]]});")
            
    def up(self):
        self.game_board, _, status = self.logic.move_up(self.game_board)
        self.check(status, self.game_board)

    def down(self):
        self.game_board, _, status = self.logic.move_down(self.game_board)
        self.check(status, self.game_board)

    def left(self):
        self.game_board, _, status = self.logic.move_left(self.game_board)
        self.check(status, self.game_board)

    def right(self):
        self.game_board, _, status = self.logic.move_right(self.game_board)
        self.check(status, self.game_board)

    def check(self, status, board):
        if status == "Game Not Over":
            self.logic.add_new_2(board)
            self.show_ui()
        elif status == "Lose":
            ms_box = QMessageBox()
            ms_box.setText("Game Over")
            ms_box.setStyleSheet("background-color: rgb(0, 0, 0);font: 700 italic 20pt 'Segoe UI';color: rgb(255, 255, 255);")
            ms_box.exec()
            self.ui.close()
        elif status == "WON":
            ms_box = QMessageBox()
            ms_box.setText("You Win")
            ms_box.setStyleSheet("background-color: rgb(255, 255, 255);font: 700 italic 20pt 'Segoe UI';color: rgb(0, 0, 0);")
            ms_box.exec()
    
    def help(self):
        ms_box = QMessageBox()
        ms_box.setText("program was developed by:\nhttps://github.com/yasinnorozzadeh\n\nup: up arrow\ndown: down arrow\nleft: left arrow\nright: right arrow")
        ms_box.setStyleSheet("background-color: rgb(0, 0, 0);font: 700 italic 20pt 'Segoe UI';color: rgb(85, 255, 255);")
        ms_box.exec()
app = QApplication([])
window = Game()
app.exec()