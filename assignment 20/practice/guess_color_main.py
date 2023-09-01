from PySide6.QtWidgets import *
from PySide6.QtUiTools import *
from PySide6.QtCore import *
import random

class Game(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        loader = QUiLoader()
        self.ui1 = loader.load("guess_color_start.ui", None)
        self.ui2 = loader.load("guess_color_game.ui", None)
        self.ui1.show()
        self.score = 0
        self.counter = 0
        self.minute = '00'
        self.second = '00'
        self.count = '00'
        self.ui1.btn_start.clicked.connect(self.start_game)
        self.colors = ["red", "green", "gray", "blue", "yellow", "white", "pink", "orange", "purple", "gold", "bice", "magenta"]
        
    def timee(self):
        self.counter += 1
        cnt = int((self.counter/10 - int(self.counter/10))*10)
        self.count = '0' + str(cnt)
        if int(self.counter/10) < 10 :
            self.second = '0' + str(int(self.counter / 10))
        else:
            self.second = str(int(self.counter / 10))
            # Set the minute value
            if self.counter / 10 == 60.0 :
                self.second == '00'
                self.counter = 0
                min = int(self.minute) + 1
                if min < 10 :
                    self.minute = '0' + str(min)
                else:
                    self.minute = str(min)


        # Merge the mintue, second and count values
        text = self.minute + ':' + self.second + ':' + self.count
        # Display the stop watch values in the label
        self.ui2.label_time.setText('<h1 style="color:blue">' + text + '</h5>')
        if self.minute == "01":
            self.check(1)

    def start_game(self):
        self.ui2.show()
        self.ui1.close()
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.timee)
        self.timer.start(100)
        self.word  = random.choice(self.colors)
        self.color = random.choice(self.colors)
        self.ui2.text.setText(f'<h1 style="color:{self.color}">' + self.word + "</h1>")
        self.ui2.btn_check.clicked.connect(self.check)
        print(self.color)
    def check(self, x=0):
        if x == 0:
            self.t = self.ui2.line.text()
            if self.t == self.color:
                self.score += 1
                self.word  = random.choice(self.colors)
                self.color = random.choice(self.colors)
                self.ui2.label_score.setText(str(self.score))
                self.ui2.text.setText(f'<h1 style="color:{self.color}">' + self.word)
            print(self.color)
        else:
            self.timer.stop()
            ms_box = QMessageBox()
            ms_box.setText(f"youre score: {self.score}")
            ms_box.setStyleSheet("background-color: rgb(255, 0, 127);font: 700 italic 20pt 'Segoe UI';")
            ms_box.exec()



        
        
        


app = QApplication([])
window = Game()
app.exec()