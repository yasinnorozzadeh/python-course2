import math
from functools import partial
from PySide6.QtWidgets import QApplication
from PySide6.QtUiTools import QUiLoader
op = None
num_1 = 0
num_2 = 0
def design():
    """
    design buttons
    """
    # numbers button from 0 to 9
    main_window.btn_0.setStyleSheet('''QPushButton:hover {background-color:rgb(0, 255, 0);};
                                    font: 700 italic 14pt "Segoe UI";
                                    background-color: rgb(85, 255, 255);
                                    color: rgb(255, 0, 127);
                                    background-color:white;''')
    main_window.btn_1.setStyleSheet('''QPushButton:hover {background-color:rgb(0, 255, 0);};
                                    font: 700 italic 14pt "Segoe UI";
                                    background-color: rgb(85, 255, 255);
                                    color: rgb(255, 0, 127);''')
    main_window.btn_2.setStyleSheet('''QPushButton:hover {background-color:rgb(0, 255, 0);};
                                    font: 700 italic 14pt "Segoe UI";
                                    background-color: rgb(85, 255, 255);
                                    color: rgb(255, 0, 127);''')
    main_window.btn_3.setStyleSheet('''QPushButton:hover {background-color:rgb(0, 255, 0);};
                                    font: 700 italic 14pt "Segoe UI";
                                    background-color: rgb(85, 255, 255);
                                    color: rgb(255, 0, 127);''')
    main_window.btn_4.setStyleSheet('''QPushButton:hover {background-color:rgb(0, 255, 0);};
                                    font: 700 italic 14pt "Segoe UI";
                                    background-color: rgb(85, 255, 255);
                                    color: rgb(255, 0, 127);''')
    main_window.btn_5.setStyleSheet('''QPushButton:hover {background-color:rgb(0, 255, 0);};
                                    font: 700 italic 14pt "Segoe UI";
                                    background-color: rgb(85, 255, 255);
                                    color: rgb(255, 0, 127);''')
    main_window.btn_6.setStyleSheet('''QPushButton:hover {background-color:rgb(0, 255, 0);};
                                    font: 700 italic 14pt "Segoe UI";
                                    background-color: rgb(85, 255, 255);
                                    color: rgb(255, 0, 127);''')
    main_window.btn_7.setStyleSheet('''QPushButton:hover {background-color:rgb(0, 255, 0);};
                                    font: 700 italic 14pt "Segoe UI";
                                    background-color: rgb(85, 255, 255);
                                    color: rgb(255, 0, 127);''')
    main_window.btn_8.setStyleSheet('''QPushButton:hover {background-color:rgb(0, 255, 0);};
                                    font: 700 italic 14pt "Segoe UI";
                                    background-color: rgb(85, 255, 255);
                                    color: rgb(255, 0, 127);''')
    main_window.btn_9.setStyleSheet('''QPushButton:hover {background-color:rgb(0, 255, 0);};
                                    font: 700 italic 14pt "Segoe UI";
                                    background-color: rgb(85, 255, 255);
                                    color: rgb(255, 0, 127);''')
    # sub button
    main_window.btn_sub.setStyleSheet('''QPushButton:hover {background-color:rgb(153, 51, 255);};
                                    font: 10000 italic 14pt "Segoe UI";
                                    background-color: rgb(102, 0, 102);
                                    color: rgb(50, 255, 255);''')
    # sum button
    main_window.btn_sum.setStyleSheet('''QPushButton:hover {background-color:rgb(153, 51, 255);};
                                    font: 900 italic 14pt "Segoe UI";
                                    background-color: rgb(102, 0, 102);
                                    color: rgb(50, 255, 255);''')
    # multiplication button
    main_window.btn_mul.setStyleSheet('''QPushButton:hover {background-color:rgb(153, 51, 255);};
                                    font: 700 italic 14pt "Segoe UI";
                                    background-color: rgb(102, 0, 102);
                                    color: rgb(50, 255, 255);''')
    # division button
    main_window.btn_div.setStyleSheet('''QPushButton:hover {background-color:rgb(153, 51, 255);};
                                    font: 900 italic 14pt "Segoe UI";
                                    background-color: rgb(102, 0, 102);
                                    color: rgb(50, 255, 255);''')
    # power button
    main_window.btn_pow.setStyleSheet('''QPushButton:hover {background-color:rgb(0, 255, 255);};
                                    font: 700 italic 14pt "Segoe UI";
                                    background-color: rgb(255, 255, 0);
                                    color: rgb(0, 0, 255);''')
    # sqrt button
    main_window.btn_sqrt.setStyleSheet('''QPushButton:hover {background-color:rgb(0, 255, 255);};
                                    font: 700 italic 14pt "Segoe UI";
                                    background-color: rgb(255, 255, 0);
                                    color: rgb(0, 0, 255);''')
    # cot button
    main_window.btn_cot.setStyleSheet('''QPushButton:hover {background-color:rgb(0, 255, 255);};
                                    font: 700 italic 14pt "Segoe UI";
                                    background-color: rgb(255, 255, 0);
                                    color: rgb(0, 0, 255);''')
    # log button
    main_window.btn_log.setStyleSheet('''QPushButton:hover {background-color:rgb(0, 255, 255);};
                                    font: 700 italic 14pt "Segoe UI";
                                    background-color: rgb(255, 255, 0);
                                    color: rgb(0, 0, 255);''')
    # cos button
    main_window.btn_cos.setStyleSheet('''QPushButton:hover {background-color:rgb(0, 255, 255);};
                                    font: 700 italic 14pt "Segoe UI";
                                    background-color: rgb(255, 255, 0);
                                    color: rgb(0, 0, 255);''')
    # fuctorial button
    main_window.btn_fuc.setStyleSheet('''QPushButton:hover {background-color:rgb(0, 255, 255);};
                                    font: 700 italic 14pt "Segoe UI";
                                    background-color: rgb(255, 255, 0);
                                    color: rgb(0, 0, 255);''')
    # sin button
    main_window.btn_sin.setStyleSheet('''QPushButton:hover {background-color:rgb(0, 255, 255);};
                                    font: 700 italic 14pt "Segoe UI";
                                    background-color: rgb(255, 255, 0);
                                    color: rgb(0, 0, 255);''')
    # pi button
    main_window.btn_pi.setStyleSheet('''QPushButton:hover {background-color:rgb(0, 255, 255);};
                                    font: 700 italic 14pt "Segoe UI";
                                    background-color: rgb(255, 255, 0);
                                    color: rgb(0, 0, 255);''')
    # tan button
    main_window.btn_tan.setStyleSheet('''QPushButton:hover {background-color:rgb(0, 255, 255);};
                                    font: 700 italic 14pt "Segoe UI";
                                    background-color: rgb(255, 255, 0);
                                    color: rgb(0, 0, 255);''')
    # dot button
    main_window.btn_dot.setStyleSheet('''QPushButton:hover {background-color:rgb(0, 255, 255);};
                                    font: 700 italic 14pt "Segoe UI";
                                    background-color: rgb(0, 0, 255);
                                    color: rgb(255, 255, 0);''')
    # abs button
    main_window.btn_abs.setStyleSheet('''QPushButton:hover {background-color:rgb(0, 255, 255);};
                                    font: 700 italic 14pt "Segoe UI";
                                    background-color: rgb(0, 0, 255);
                                    color: rgb(255, 255, 0);''')
    # ac button
    main_window.btn_ac.setStyleSheet('''QPushButton:hover {background-color:rgb(153, 153, 0);};
                                    font: 700 italic 14pt "Segoe UI";
                                    background-color: rgb(0, 102, 0);
                                    color: rgb(255, 128, 0);''')
    # # c button
    main_window.btn_c.setStyleSheet('''QPushButton:hover {background-color:rgb(153, 153, 0);};
                                    font: 700 italic 14pt "Segoe UI";
                                    background-color: rgb(0, 102, 0);
                                    color: rgb(255, 128, 0);''')
    # equal button
    main_window.btn_eq.setStyleSheet('''QPushButton:hover {background-color:rgb(153, 153, 0);};
                                    font: 700 italic 14pt "Segoe UI";
                                    background-color: rgb(255, 0, 127);
                                    color: rgb(0, 0, 0);''')
    main_window.setStyleSheet('''background-color: qconicalgradient(cx:0, cy:0, angle:14.8, stop:0 rgba(0, 255, 255, 255), stop:0.164773 rgba(0, 177, 255, 255), stop:0.329545 rgba(0, 86, 255, 255), stop:0.5 rgba(0, 0, 255, 255), stop:0.653409 rgba(0, 87, 255, 255), stop:0.835227 rgba(0, 180, 255, 255), stop:1 rgba(0, 255, 255, 255));''')
    # line Edit
    main_window.lineEdit.setStyleSheet('''background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 0, 0, 255), stop:0.166 rgba(255, 255, 0, 255), stop:0.333 rgba(0, 255, 0, 255), stop:0.5 rgba(0, 255, 255, 255), stop:0.666 rgba(0, 0, 255, 255), stop:0.833 rgba(255, 0, 255, 255), stop:1 rgba(255, 0, 0, 255));''')

