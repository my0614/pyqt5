from roomcare import *
import serial
import threading

L1_State=0
L2_State=0
L3_State=0

ser = serial.Serial(port='COM5',
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
        message = ''.join(['\x02','L', 'I', 'V', 'I', 'N','G', 'N','\x03'])
        ser.write(bytes(message.encode()))
        self.LED1.setText("ON")
        self.LED1.move(122,180)
        self.LED1.setStyleSheet("background-color : rgb(112,173,71); border-radius :15px;color : white; font: 87 16pt;font-weight : bold;")
        L1_State = 0
        
    else:
        message = ''.join(['\x02','L', 'I', 'V', 'I', 'N','G','F', '\x03'])
        ser.write(bytes(message.encode()))
        self.LED1.setText("OFF")
        self.LED1.move(122,360)
        self.LED1.setStyleSheet("background-color : red; border-radius :15px;color : white; font: 87 16pt; font-weight : bold;")
        L1_State = 1

def LED2_control(self):
    global L2_State
    if(L2_State):
        message = ''.join(['\x02','B', 'A', 'T', 'H', 'N', '\x03'])
        ser.write(bytes(message.encode()))
        self.LED2.setText("ON")
        self.LED2.setStyleSheet("background-color : rgb(112,173,71); border-radius :15px;color : white; font: 87 16pt;font-weight : bold;")
        self.LED2.move(338,180)
        L2_State = 0
    else:
        message = ''.join(['\x02','B', 'A', 'T', 'H', 'F', '\x03'])
        ser.write(bytes(message.encode()))
        self.LED2.setText("OFF")
        self.LED2.move(338,360)
        self.LED2.setStyleSheet("background-color : red; border-radius :15px;color : white; font: 87 16pt; font-weight : bold;")
        L2_State = 1

def dht11(self):
    global dht11
    for i in range(5):
        ser.read(bytes(dht11[i].encode()))

    print(dht11[i])



def LED3_control(self):
    global L3_State
    if(L3_State):
        message = ''.join(['\x02','K', 'I', 'T', 'C', 'H','E','N', '\x03'])
        ser.write(bytes(message.encode()))
        self.LED3.setText("ON")
        self.LED3.move(558,180)
        self.LED3.setStyleSheet("background-color : rgb(112,173,71); border-radius :15px;color : white; font: 87 16pt;font-weight : bold;")
        L3_State = 0
    else:
        message = ''.join(['\x02','K', 'I', 'T', 'C', 'H','E','F', '\x03'])
        ser.write(bytes(message.encode()))
        self.LED3.setText("OFF")
        self.LED3.setStyleSheet("background-color : red; border-radius :15px;color : white; font: 87 16pt; font-weight : bold;")
        self.LED3.move(558,360)
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