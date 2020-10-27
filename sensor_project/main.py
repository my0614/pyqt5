
from sensor import *
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