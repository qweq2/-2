from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QLable, QApplication,QPushButton,QVBoxLayout,QHBoxLayout,QLineEdit
from instr import *
class MainWin(QWidget):
    def __init__(self):
        super().__init__
        self.set_appear()
        self.initUI()
        self.connects()
        self.show()
    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width,win_height)
        self.move(win_x,win_y)
    def initUI():
        self.hello_text = QLable(txt_hello)
        self.instruction = QLable(txt_instruction)
        self.button = QPushButton(txt_next)
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.hello_text)
        self.layout.addWidget(self.instruction)
        self.layout.addWidget(self.button)
    def connects(self):
        self.btn_next.clicked.connect(self.next_click)
    def next_click(self):
        self.hide
        self.tw = TestWin()