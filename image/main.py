from image import *
import pygame
pygame.init()
pygame.mixer.init()


def cat_wav(self):
    import pygame
    pygame.init()
    pygame.mixer.init()
    sounda = pygame.mixer.Sound('Cat.wav')
    sounda.play()
def wolf_wav(self):
    import pygame
    pygame.init()
    pygame.mixer.init()
    soundb = pygame.mixer.Sound('Wolf howl sound effect.wav')
    soundb.play()


def event(self):
    self.wolf.clicked.connect(self.wolf_wav)
    self.cat.clicked.connect(self.cat_wav)
    


Ui_MainWindow.event = event
Ui_MainWindow.cat_wav = cat_wav
Ui_MainWindow.wolf_wav = wolf_wav


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.event()
    MainWindow.show()
    sys.exit(app.exec_())