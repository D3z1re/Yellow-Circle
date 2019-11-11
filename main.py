from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPainter, QColor, QPen
from UI import Ui_Form
from random import randint
import sys


class MainWindow(QWidget, Ui_Form):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.isClicked = 0
        self.initUI()

    def initUI(self):
        self.btn.clicked.connect(self.make_circle)

    def paintEvent(self, event):
        if self.isClicked:
            qp = QPainter()
            qp.begin(self)
            r = randint(10, 300)
            qp.setPen(QPen(QColor(randint(0, 255), randint(0, 255), randint(0, 255)), 2))
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
