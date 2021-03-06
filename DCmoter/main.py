from motor import *
import serial

LEFT_STATE=1
RIGHT_STATE=1
FORWARD_STATE=1
BACK_STATE=1
UP_STATE = 1
DOWN_STATE=1
STOP_STATE =1

ser = serial.Serial(port='COM4',
                    baudrate=9600,
                    parity=serial.PARITY_NONE,
                    stopbits=serial.STOPBITS_ONE,
                    bytesize=serial.EIGHTBITS,
                    timeout=1)

def signals(self):
    self.LEFT.clicked.connect(self.bt_LEFT)
    self.RIGHT.clicked.connect(self.bt_RiGHT)
    self.FORWARD.clicked.connect(self.bt_FORWARD)
    self.BACK.clicked.connect(self.bt_BACK)
    self.speedup.clicked.connect(self.bt_UP)
    self.speeddown.clicked.connect(self.bt_DOWN)
    self.STOP.clicked.connect(self.bt_STOP)

def bt_LEFT(self):
    global LEFT_STATE
    if(LEFT_STATE):
        message = ''.join(['\x02','L', 'E', 'F', 'T', '\x03'])
        ser.write(bytes(message.encode()))
        EFT_STATE = 0
    else:
        message = ''.join(['\x02','L', 'E', 'F', 'T', '\x03'])
        ser.write(bytes(message.encode()))
        LEFT_STATE = 1    

def bt_RiGHT(self):
    global RIGHT_STATE
    if(RIGHT_STATE):
        message = ''.join(['\x02','R', 'I', 'G', 'H', 'T','\x03'])
        ser.write(bytes(message.encode()))
        RIGHT_STATE = 0
    else:
        message = ''.join(['\x02','R', 'I', 'G', 'H','T', '\x03'])
        ser.write(bytes(message.encode()))
        RIGHT_STATE = 1


def bt_FORWARD(self):
    global FORWARD_STATE
    if(FORWARD_STATE):
        message = ''.join(['\x02','F', 'O', 'R', 'W', 'A', 'R','D','\x03'])
        ser.write(bytes(message.encode()))
        FORWARD_STATE = 0
    else:
        message = ''.join(['\x02','F', 'O', 'R', 'W','A','R','D', '\x03'])
        ser.write(bytes(message.encode()))
        FORWARD_STATE = 1

def bt_BACK(self):
    global BACK_STATE
    if(BACK_STATE):
        message = ''.join(['\x02','B', 'A', 'C', 'K', '\x03'])
        ser.write(bytes(message.encode()))
        BACK_STATE = 0
    else:
        message = ''.join(['\x02','B', 'A', 'C', 'K', '\x03'])
        ser.write(bytes(message.encode()))
        BACK_STATE = 1

def bt_UP(self):
    global UP_STATE
    if(UP_STATE):
        message = ''.join(['\x02','U', 'P', '\x03'])
        ser.write(bytes(message.encode()))
        UP_STATE = 0
    else:
        message = ''.join(['\x02','U', 'P', '\x03'])
        ser.write(bytes(message.encode()))
        UP_STATE = 1

def bt_DOWN(self):
    global DOWN_STATE
    if(DOWN_STATE):
        message = ''.join(['\x02','D', 'O', 'W','N','\x03'])
        ser.write(bytes(message.encode()))
        DOWN_STATE = 0
    else:
        message = ''.join(['\x02','D', 'O', 'W','N','\x03'])
        ser.write(bytes(message.encode()))
        DOWN_STATE = 1

def bt_STOP(self):
    global STOP_STATE
    if(STOP_STATE):
        message = ''.join(['\x02','S', 'T', 'O','P','\x03'])
        ser.write(bytes(message.encode()))
        STOP_STATE = 0
    else:
        message = ''.join(['\x02','S', 'T', 'O','P','\x03'])
        ser.write(bytes(message.encode()))
        STOP_STATE = 1
  
Ui_MainWindow.signals = signals
Ui_MainWindow.bt_LEFT = bt_LEFT
Ui_MainWindow.bt_RiGHT = bt_RiGHT
Ui_MainWindow.bt_FORWARD = bt_FORWARD
Ui_MainWindow.bt_BACK = bt_BACK
Ui_MainWindow.bt_UP = bt_UP
Ui_MainWindow.bt_DOWN = bt_DOWN
Ui_MainWindow.bt_STOP = bt_STOP

if __name__=="__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.signals()
    MainWindow.show()
    sys.exit(app.exec_())