from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QLable, QApplication,QPushButton,QVBoxLayout,QHBoxLayout,QLineEdit
from instr import *
txt_title = "Тест Руфле"
win_width,win_height = 1000,600
win_x,win_y = 200,200
class TestWin(QtWidget):
    def __init__(self):
        super()__init__()
        self.set_appear()
        self.initUI()
        self.connects()
        self.show()
    def set_appear(self):
        self.setWindowTitle(set_text)
        self.resize(win_width,win_height)
        self.move(win_x,win_y)
    def initUI(self):
        self.txt_title = QLable(txt_title)
        self.txt_name = QLable(txt_name)
        self.txt_hintname = QLineEdit(hintname)
        self.txt_age = QLable(txt_age)
        self.txt_hintage = QLineEdit(hintage)
        self.txt_test1 = QLable(txt_test1)
        self.txt_starttest1 = QPushButton(txt_starttest1)
        self.txt_hinttest1 = QLineEdit(hinttest1)
        self.txt_test2 = QLable(txt_test2)
        self.txt_starttest2 = QPushButton(txt_starttest2)
        self.txt_test3 = QLable(txt_test3)
        self.txt_starttest3 = QPushButton(txt_starttest3)
        self.txt_hinttest2 = QLineEdit(hinttest2)
        self.txt_hinttest3 = QLineEdit(hinttest3)
        self.txt_sendresults = QPushButton(txt_sendresults)
        self.txt_timer = QLable(txt_timer)
        self.h_line = QHBoxLayout()
        self.r_line = QVBoxLayout()
        self.l_line = QVBoxLayout()
        self.l_line.addWidget(self.txt_name)
        self.l_line.addWidget(self.txt_hintname)
        self.l_line.addWidget(self.txt_age)
        self.l_line.addWidget(self.txt_hintage)
        self.l_line.addWidget(self.txt_test1)
        self.l_line.addWidget(self.txt_starttest1)
        self.l_line.addWidget(self.txt_hinttest1)
        self.l_line.addWidget(self.txt_test2)
        self.l_line.addWidget(self.txt_starttest2)
        self.l_line.addWidget(self.txt_test3)
        self.l_line.addWidget(self.txt_starttest3)
        self.l_line.addWidget(self.txt_hinttest2)
        self.l_line.addwidget(self.txt_hinttest3)
        self.h_line.addWidget(self.txt_sendresults)
        self.r_line.addWidget(self.txt_timer)
    def connects(self):
        self.bnt_next.clicked.connect(self.next_click)
    def next_click(self):
        self.hide()
        self.fw = FinWin()