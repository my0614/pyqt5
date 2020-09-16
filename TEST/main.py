from test import *
import serial



ser = serial.Serial(port='COM5',
                    baudrate=9600,
                    parity=serial.PARITY_NONE,
                    stopbits=serial.STOPBITS_ONE,
                    bytesize=serial.EIGHTBITS,
                    timeout=1)

def signals(self):
    self.pushButton.clicked.connect(self.button)
    

def button(self):
    global button
    value = self.input.toPlainText()
    print(value)
    if(button):
        message = ''.join(['\x02',value[0], value[1], value[2], '\x03'])
        ser.write(bytes(message.encode()))
        




Ui_MainWindow.signals = signals  
Ui_MainWindow.button = button


if __name__=="__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.signals()
    MainWindow.show()
    sys.exit(app.exec_())
