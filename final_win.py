from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QGroupBox, QRadioButton, QPushButton, QLabel, QListWidget, QLineEdit
from instr import *
class FinWin(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.initUI()
        self.show()
    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width,win_height)
        self.move(win_x,win_y)
    def initUI(self):
        self.line = QVBoxLayout()
        self.txt_index = QLabel(txt_index)
        self.txt_workheart = QLabel(txt_workheart)
        self.line.addWidget(self.txt_index, alignment = Qt.AlignCenter)
        self.line.addWidget(self.txt_workheart, alignment = Qt.AlignCenter)
        self.setLayout(self.line)
