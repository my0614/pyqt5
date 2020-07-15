from PyQt5 import QtCore, QtGui, QtWidgets
from graph import *
import pyqtgraph as pg



x = [2,4,6,8,10]
y = [1,2,3,4,5]
z = [1,3,7,5,10]
class MyFirstGuiProgram(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent=parent)
        self.setupUi(self)
        self.graphicsView.setBackground('#11ffff')       
        self.graphicsView_2.setBackground('#ffffff')
        self.graphicsView_3.setBackground('y')
        
    def cevent(self):
        self.pushButton.clicked.connect(self.plotGraph)

    def plotGraph(self):
        self.graphicsView.plot(x, pen=pg.mkPen('b', width=2),
            style=QtCore.Qt.DashLine, symbol=('o'), 
            symbolBrush='y')
        self.graphicsView_2.plot(y, pen='#0000ff', symbol='x')
        self.graphicsView_3.plot(z, pen="#ffffff", symbol = "x")

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    w = MyFirstGuiProgram()
    w.show()
    w.cevent()
    sys.exit(app.exec_())