def num(x):
    text = main_window.lineEdit.text()
    main_window.lineEdit.setText(text + x)

def ac():
    main_window.lineEdit.setText("")

def c():
    t = main_window.lineEdit.text()
    main_window.lineEdit.setText(t[:-1])

def dot():
    if "." not in main_window.lineEdit.text():
        main_window.lineEdit.setText(main_window.lineEdit.text() + ".")

def sum():
    global op , num_1
    op = "+"
    num_1 = float(main_window.lineEdit.text())
    main_window.lineEdit.setText("")
    
def sub(): 
    global op , num_1
    op = "-"
    num_1 = float(main_window.lineEdit.text())
    main_window.lineEdit.setText("")

def mul():
    global op , num_1
    op = "*"
    num_1 = float(main_window.lineEdit.text())
    main_window.lineEdit.setText("")

def div():
    global op , num_1
    op = "/"
    num_1 = float(main_window.lineEdit.text())
    main_window.lineEdit.setText("")

def sin():
    num = float(main_window.lineEdit.text())
    main_window.lineEdit.setText(str(math.sin(num)))

def cos():
    num = float(main_window.lineEdit.text())
    main_window.lineEdit.setText(str(math.cos(num)))

def tan():
    num = float(main_window.lineEdit.text())
    main_window.lineEdit.setText(str(math.tan(num)))

