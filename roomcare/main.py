from roomcare import *
import serial

L1_State=0
L2_State=0
L3_State=0

ser = serial.Serial(port='COM4',
                    baudrate=9600,
                    parity=serial.PARITY_NONE,
                    stopbits=serial.STOPBITS_ONE,
                    bytesize=serial.EIGHTBITS,
                    timeout=1)

def signals(self):
    self.LED1.clicked.connect(self.LED1_control)
    self.LED2.clicked.connect(self.LED2_control)
    self.LED3.clicked.connect(self.LED3_control)

def LED1_control(self):
    global L1_State
    if(L1_State):
        message = ''.join(['\x02','l', 'i', 'v', 'i', 'n','g', 'n','\x03'])
        ser.write(bytes(message.encode()))
        L1_State = 0
    else:
        message = ''.join(['\x02','l', 'i', 'v', 'i', 'n','g','f', '\x03'])
        ser.write(bytes(message.encode()))
        L1_State = 1

def LED2_control(self):
    global L2_State
    if(L2_State):
        message = ''.join(['\x02','b', 'a', 't', 'h', 'n', '\x03'])
        ser.write(bytes(message.encode()))
        L2_State = 0
    else:
        message = ''.join(['\x02','b', 'a', 't', 'h', 'f', '\x03'])
        ser.write(bytes(message.encode()))
        L2_State = 1

def LED3_control(self):
    global L3_State
    if(L3_State):
        message = ''.join(['\x02','k', 'i', 't', 'c', 'h','e','n', '\x03'])
        ser.write(bytes(message.encode()))
        L3_State = 0
    else:
        message = ''.join(['\x02','k', 'i', 't', 'c', 'h','e','f', '\x03'])
        ser.write(bytes(message.encode()))
        L3_State = 1
Ui_MainWindow.signals = signals
Ui_MainWindow.LED1_control = LED1_control
Ui_MainWindow.LED2_control = LED2_control
Ui_MainWindow.LED3_control = LED3_control

if __name__=="__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.signals()
    MainWindow.show()
    sys.exit(app.exec_())