from PyQt5.QtWidgets import QWidget, QPushButton, QApplication
from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5 import uic
from random import randint
import sys


class MainWindow(QWidget):

    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.isClicked = 0
        self.initUI()

    def initUI(self):
        self.btn.clicked.connect(self.make_circle)

    def paintEvent(self, event):
        if self.isClicked:
            qp = QPainter()
            qp.begin(self)
            r = randint(10, 300)
            qp.setPen(QPen(QColor(255, 255, 0), 2))
            qp.drawEllipse(randint(100, 540), randint(100, 380), r, r)
            qp.end()

    def make_circle(self):
        self.isClicked = 1
        self.update()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec_())
