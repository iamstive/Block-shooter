import os
import sys
import New_game
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtGui import QPalette, QBrush, QPixmap
from PyQt5.QtGui import QPalette
from PyQt5.QtGui import QFont
from PyQt5.QtCore import pyqtSlot
from screeninfo import get_monitors



class App(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'Menu'
        self.left = 760
        self.top = 200
        self.width = 800
        self.height = 600
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        palette = QPalette()
        palette.setBrush(QPalette.Background, QBrush(QPixmap("back.png")))
        self.setPalette(palette)
        
        #: start button
        button = QPushButton('Start', self)
        button.setFont(QFont('Arial', 40))
        button.setStyleSheet("#MainWindow{border-image:url(CR0.png)}")
        button.setStyleSheet("background-color: rgba(255, 255, 255, 75);\n""border: rgba(255, 255, 255, 100);")
        button.setToolTip('This is an example button')
        button.resize(200, 50)
        button.move(300,150)
        button.clicked.connect(self.start)
        
        #: map button
        button1 = QPushButton('Map', self)
        button1.setFont(QFont('Arial', 40))
        button1.setStyleSheet("#MainWindow{border-image:url(CR0.png)}")
        button1.setStyleSheet("background-color: rgba(255, 255, 255, 75);\n""border: rgba(255, 255, 255, 100);")
        button1.setToolTip('This is an example button')
        button1.resize(200, 50)
        button1.move(300,212.5)
        button1.clicked.connect(self.map)

        #: shop button
        button2 = QPushButton('Shop', self)
        button2.setFont(QFont('Arial', 40))
        button2.setStyleSheet("#MainWindow{border-image:url(CR0.png)}")
        button2.setStyleSheet("background-color: rgba(255, 255, 255, 75);\n""border: rgba(255, 255, 255, 100);")
        button2.setToolTip('This is an example button')
        button2.resize(200, 50)
        button2.move(300,275)
        button2.clicked.connect(self.shop)
        
        # special button
        button3 = QPushButton('Special', self)
        button3.setFont(QFont('Arial', 40))
        button3.setStyleSheet("#MainWindow{border-image:url(CR0.png)}")
        button3.setStyleSheet("background-color: rgba(255, 255, 255, 75);\n""border: rgba(255, 255, 255, 100);")
        button3.setToolTip('This is an example button')
        button3.resize(200, 50)
        button3.move(300,337.5)
        button3.clicked.connect(self.special)

        #: special button 2
        button4 = QPushButton('Exit', self)
        button4.setFont(QFont('Arial', 40))
        button4.setStyleSheet("#MainWindow{border-image:url(CR0.png)}")
        button4.setStyleSheet("background-color: rgba(255, 255, 255, 75);\n""border: rgba(255, 255, 255, 100);")
        button4.setToolTip('This is an example button')
        button4.resize(200, 50)
        button4.move(300,400)
        button4.clicked.connect(self.special2)

        self.show()


    @pyqtSlot()
    def start(self):
        New_game.start()

    
    @pyqtSlot()
    def map(self):
        print(os.getpid())
    
    @pyqtSlot()
    def shop(self):
        print(get_monitors())

    @pyqtSlot()
    def special(self):
        print(get_monitors())
    
    @pyqtSlot()
    def special2(self):
        sys.exit()
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())