import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPainter, QBrush, QPen, QColor
from PyQt5 import QtCore, QtWidgets
from random import randint
from UI import Ui_Form


class Main(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initUI()

    def initUI(self):
        self.flag = False
        self.s1 = 1
        self.s2 = 100000
        self.s3 = 100000
        self.sq = QColor(randint(0, 255), randint(0, 255), randint(0, 255))
        self.btn.clicked.connect(self.start)

    def start(self):
        self.flag = True

    def paintEvent(self, event):
            painter = QPainter(self)
            if self.flag:
                self.s1 = randint(10, 50)
                self.s2 = randint(1, 400)
                self.s3 = randint(1, 300)
                self.sq = QColor(randint(0, 255), randint(0, 255), randint(0, 255))
                self.flag = False
            painter.setPen(QPen(self.sq, 8))
            painter.setBrush(QBrush(self.sq))
            painter.drawEllipse(self.s2, self.s3, self.s1, self.s1)
            painter.end()
            self.update()


if __name__ == '__main__':
    sa = QApplication(sys.argv)
    sx = Main()
    sx.show()
    sys.exit(sa.exec())
