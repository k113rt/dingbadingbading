import random
import time
import pygame
import tkinter as tk



class Game:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Audio Player")

        self.audio_file = './resources/Mingle Game Song Round and Round (Lyrics) Squid Game.mp3'


    def play_audio(self):
        if self.audio_file:
            pygame.init()
            pygame.mixer.init()
            pygame.mixer.music.load(self.audio_file)
            pygame.mixer.music.play()


    def stop_audio(self):
        pygame.mixer.music.stop()
    
if __name__ == "__main__":
        print("get ready to play")
        print("3...")
        time.sleep(1)
        print("2...")
        time.sleep(1)
        print("1...")
        time.sleep(1)
        print("GO")
        Game().play_audio()

        time.sleep(random.randint(33, 50))
        Game().stop_audio()
        print(random.randint(2, 5))
        

