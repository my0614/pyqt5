from dht11_graph import *
from PyQt5 import QtCore, QtGui, QtWidgets
import pyqtgraph as pg
import threading
import serial
import time
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtCore import pyqtSlot


temp=[]
humi=[]

ser = serial.Serial(port='COM5',
                    baudrate=9600,
                    parity=serial.PARITY_NONE,
                    stopbits=serial.STOPBITS_ONE,
                    bytesize=serial.EIGHTBITS,
                    timeout=1)

#def signals(self):
def dht11(ui):
    global temp, humi
    cnt = 0
    while True:
        ser_data = ser.readline()
        if(ser_data):
            #ser_data = str(ser_data)
            #print(type(ser_data))
            print("success")
            print(ser_data)
        
            ftemp = int(ser_data[0:3]) # 슬라이싱한값을 int로 바로 변환
            temp.append(ftemp)

            fhumi = int(ser_data[3:6])# 슬라이싱한값을 int로 바로 변환
            humi.append(fhumi)

            ui.uiUpdateDelegate.emit(1)

    

class MyFirstGuiProgram(QtWidgets.QMainWindow, Ui_MainWindow):
    uiUpdateDelegate = pyqtSignal(int)
    global temp,humi
    def __init__(self, parent= None):
        QtWidgets.QMainWindow.__init__(self,parent=parent)
        self.setupUi(self)
        self.uiUpdateDelegate.connect(self.uiUpdater)
        self.graphicsView.setBackground('#ffffff')
        self.graphicsView.setRange(xRange=[1, 40])
        self.graphicsView.showGrid(x=True, y=True)
        self.graphicsView_2.setBackground('#ffffff')
        self.graphicsView_2.setRange(xRange=[1, 40])
        self.graphicsView_2.showGrid(x=True, y=True)
        
        
        self.graphicsView.plot(temp, pen=pg.mkPen('b', width=2),
           style=QtCore.Qt.DashLine, symbol=('x'),  symbolBrush='b') 
        
    def uiUpdater(self):    
        self.graphicsView.clear()
        self.graphicsView_2.clear()
        self.graphicsView.plot(temp, pen=pg.mkPen('r', width=2),style=QtCore.Qt.DashLine, symbol=('o'), symbolBrush='r', symbolSize=5) 
        self.graphicsView_2.plot(humi, pen=pg.mkPen('r', width=2),style=QtCore.Qt.DashLine, symbol=('o'), symbolBrush='r', symbolSize=5) 



#Ui_MainWindow.signals = signals

if __name__=="__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = MyFirstGuiProgram()
    ui.show()
    th = threading.Thread(target = dht11,args=(ui,))
    th.daemon = True
    th.start()
    sys.exit(app.exec_())