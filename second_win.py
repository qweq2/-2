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
        self.txt_starttest1 = QPushButton(txt_starttest1)
        self.txt_hinttest1 = QLineEdit(txt_hinttest1)
        self.txt_test2 = QLabel(txt_test2)
        self.txt_starttest2 = QPushButton(txt_starttest2)
        self.txt_test3 = QLabel(txt_test3)
        self.txt_starttest3 = QPushButton(txt_starttest3)
        self.txt_hinttest2 = QLineEdit(txt_hinttest2)
        self.txt_hinttest3 = QLineEdit(txt_hinttest3)
        self.txt_sendresults = QPushButton(txt_sendresults)
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
        

class Experiment():
    def __init__(self, age, test1, test2, test3):
        self.age = age
        self.t1 = test1
        self.t2 = test2
        self.t3 = test3
    
    def next_click(self):
        self.hide()
        self.exp = Experiment(int(self.line_age.text()), self.line_test1.text(),
        self.line_test2.text(), self.line_test2.text())
        self.fw = FinalWin(self.exp)

    def connects(self):
        self.btn_next.clicked.connect(self.next_click)
        self.btn_test1.clicked.connect(self.timer_test)
        self.btn_test2.clicked.connect(self.timer_sits)
        self.btn_test3.clicked.connect(self.timer_final)


    def timer_test(self):
        global time 
        time = QTime(0,0,15)
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer1Event)
        self.timer.start(1000)
    
    def timer_sits(self):
        global time
        time = QTime(0,0,30)
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer2Event)
        self.timer.start(1500)

    def timer_final(self):
        global time
        time = QTime(0,1,0)
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer3Event)
        self.timer.start(1000)

    def timer1Event(self):
        global time
        time = time.addSecs(-1)
        self.text_timer.setText(time.toString("hh:mm:ss")[6:8])
        self.text_timer.setFont(QFont("Times",36, QFont.Bold))
        self.text_timer.setStyleSheet("color:rgb(0:0:0)")
        if time.toString("hh:mm:ss") == "00:00:00":
            self.timer.stop()

    def timer2Event(self):
        global time
        time = time.addSecs(-1)
        self.text_timer.setText(time.toString("hh:mm:ss")[6:8])
        self.text_timer.setStyleSheet("color:rgb(0:0:0)")
        self.text_timer.setFont(QFont("Times",36, QFont.Bold))
        if time.toString("hh:mm:ss") == "00:00:00":
            self.timer.stop()

    def timer3Event(self):
        global time
        time = time.addSecs(-1)
        self.text_timer.setText(time.toString("hh:mm:ss"))
        if int(time.toString("hh:mm:ss")[6:8]) >= 45:
            self.text_timer.setStyleSheet("color:rgb(0:255:0)")
        elif int(time.toString("hh:mm:ss")[6:8]) <= 15:
            self.text_timer.setStyleSheet("color:rgb(0:255:0)")
        else:
            self.text_timer.setStyleSheet("color:rgb(0:0:0)")
        self.text_timer.setFont(QFont("Times",36, QFont.Bold))
        if time.toString("hh:mm:ss") == "00:00:00":
            self.timer.stop


        




    def connects(self):
        self.txt_sendresults.clicked.connect(self.next_click)
        self.txt_starttest1.clicked.connect(self.timer_test)
    def next_click(self):
        self.hide()
        self.fw = FinWin()
