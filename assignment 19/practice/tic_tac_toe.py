import random
from functools import partial
from PySide6.QtWidgets import *
from PySide6.QtUiTools import *
from PySide6.QtCore import *

class TicTacToe(QMainWindow):
    def __init__(self):
        super().__init__()
        loader = QUiLoader()
        self.ui = loader.load("TicTacToe.ui", None)
        self.ui.show()
        self.game = [[self.ui.btn_1, self.ui.btn_2, self.ui.btn_3],
                     [self.ui.btn_4, self.ui.btn_5, self.ui.btn_6],
                     [self.ui.btn_7, self.ui.btn_8, self.ui.btn_9]]
        for i in range(3):
            for j in range(3):
                self.game[i][j].setText("")
                self.game[i][j].setStyleSheet("color: rgb(255, 255, 255); background-color:rgb(100, 100, 100)")
                self.game[i][j].clicked.connect(partial(self.Play, i, j))
        self.ui.btn_new.clicked.connect(self.new_game)
        self.player = "😍"
        self.player_score = 0
        self.player2_score = 0
    def check(self): 
        if ((self.game[0][0].text() == "😍" and self.game[1][1].text() == "😍" and self.game[2][2].text() == "😍") or (self.game[0][2].text() == "😍" and self.game[1][1].text() == "😍" and self.game[2][0].text() == "😍") or (self.game[0][0].text() == "😍" and self.game[0][1].text() == "😍" and self.game[0][2].text() == "😍") or (self.game[1][0].text() == "😍" and self.game[1][1].text() == "😍" and self.game[1][2].text() == "😍") or (self.game[2][0].text() == "😍" and self.game[2][1].text() == "😍" and self.game[2][2].text() == "😍") or (self.game[0][0].text() == "😍" and self.game[1][0].text() == "😍" and self.game[2][0].text() == "😍") or (self.game[0][1].text() == "😍" and self.game[1][1].text() == "😍" and self.game[2][1].text() == "😍") or (self.game[0][2].text() == "😍" and self.game[1][2].text() == "😍" and self.game[2][2].text() == "😍")):
            self.player_score += 1
            ms_box = QMessageBox()
            ms_box.setText("player 1 wins")
            self.ui.scorex.setText(str(self.player_score))
            ms_box.exec()
            self.new_game()
        elif ((self.game[0][0].text() == "🤩" and self.game[1][1].text() == "🤩" and self.game[2][2].text() == "🤩") or (self.game[0][2].text() == "🤩" and self.game[1][1].text() == "🤩" and self.game[2][0].text() == "🤩") or (self.game[0][0].text() == "🤩" and self.game[0][1].text() == "🤩" and self.game[0][2].text() == "🤩") or (self.game[1][0].text() == "🤩" and self.game[1][1].text() == "🤩" and self.game[1][2].text() == "🤩") or (self.game[2][0].text() == "🤩" and self.game[2][1].text() == "🤩" and self.game[2][2].text() == "🤩") or (self.game[0][0].text() == "🤩" and self.game[1][0].text() == "🤩" and self.game[2][0].text() == "🤩") or (self.game[0][1].text() == "🤩" and self.game[1][1].text() == "🤩" and self.game[2][1].text() == "🤩") or (self.game[0][2].text() == "🤩" and self.game[1][2].text() == "🤩" and self.game[2][2].text() == "🤩")):
            self.player2_score += 1
            ms_box = QMessageBox()
            ms_box.setText("player2 win")
            self.ui.scoreo.setText(str(self.player2_score))
            ms_box.exec()
            self.new_game()
        if self.game[0][0].text() != "" and self.game[0][1].text() != "" and self.game[0][2].text() != "" and self.game[1][0].text() != "" and self.game[1][1].text() != "" and self.game[1][2].text() != "" and self.game[2][0].text() != "" and self.game[2][1].text() != "" and self.game[2][2].text() != "":
            ms_box = QMessageBox()
            ms_box.setText("draw")
            ms_box.exec()
            self.new_game()
    def Play(self, i, j):
        if self.game[i][j].text() == "":
            if self.ui.btn_ptp.isChecked():
                if self.player == "😍":
                    self.game[i][j].setText("😍")
                    self.game[i][j].setStyleSheet("background-color: rgb(0, 170, 255);")
                    self.player = "🤩"
                else:
                    self.game[i][j].setText("🤩")
                    self.game[i][j].setStyleSheet("background-color: rgb(255, 85, 0);")
                    self.player = "😍"
            if self.ui.btn_ptc.isChecked():
                if self.player == "😍":
                    self.game[i][j].setText("😍")
                    self.game[i][j].setStyleSheet("background-color: rgb(0, 170, 255);")
                    self.player = "🤩"
                if self.player == "🤩":
                    while True:
                        i = random.randint(0, 2)
                        j = random.randint(0, 2)
                        if self.game[i][j].text() == "":
                            self.game[i][j].setText("🤩")
                            self.game[i][j].setStyleSheet("background-color: rgb(255, 85, 0);")
                            self.player = "😍"
                            break
        self.check()
    def new_game(self):
        for i in range(3):
            for j in range(3):
                self.game[i][j].setStyleSheet("color: rgb(255, 255, 255); background-color:rgb(100, 100, 100)")
                self.game[i][j].setText("")

app = QApplication([])
window = TicTacToe()
app.exec()