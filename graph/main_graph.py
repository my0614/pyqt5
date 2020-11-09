from graph import *
import serial
import threading
from threading import Thread
import time


ser = serial.Serial(port='COM5',
                    baudrate=9600,
                    parity=serial.PARITY_NONE,
                    stopbits=serial.STOPBITS_ONE,
                    bytesize=serial.EIGHTBITS,
                    timeout=1)

def signals(self):
    

            
def dht11(ui):
    while True:
        ser_data = str(ser.readline())
        print("success")
        print(ser_data)
            
        ui.temp.setText(ser_data[3:6] + "°C") 
        ui.humi.setText(ser_data[6:8] + "%")
        time.sleep(3)  
    
    



Ui_MainWindow.signals = signals

Ui_MainWindow.dht11 = dht11


if __name__=="__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.signals()
    th = threading.Thread(target = dht11,args=(ui,))
    th.daemon = True
    th.start()
    MainWindow.show()
    
    sys.exit(app.exec_())