import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton
from PyQt5.QtGui import QPixmap, QPainter, QFontDatabase, QFont
from PyQt5.QtCore import Qt, QProcess
import pygame
from game import Game

import os
# Translate asset paths to useable format for PyInstaller
def resource_path(relative_path):
  if hasattr(sys, '_MEIPASS'):
      return os.path.join(sys._MEIPASS, relative_path)
  return os.path.join(os.path.abspath('.'), relative_path)



class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 1276, 654)
        self.setWindowTitle('mingol')

        #label obj
        titleLbl = QLabel('Mingle !!!! (from the squid game)', self)
        titleLbl.setGeometry(100, 170, 2000, 200)


        #button obj
        button = QPushButton('Play !', self)
        button.clicked.connect(self.on_button_click)
        button.setGeometry(550, 430, 150, 50)

        font_db = QFontDatabase()
        font_db.addApplicationFont(resource_path('./resources/game_of_squids/Game Of Squids.ttf'))

        titleLbl.setFont(QFont('Game of Squids', 36))
        titleLbl.setStyleSheet('color: white;')
        button.setFont(QFont('Game of Squids', 24))

        self.game = None

        self.show()

    def on_button_click(self):
        print('starting..')
        self.game = Game()
        self.game.show()


    def paintEvent(self, event):
        painter = QPainter(self)
        painter.drawPixmap(self.rect(), QPixmap(resource_path('./resources/background.JPG')))
    
stylesheet = """


    MyApp {
        font: 24pt 'Game of Squids';
        background-repeat: no-repeat; 
        background-position: center;
}
"""


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyleSheet(stylesheet)
    ex = MyApp()
    ex.resize(1276, 654)
    sys.exit(app.exec_())