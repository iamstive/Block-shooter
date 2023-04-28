from PyQt5.QtWidgets import * 
from PyQt5 import QtCore
from PyQt5.QtGui import * 
import sys
import New_game

class Menu(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        show = True
        self.widget = QWidget()
        self.setGeometry(300, 300, 600, 600)
        self.setWindowTitle('Menu')
        self.setWindowIcon(QIcon('web.png'))
        self.setStyleSheet("background-color: black;")
        btn = QPushButton(self.widget)
        btn.setText("Play")
        btn.move(150, 150)
        btn.clicked.connect(self.btn_connected)
        if show == True:
            self.widget.show()
            show = False
        #self.show()

    def btn_connected(self):
        New_game.start()
        print("Game")



app = QApplication(sys.argv)
win = Menu()
sys.exit(app.exec_())

