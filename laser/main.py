
from laser import *
from PyQt5 import QtCore, QtGui, QtWidgets
import pygame
import threading
import serial
import time
pygame.init()
pygame.mixer.init()


ser = serial.Serial(port='COM7',
                    baudrate=9600,
                    parity=serial.PARITY_NONE,
                    stopbits=serial.STOPBITS_ONE,
                    bytesize=serial.EIGHTBITS,
                    timeout=1)

def signals(self):
    cnt = 0
    
    
    
def laser(self):
    while True:
        ser_data = ser.readline()
        if(ser_data):
            print(ser_data)
            cnt = int(ser_data[0:1])
            if cnt == 1:
                self.color.setStyleSheet("background-color : red; border-radius : 50%;")
                self.label.setText("침입 감지")
                import pygame
                pygame.init()
                sounda = pygame.mixer.Sound('sound2.wav')
                sounda.play()

            elif cnt == 0:
                self.color.setStyleSheet("background-color : blue; border-radius : 50%;")
                self.label.setText("침입 감지 중")

            




Ui_MainWindow.signals = signals
Ui_MainWindow.laser = laser


if __name__=="__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.signals()
    th = threading.Thread(target = laser,args=(ui,))
    th.daemon = True
    th.start()
   
    MainWindow.show()
    sys.exit(app.exec_())
