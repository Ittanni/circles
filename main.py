from PyQt5 import uic  # Импортируем uic
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
import random
from PyQt5.QtWidgets import QWidget, QPushButton
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtCore import Qt


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.pushButton.clicked.connect(self.addDot)
        self.dots = []

    def addDot(self):
        x = random.randint(10, 400)
        y = random.randint(10, 220)
        size = random.randint(10, 200)
        self.dots.append((x, y, size))
        self.update()

    def paintEvent(self, e):
        qp = QPainter()
        qp.begin(self)
        self.drawDots(qp)
        qp.end()

    def drawDots(self, qp):
        qp.setBrush(QColor("yellow"))
        for dot in self.dots:
            qp.drawEllipse(dot[0], dot[1], dot[2], dot[2])


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())