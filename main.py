import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPainter, QBrush, QPen
from PyQt5.QtCore import Qt
from random import randint


class Main(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("UI.ui", self)
        self.initUI()

    def initUI(self):
        self.flag = False
        self.s1 = 1
        self.s2 = 100000
        self.s3 = 100000
        self.btn.clicked.connect(self.start)

    def start(self):
        self.flag = True

    def paintEvent(self, event):
            painter = QPainter(self)
            painter.setPen(QPen(Qt.red, 8))
            painter.setBrush(QBrush(Qt.yellow))
            if self.flag:
                self.s1 = randint(10, 50)
                self.s2 = randint(1, 400)
                self.s3 = randint(1, 300)
                self.flag = False
            painter.drawEllipse(self.s2, self.s3, self.s1, self.s1)
            painter.end()
            self.update()


if __name__ == '__main__':
    sa = QApplication(sys.argv)
    sx = Main()
    sx.show()
    sys.exit(sa.exec())
