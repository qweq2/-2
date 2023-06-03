from PyQt5.QtCore import Qt , QTime , QTimer
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QGroupBox, QRadioButton, QPushButton, QLabel, QListWidget, QLineEdit
from instr import *
from final_win import *
class TestWin(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.initUI()
        self.connects()
        self.show()
    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width,win_height)
        self.move(win_x,win_y)
    def initUI(self):
        self.txt_title = QLabel(txt_title)
        self.txt_name = QLabel(txt_name)
        self.txt_hintname = QLineEdit(txt_hintname)
        self.txt_age = QLabel(txt_age)
        self.txt_hintage = QLineEdit(txt_hintage)
        self.txt_test1 = QLabel(txt_test1)
        self.btn_starttest1 = QPushButton(txt_starttest1)
        self.txt_hinttest1 = QLineEdit(txt_hinttest1)
        self.txt_test2 = QLabel(txt_test2)
        self.btn_starttest2 = QPushButton(txt_starttest2)
        self.txt_test3 = QLabel(txt_test3)
        self.btn_starttest3 = QPushButton(txt_starttest3)
        self.txt_hinttest2 = QLineEdit(txt_hinttest2)
        self.txt_hinttest3 = QLineEdit(txt_hinttest3)
        self.btn_sendresults = QPushButton(txt_sendresults)
        self.txt_timer = QLabel(txt_timer)
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
        self.l_line.addWidget(self.txt_hinttest3)
        self.l_line.addWidget(self.txt_sendresults,alignment = Qt.AlignCenter)
        self.h_line.addWidget(self.txt_timer)
        self.h_line.addLayout(self.l_line)
        self.h_line.addLayout(self.r_line)
        self.setLayout(self.h_line)
        
    def timer_test(self):
        time = QTime(0,1,0)
        self.timer.timeout.connect(self.timerEvent)
        self.timer.start(1000)
    def timerEvent(self):


    def connects(self):
        self.btn_sendresults.clicked.connect(self.next_click)
        self.btn_starttest1.clicked.connect(self.timer_test)
    def next_click(self):
        self.hide()
        self.fw = FinWin()
