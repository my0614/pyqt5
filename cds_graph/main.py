from cds import *
from PyQt5 import QtCore, QtGui, QtWidgets
from pyqtgraph import PlotWidget, plot
import pyqtgraph as pg
import threading
import serial
import time
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtCore import pyqtSlot


value = []
fvalue = 0
ser = serial.Serial(port='COM5',
                    baudrate=115200,
                    parity=serial.PARITY_NONE,
                    stopbits=serial.STOPBITS_ONE,
                    bytesize=serial.EIGHTBITS,
                    timeout=1)

#def signals(self):
def cds(ui):
    global value
    global fvalue
    cnt = 0
    while True:
        ser_data = ser.readline()
        if(ser_data):
            #ser_data = str(ser_data)
            #print(type(ser_data))
            print("success")
        
            fvalue = int(ser_data[5:10]) # 슬라이싱한값을 int로 바로 변환
            print(fvalue)
            ui.cds_value.setText(str(fvalue))
            value.append(fvalue)
            ui.uiUpdateDelegate.emit(1)

    

class MyFirstGuiProgram(QtWidgets.QMainWindow, Ui_MainWindow):
    uiUpdateDelegate = pyqtSignal(int)
    global value
    global fvalue
    def __init__(self, parent= None):
        QtWidgets.QMainWindow.__init__(self,parent=parent)
        self.setupUi(self)
        
        self.graphWidget = pg.PlotWidget(self.graphicsView)
        self.graphWidget.resize(self.graphicsView.size()) # graphicView사이즈만큼 키우기
        self.uiUpdateDelegate.connect(self.uiUpdater)
        self.graphWidget.setBackground('#ffffff')
        self.graphWidget.setRange(xRange=[1, 20],yRange = [1,4000])
        self.graphWidget.showGrid(x=True, y=True)
        
        self.graphWidget.plot(value, pen=pg.mkPen('b', width=2),
           style=QtCore.Qt.DashLine, symbol=('x'),  symbolBrush='b') 
        
    def uiUpdater(self):    
        self.graphWidget.clear()
        self.graphWidget.plot(value, pen=pg.mkPen('r', width=2),style=QtCore.Qt.DashLine, symbol=('o'), symbolBrush='r', symbolSize=5) 

#Ui_MainWindow.signals = signals


if __name__== "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = MyFirstGuiProgram()
    ui.show()
    th = threading.Thread(target = cds,args=(ui,))
    th.daemon = True
    th.start()
    sys.exit(app.exec_())