import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPainter, QColor
from UI import Ui_Form
from random import randint

MAX_R = 250


class MyWidget(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Случайные круги")
        self.do_paint = False
        self.btn.clicked.connect(self.click)

    def click(self):
        self.do_paint = True
        self.repaint()

    def randomColor(self):
        return randint(0, 2 ** 24 - 1)

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            qp.setBrush(QColor(self.randomColor()))
            self.draw(qp)
            qp.end()

    def draw(self, qp):
        d = randint(10, MAX_R) * 2
        x = randint(0, self.size().width() - d)
        y = randint(0, self.size().height() - d)
        qp.drawEllipse(x, y, d, d)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())