def cot():
    num = float(main_window.lineEdit.text())
    main_window.lineEdit.setText(str(math.cos(math.radians(num) / math.sin(math.radians(num)))))

def pi():
    text = main_window.lineEdit.text()
    main_window.lineEdit.setText(text + "3.14")

def pow():
    text = float(main_window.lineEdit.text())
    text2 = text ** 2
    main_window.lineEdit.setText(str(text2))

def log():
    num = float(main_window.lineEdit.text())
    main_window.lineEdit.setText(str(math.log(num)))

def fuc():
    num = int(main_window.lineEdit.text())
    main_window.lineEdit.setText(str(math.factorial(num)))

def sqrt():
    num = float(main_window.lineEdit.text())
    main_window.lineEdit.setText(str(math.sqrt(num)))

def abs():
    num_1 = float(main_window.lineEdit.text())
    abc = num_1 * -1
    main_window.lineEdit.setText(str(abc))

def equal():
    if op == "+":
        eq_sum()
    elif op == "-":
        eq_sub()
    elif op == "*":
        eq_mul()
    elif op == "/":
        eq_div()
def eq_sum():
    num_2 = float(main_window.lineEdit.text())
    main_window.lineEdit.setText("")
    result = num_1 + num_2
    main_window.lineEdit.setText(str(result))
def eq_sub():
    num_2 = float(main_window.lineEdit.text())
    main_window.lineEdit.setText("")
    result = num_1 - num_2
    main_window.lineEdit.setText(str(result))

def eq_mul():
    num_2 = float(main_window.lineEdit.text())
    main_window.lineEdit.setText("")
    result = num_1 * num_2
    main_window.lineEdit.setText(str(result))

def eq_div():
    try:
        num_2 = float(main_window.lineEdit.text())
        main_window.lineEdit.setText("")
        result = num_1 / num_2
        main_window.lineEdit.setText(str(result))
    except:
        main_window.lineEdit.setText("you can not divition by zero!")

app = QApplication([])
loader = QUiLoader()

main_window = loader.load("cal.ui")
design()
main_window.show()

main_window.btn_c.clicked.connect(c)
main_window.btn_ac.clicked.connect(ac)
main_window.btn_0.clicked.connect(partial(num, "0"))
main_window.btn_1.clicked.connect(partial(num, "1"))
main_window.btn_2.clicked.connect(partial(num, "2"))
main_window.btn_3.clicked.connect(partial(num, "3"))
main_window.btn_4.clicked.connect(partial(num, "4"))
main_window.btn_5.clicked.connect(partial(num, "5"))
main_window.btn_6.clicked.connect(partial(num, "6"))
main_window.btn_7.clicked.connect(partial(num, "7"))
main_window.btn_8.clicked.connect(partial(num, "8"))
main_window.btn_9.clicked.connect(partial(num, "9"))
main_window.btn_sum.clicked.connect(sum)
main_window.btn_sub.clicked.connect(sub)
main_window.btn_mul.clicked.connect(mul)
main_window.btn_div.clicked.connect(div)
main_window.btn_sin.clicked.connect(sin)
main_window.btn_cos.clicked.connect(cos)
main_window.btn_log.clicked.connect(log)
main_window.btn_tan.clicked.connect(tan)
main_window.btn_pi.clicked.connect(pi)
main_window.btn_pow.clicked.connect(pow)
main_window.btn_sqrt.clicked.connect(sqrt)
main_window.btn_cot.clicked.connect(cot)
main_window.btn_abs.clicked.connect(abs)
main_window.btn_dot.clicked.connect(dot)
main_window.btn_fuc.clicked.connect(fuc)
main_window.btn_eq.clicked.connect(equal)

app.exec()
