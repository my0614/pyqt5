from PyQt5 import QtCore, QtGui, QtWidgets
from serial1 import *
import sys
import serial
import asyncio
import serial_asyncio
from threading import Thread

class UartCom():
    connect_port=[]
    def __init__(self, app):  

        self.app=app

        self.get_com()
        app.connect.clicked.connect(self.connect_serial)
        app.send.clicked.connect(self.sendUart)

        self.uart =None

    def get_com(self):
        if sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
            self.isLinux = True
        else:
            self.isLinux = False

        COM_Ports=self.serial_ports()   
        for port in COM_Ports:
            if port.find('COM') > -1:
                self.connect_port.append(port)
        print (self.connect_port)   
        for comport in self.connect_port:
            app.port_number.addItem(comport)
    def run(self, loop):
        try:
            loop.run_forever()
        except KeyboardInterrupt:
            pass
            print("Closed Uart trhead!")

    def connect_serial(self, text):
        self.loop = asyncio.new_event_loop()
        asyncio.set_event_loop(self.loop)

        com_no = str(app.port_number.currentText())
        print (com_no)

        if self.isLinux:
            self.coro = serial_asyncio.create_serial_connection(self.loop, lambda: UartProtocol(self.app), self.mcuPort, baudrate=115200)
            print('Connected mcu port = '+self.mcuPort)
        else:
            print('com connect')
            self.coro = serial_asyncio.create_serial_connection(self.loop, lambda: UartProtocol(self), com_no, baudrate=115200)
        self.loop.run_until_complete(self.coro)

        t = Thread(target=self.run, args=(self.loop,))
        t.start()

            #self.loop.call_soon_threadsafe(asyncio.async , self.coro)
        pass
    def serial_ports(self):  
        if sys.platform.startswith('win'):   
            ports = ['COM%s' % (i + 1) for i in range(256)]   
        elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):   
            # this excludes your current terminal "/dev/tty"   
            ports = glob.glob('/dev/tty[A-Za-z]*')   
        elif sys.platform.startswith('darwin'):   
            ports = glob.glob('/dev/tty.*')   
        else:   
            raise EnvironmentError('Unsupported platform')   
        result = []   
        for port in ports:   
            try:   
                s = serial.Serial(port)   
                s.close()   
                result.append(port)   
            except (OSError, serial.SerialException):  
                pass
        return result

    def printLog(self, msg):
            print('<{!r}> {!r}'.format(self.getTimeStamp(), msg))

    def sendUart(self):
            msg=app.lineEdit.text()
            if self.uart != None:
                print (msg)
                #message = ''.join(['\x02',msg,'\x03'])
                self.uart.write(msg.encode()) 
                #print(bytes(message.encode()))       
                print ('Finished Send')
            else : 
                print ('Not Connected')

class UartProtocol(asyncio.Protocol):
    def __init__(self, app):
        self.app = app

    def connection_made(self, transport):
        self.transport = transport
        print('port opened', transport)
        transport.serial.rts = False
        self.app.uart = transport

    def data_received(self, data):
        message = data.decode() # repr(data)
        print('data received', message)
        app.textEdit.append(message)

    def connection_lost(self, exc):
        print('port closed')
        self.transport.loop.stop()
    def stopall(UART_Window):
        if UART_Window.uart != None:
            UART_Window.uart.close()

if __name__ == '__main__':
    import sys
    win = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    app = Ui_MainWindow()
    app.setupUi(MainWindow)         
    UART_Window=UartCom(app)
    MainWindow.show() 
    win.aboutToQuit.connect(lambda: stopall(UART_Window))
    sys.exit(win.exec_())



