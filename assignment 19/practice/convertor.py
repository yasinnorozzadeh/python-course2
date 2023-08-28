from PySide6.QtWidgets import *
from PySide6.QtUiTools import *
from PySide6.QtCore import *

class Convertor(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        loader = QUiLoader()
        self.ui = loader.load("start_convertor.ui", None)
        self.ui1 = loader.load("convertor_temp.ui", None)
        self.ui2 = loader.load("convertor_length.ui", None)
        self.ui3 = loader.load("convertor_currency.ui", None)
        self.ui4 = loader.load("convertor_transfer.ui", None)
        self.ui.show()

        self.ui.btn_tmp.clicked.connect(self.temp)
        self.ui.btn_len.clicked.connect(self.length)
        self.ui.btn_cur.clicked.connect(self.currency)
        self.ui.btn_dat.clicked.connect(self.transfer)
     
    def temp(self):
        self.ui1.show()
        self.ui.close()
        self.ui1.btn_c.clicked.connect(self.check_t)

    def length(self):
        self.ui2.show()
        self.ui.close()
        self.ui2.btn_c.clicked.connect(self.check_l)

    def currency(self):
        self.ui3.show()
        self.ui.close()
        self.ui3.btn_c.clicked.connect(self.check_c)
        

    def transfer(self):
        self.ui4.show()
        self.ui.close()
        self.ui4.btn_c.clicked.connect(self.check_t)


    
    def check_t(self):
        if self.ui1.rb_CF.isChecked() == True:
            text = self.ui1.line.text()
            self.result = self.convert(text, 0)
            self.ui1.line.setText(str(self.result))

        elif self.ui1.rb_CK.isChecked() == True:
            text = self.ui1.line.text()
            self.result = self.convert(text, 1)
            self.ui1.line.setText(str(self.result))

        elif self.ui1.rb_KF.isChecked() == True:
            text = self.ui1.line.text()
            self.result = self.convert(text, 2)
            self.ui1.line.setText(str(self.result))

        elif self.ui1.rb_FK.isChecked() == True:
            text = self.ui1.line.text()
            self.result = self.convert(text, 3)
            self.ui1.line.setText(str(self.result))

        elif self.ui1.rb_KC.isChecked() == True:
            text = self.ui1.line.text()
            self.result = self.convert(text, 4)
            self.ui1.line.setText(str(self.result))

        elif self.ui1.rb_FC.isChecked() == True:
            text = self.ui1.line.text()
            self.result = self.convert(text, 5)
            self.ui1.line.setText(str(self.result))

        else:
            self.ui1.line.setText("choose temperature for conversion")

    def check_l(self):
        self.text = self.ui2.line.text()
        if self.ui2.rb_YM.isChecked() == True:
            self.result = self.convert(self.text, 6)
            self.ui2.line.setText(str(self.result))

        elif self.ui2.rb_FM.isChecked() == True:
            self.result = self.convert(self.text, 7)
            self.ui2.line.setText(str(self.result))

        elif self.ui2.rb_IM.isChecked() == True:
            self.result = self.convert(self.text, 8)
            self.ui2.line.setText(str(self.result))

        elif self.ui2.rb_MY.isChecked() == True:
            self.result = self.convert(self.text, 9)
            self.ui2.line.setText(str(self.result))

        elif self.ui2.rb_FY.isChecked() == True:
            self.result = self.convert(self.text, 10)
            self.ui2.line.setText(str(self.result))

        elif self.ui2.rb_IY.isChecked() == True:
            self.result = self.convert(self.text, 11)
            self.ui2.line.setText(str(self.result))

        elif self.ui2.rb_MF.isChecked() == True:
            self.result = self.convert(self.text, 12)
            self.ui2.line.setText(str(self.result))

        elif self.ui2.rb_YF.isChecked() == True:
            self.result = self.convert(self.text, 13)
            self.ui2.line.setText(str(self.result))

        elif self.ui2.rb_IF.isChecked() == True:
            self.result = self.convert(self.text, 14)
            self.ui2.line.setText(str(self.result))

        elif self.ui2.rb_MI.isChecked() == True:
            self.result = self.convert(self.text, 15)
            self.ui2.line.setText(str(self.result))

        elif self.ui2.rb_YI.isChecked() == True:
            self.result = self.convert(self.text, 16)
            self.ui2.line.setText(str(self.result))

        elif self.ui2.rb_FI.isChecked() == True:
            self.result = self.convert(self.text, 17)
            self.ui2.line.setText(str(self.result))
        
        else:
            self.ui2.line.setText("choose temperature for conversion")
         
    def check_c(self):
        self.text = self.ui3.line.text()
        if self.ui3.rb_PR.isChecked() == True:
            self.result = self.convert(self.text, 18)
            self.ui3.line.setText(str(self.result))
        elif self.ui3.rb_DR.isChecked() == True:
            self.result = self.convert(self.text, 19)
            self.ui3.line.setText(str(self.result))
        elif self.ui3.rb_FR.isChecked() == True:
            self.result = self.convert(self.text, 20)
            self.ui3.line.setText(str(self.result))
        elif self.ui3.rb_RP.isChecked() == True:
            self.result = self.convert(self.text, 21)
            self.ui3.line.setText(str(self.result))
        elif self.ui3.rb_DP.isChecked() == True:
            self.result = self.convert(self.text, 22)
            self.ui3.line.setText(str(self.result))
        elif self.ui3.rb_FP.isChecked() == True:
            self.result = self.convert(self.text, 23)
            self.ui3.line.setText(str(self.result))
        elif self.ui3.rb_RD.isChecked() == True:
            self.result = self.convert(self.text, 24)
            self.ui3.line.setText(str(self.result))
        elif self.ui3.rb_PD.isChecked() == True:
            self.result = self.convert(self.text, 25)
            self.ui3.line.setText(str(self.result))
        elif self.ui3.rb_FD.isChecked() == True:
            self.result = self.convert(self.text, 26)
            self.ui3.line.setText(str(self.result))
        elif self.ui3.rb_RF.isChecked() == True:
            self.result = self.convert(self.text, 27)
            self.ui3.line.setText(str(self.result))
        elif self.ui3.rb_PF.isChecked() == True:
            self.result = self.convert(self.text, 28)
            self.ui3.line.setText(str(self.result))
        elif self.ui3.rb_DF.isChecked() == True:
            self.result = self.convert(self.text, 29)
            self.ui3.line.setText(str(self.result))
        else:
            self.ui3.line.setText("choose temperature for conversion")
    def check_t(self):
        self.text = self.ui4.line.text()
        if self.ui4.rb_KB.isChecked() == True:
            self.result = self.convert(self.text, 30)
            self.ui4.line.setText(str(self.result))

        elif self.ui4.rb_MB.isChecked() == True:
            self.result = self.convert(self.text, 31)
            self.ui4.line.setText(str(self.result))

        elif self.ui4.rb_GB.isChecked() == True:
            self.result = self.convert(self.text, 32)
            self.ui4.line.setText(str(self.result))

        elif self.ui4.rb_BK.isChecked() == True:
            self.result = self.convert(self.text, 33)
            self.ui4.line.setText(str(self.result))

        elif self.ui4.rb_MK.isChecked() == True:
            self.result = self.convert(self.text, 34)
            self.ui4.line.setText(str(self.result))

        elif self.ui4.rb_GK.isChecked() == True:
            self.result = self.convert(self.text, 35)
            self.ui4.line.setText(str(self.result))

        elif self.ui4.rb_BM.isChecked() == True:
            self.result = self.convert(self.text, 36)
            self.ui4.line.setText(str(self.result))

        elif self.ui4.rb_KM.isChecked() == True:
            self.result = self.convert(self.text, 37)
            self.ui4.line.setText(str(self.result))

        elif self.ui4.rb_GM.isChecked() == True:
            self.result = self.convert(self.text, 38)
            self.ui4.line.setText(str(self.result))

        elif self.ui4.rb_BG.isChecked() == True:
            self.result = self.convert(self.text, 39)
            self.ui4.line.setText(str(self.result))

        elif self.ui4.rb_KG.isChecked() == True:
            self.result = self.convert(self.text, 40)
            self.ui4.line.setText(str(self.result))

        elif self.ui4.rb_MG.isChecked() == True:
            self.result = self.convert(self.text, 41)
            self.ui4.line.setText(str(self.result))

        else:
            self.ui4.line.setText("choose temperature for conversion")

    def convert(self, num,  x):
        if num != "" and num != "choose temperature for conversion":
            if x == 0:
                self.result = ((9/5) * float(num)) + 32
            elif x == 1:
                self.result = float(num) + 273.15
            elif x == 2:
                self.result = (float(num) - 273.15) * (9/5) + 32
            elif x == 3:
                self.result = ((float(num) - 32) * (5/9)) + 273.15
            elif x == 4:
                self.result = float(num) - 273.15
            elif x == 5:
                self.result = (float(num) - 32) * (5/9)
            elif x == 6:
                self.result = float(num) / 1.94
            elif x == 7:
                self.result = float(num) / 3.281
            elif x == 8:
                self.result = float(num) / 39.37
            elif x == 9:
                self.result = float(num) * 1.094
            elif x == 10:
                self.result = float(num) / 3
            elif x == 11:
                self.result = float(num) / 36
            elif x == 12:
                self.result = float(num) * 3.281
            elif x == 13:
                self.result = float(num) * 3
            elif x == 14:
                self.result = float(num) / 12
            elif x == 15:
                self.result = float(num) * 39.37
            elif x == 16:
                self.result = float(num) * 36
            elif x == 17:
                self.result = float(num) * 12
            elif x == 18:
                self.result = float(num) * 53264.39
            elif x == 19:
                self.result = float(num) * 42275
            elif x == 20:
                self.result = float(num) * 47820.47
            elif x == 21:
                self.result = float(num) * 0.000019
            elif x == 22:
                self.result = float(num) * 0.79
            elif x == 23:
                self.result = float(num) * 0.90
            elif x == 24:
                self.result = float(num) * 0.000024
            elif x == 25:
                self.result = float(num) * 1.26
            elif x == 26:
                self.result = float(num) * 1.13
            elif x == 27:
                self.result = float(num) * 0.000021
            elif x == 28:
                self.result = float(num) * 1.11
            elif x == 29:
                self.result = float(num) * 0.88
            elif x == 30:
                self.result = float(num) * 1000
            elif x == 31:
                self.result = float(num) * 1.049e+6
            elif x == 32:
                self.result = float(num) * 1e+9
            elif x == 33:
                self.result = float(num) / 1000
            elif x == 34:
                self.result = float(num) * 1024
            elif x == 35:
                self.result = float(num) * 1e+6
            elif x == 36:
                self.result = float(num) / 1e+6
            elif x == 37:
                self.result = float(num) / 1049
            elif x == 38:
                self.result = float(num) * 953.7
            elif x == 39:
                self.result = float(num) / 1e+9
            elif x == 40:
                self.result = float(num) / 1e+6
            elif x == 41:
                self.result = float(num) / 1000
        else:
            self.result = "input youre number"
        return self.result

app = QApplication([])
window = Convertor()
app.exec()