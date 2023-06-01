from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QLable, QApplication,QPushButton,QVBoxLayout,QHBoxLayout,QLineEdit
from instr import *
class FinWin():
    def __init__(self):
        super()__init__()
        self.set_appear()
        self.initUI()
        self.show()
    def set_appear(self):
        self.setWindowTitle(set_text)
        self.resize(win_width,win_height)
        self.move(win_x,win_y)
    def initUI(self):
        self.index = QLable(txt_index)
        self.result = QLable(txt_results)
        self.finlayout = QVBoxLayout()
        self.finlayout.addWidget(self.index)
        self.finlayout.addWidget(self.result)