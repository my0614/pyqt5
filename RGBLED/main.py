from rgb import *
import serial
import threading
from threading import Thread
import time

red = []
green = []
blue = []

ser = serial.Serial(port='COM7',
                    baudrate=9600,
                    parity=serial.PARITY_NONE,
                    stopbits=serial.STOPBITS_ONE,
                    bytesize=serial.EIGHTBITS,
                    timeout=1)

def signals(self):
    print("rgb start")
    self.pushButton.clicked.connect(self.rgb_led)
    

def rgb_led(self):
    
    red = self.red_text.toPlainText()
    blue =  self.green_text.toPlainText()
    green = self.blue_text.toPlainText()
        
    print(red + blue + green)
    message = ''.join(['\x02',red,green,blue,'\x03'])
    ser.write(bytes(message.encode())) # 값 보내기

Ui_MainWindow.signals = signals
Ui_MainWindow.rgb_led = rgb_led

if __name__=="__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.signals()
    th = threading.Thread(target = signals,args=(ui,))
    th.daemon = True
    th.start()
    MainWindow.show()
    sys.exit(app.exec_())