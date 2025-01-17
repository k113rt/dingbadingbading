import sys
import random
import time
import pygame
import os
import tkinter as tk
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton
from PyQt5.QtGui import QPixmap, QPainter, QFontDatabase, QFont
from PyQt5.QtCore import Qt, QTimer


def resource_path(relative_path):
  if hasattr(sys, '_MEIPASS'):
      return os.path.join(sys._MEIPASS, relative_path)
  return os.path.join(os.path.abspath('.'), relative_path)

class AudioPlayer:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Audio Player")

        self.bading_mp3 = resource_path('./resources/Mingle Game Song Round and Round (Lyrics) Squid Game.mp3')
        self.tense_mp3 = resource_path('./resources/Persona 5 OST - Getaway Arrest.mp3')

    def play_bading(self):
        if self.bading_mp3:
            pygame.init()
            pygame.mixer.init()
            pygame.mixer.music.load(self.bading_mp3)
            pygame.mixer.music.play()
    
    def play_tense(self):
        if self.tense_mp3:
            pygame.init()
            pygame.mixer.init()
            pygame.mixer.music.load(self.tense_mp3)
            pygame.mixer.music.play()


    def stop_audio(self):
        pygame.mixer.music.stop()

    def is_init(self):
        return pygame.mixer.get_init()

class Game(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
       

    def initUI(self):
        self.setGeometry(300, 300, 1276, 654)
        self.setWindowTitle('mingol')

        #label obj
        self.titleLbl = QLabel('Get Ready to Play the game', self)
        self.startLbl = QLabel('3...', self)
        self.numberLbl = QLabel('', self)
        self.titleLbl.setGeometry(250, 400, 2000, 200)
        self.titleLbl.setFont(QFont('Game of Squids', 60))
        self.titleLbl.setStyleSheet('color: white;')
        self.startLbl.setGeometry(550, 450, 800, 200)
        self.startLbl.setFont(QFont('Game of Squids', 180))
        self.startLbl.setStyleSheet('color: white;')
        self.numberLbl.setGeometry(830, 350, 2000, 400)
        self.numberLbl.setFont(QFont('Game of Squids', 360))
        self.numberLbl.setStyleSheet('color: white;')

        self.startLbl.hide()
        self.numberLbl.hide()

        #exit button
        button = QPushButton('X', self)
        button.clicked.connect(self.exit_button)
        button.setGeometry(1870, 0, 50, 50)

        self.startBtn = QPushButton('play', self)
        self.startBtn.clicked.connect(self.countdown)
        self.startBtn.setFont(QFont('Game of Squids', 24))
        self.startBtn.setGeometry(800,800,300,100)

        #timer 
        self.timer = QTimer(self)
        self.timer_count = 0
        self.game_timer = QTimer(self)

        self.audio = AudioPlayer()

        font_db = QFontDatabase()
        font_db.addApplicationFont(resource_path('./resources/game_of_squids/Game Of Squids.ttf'))

        
        button.setFont(QFont('Game of Squids', 24))

        self.showFullScreen()

    def exit_button(self):
        app = QApplication.instance()
        app.quit()

    def change_label(self, text):
        self.startLbl.setText(text)
        self.timer_count += 1
        print("Timer {} finished".format(self.timer_count))

        next_text = '1...' if self.timer_count == 1 else 'Start!' if self.timer_count == 2 else None
        if next_text:
            self.timer.timeout.disconnect()
            self.timer.timeout.connect(lambda: self.change_label(next_text))
            self.timer.start(1000)
        else:
            self.timer.timeout.disconnect()
            self.timer.stop()
            self.game_start()
    

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.drawPixmap(self.rect(), QPixmap(resource_path('./resources/background.JPG')))
    
    def countdown(self):
        print('start')
        self.titleLbl.hide()
        self.numberLbl.hide()
        self.startBtn.hide()
       
        self.timer_count = 0

        if self.audio.is_init():
            self.audio.stop_audio()

        self.startLbl.setText('3...')
        self.startLbl.show()

        self.timer.timeout.connect(lambda: self.change_label('2...'))
        self.timer.start(1000)


    def game_start(self): ###please fixxxx i haate this
        """
        Start the game by playing music and setting a timer
        to stop the music after a random interval.
        """
        self.audio.play_bading()
        self.game_timer.timeout.connect(self.audio.stop_audio)
        self.game_timer.timeout.connect(self.showNumber)
        random_interval = random.randint(33000, 60000)
        self.game_timer.start(random_interval)
        
    
    def showNumber(self):
        self.game_timer.disconnect()
        self.startLbl.hide()
        self.numberLbl.setText(str(random.randint(2, 5)))
        self.numberLbl.show()
        self.startBtn.show()
        self.audio.play_tense()
    
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
    ex = Game()
    #ex.game_start()
    sys.exit(app.exec_())