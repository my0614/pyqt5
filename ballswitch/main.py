
from ballswitch import *
from PyQt5 import QtCore, QtGui, QtWidgets
import pyqtgraph as pg
import threading
import serial
import time


ser = serial.Serial(port='COM7',
                    baudrate=9600,
                    parity=serial.PARITY_NONE,
                    stopbits=serial.STOPBITS_ONE,
                    bytesize=serial.EIGHTBITS,
                    timeout=1)

def signals(self):
    cnt = 0
    cnt2 = 0
    
    
def ballsensor(self):
    while True:
        ser_data = ser.readline()
        if(ser_data):
            print("success")
            print(ser_data)
            cnt = int(ser_data[0:2]) # 슬라이싱한값을 int로 바로 변환
            print(cnt)
            self.label_2.setText(str(cnt))
            cnt2 = int(ser_data[2:4])
            print(cnt2)
            self.label_4.setText(str(cnt2))




Ui_MainWindow.signals = signals
Ui_MainWindow.ballsensor = ballsensor


if __name__=="__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.signals()
    th = threading.Thread(target = ballsensor,args=(ui,))
    th.daemon = True
    th.start()
   
    MainWindow.show()
    sys.exit(app.exec_())
