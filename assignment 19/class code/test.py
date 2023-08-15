from functools import partial
from PySide6.QtWidgets import QApplication
from PySide6.QtUiTools import QUiLoader
def ans():
    main_window.label.label_display.set_Text()
    try:
        answer = eval()
        main_window.label.label_display.set_Text(str(answer))
    except:
        main_window.label.label_display.set_Text("wrang input!")
def num(x):
    text = main_window.label_display.text()
    if text == "0" or text == "wrang input!":pass
    new_text = text + x
    main_window.label_display.set_Text(new_text)
def ac():
    main_window.label.label_display.set_Text("")
def c():
    t = main_window.label_display.text()
    new_t = t[:-1]
    main_window.label_display.set_Text(new_t)


app = QApplication([])
loader = QUiLoader()

main_window = loader.load("PATH.ui")
main_window.show()

main_window.btn_c.clicked.connect(c)
main_window.btn_plus.clicked.connect()
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


app.exec()
