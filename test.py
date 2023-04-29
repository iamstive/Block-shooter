import os
import sys
import MainEngine
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtGui import QPalette, QBrush, QPixmap
from PyQt5.QtGui import QPalette
from PyQt5.QtGui import QFont
from PyQt5.QtCore import pyqtSlot
import threading


class App(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'Cold Road Alpha 0.1'
        self.left = 760
        self.top = 200
        self.width = 800
        self.height = 600
        self.initUI()

    def initUI(self):

        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.palette = QPalette()
        self.palette.setBrush(QPalette.Background, QBrush(QPixmap("CR0.1.png")))
        self.setPalette(self.palette)

        #: start button
        self.button = QPushButton('Start', self)
        self.button.setFont(QFont('Arial', 40))
        self.button.setStyleSheet("#MainWindow{border-image:url(CR0.png)}")
        self.button.setStyleSheet("background-color: rgba(255, 255, 255, 75);\n""border: rgba(255, 255, 255, 100);")
        self.button.setToolTip('This is an example button')
        self.button.resize(200, 50)
        self.button.move(300, 150)
        self.button.clicked.connect(self.start)

        #: map button
        self.button1 = QPushButton('Map', self)
        self.button1.setFont(QFont('Arial', 40))
        self.button1.setStyleSheet("#MainWindow{border-image:url(CR0.png)}")
        self.button1.setStyleSheet("background-color: rgba(255, 255, 255, 75);\n""border: rgba(255, 255, 255, 100);")
        self.button1.setToolTip('This is an example button')
        self.button1.resize(200, 50)
        self.button1.move(300, 212)
        self.button1.clicked.connect(self.map)

        #: shop button
        self.button2 = QPushButton('Shop', self)
        self.button2.setFont(QFont('Arial', 40))
        self.button2.setStyleSheet("#MainWindow{border-image:url(CR0.png)}")
        self.button2.setStyleSheet("background-color: rgba(255, 255, 255, 75);\n""border: rgba(255, 255, 255, 100);")
        self.button2.setToolTip('This is an example button')
        self.button2.resize(200, 50)
        self.button2.move(300, 275)
        self.button2.clicked.connect(self.shop)

        # special button
        self.button3 = QPushButton('Special', self)
        self.button3.setFont(QFont('Arial', 40))
        self.button3.setStyleSheet("#MainWindow{border-image:url(CR0.png)}")
        self.button3.setStyleSheet("background-color: rgba(255, 255, 255, 75);\n""border: rgba(255, 255, 255, 100);")
        self.button3.setToolTip('This is an example button')
        self.button3.resize(200, 50)
        self.button3.move(300, 337)
        self.button3.clicked.connect(self.special)

        #: special button 2
        self.button4 = QPushButton('Exit', self)
        self.button4.setFont(QFont('Arial', 40))
        self.button4.setStyleSheet("#MainWindow{border-image:url(CR0.png)}")
        self.button4.setStyleSheet("background-color: rgba(255, 255, 255, 75);\n""border: rgba(255, 255, 255, 100);")
        self.button4.setToolTip('This is an example button')
        self.button4.resize(200, 50)
        self.button4.move(300, 400)
        self.button4.clicked.connect(self.special2)

        self.show()

    @pyqtSlot()
    def start(self):
        self.palette.setBrush(QPalette.Background, QBrush(QPixmap("cro1.png")))
        self.setPalette(self.palette)
        launch = threading.Timer(1, self.game)
        launch.start()

    @pyqtSlot()
    def map(self):
        print(os.getpid())

    @pyqtSlot()
    def shop(self):
        print('MAGAZIN')

    @pyqtSlot()
    def special(self):
        print('WHAAAT')

    @pyqtSlot()
    def special2(self):
        sys.exit()

    def game(self):
        os.system("python MainEngine.py 1")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
