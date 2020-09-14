from PyQt5 import QtGui
import sys
from PyQt5.QtCore import pyqtSignal, QObject
from PyQt5.QtWidgets import QApplication, QMainWindow
from start_page import *
from first_page import *


class Main(QtWidgets.QStackedWidget):
    pager = pyqtSignal(int)
    def __init__(self):
        super().__init__()
        self.pager.connect(self.setCurrentIndex) 

        self.start_page = Ui_start_page(self.pager)
        self.addWidget(self.start_page) #index 0
        
        self.first_page = Ui_first_page(self.pager)
        self.addWidget(self.first_page) #index 1
        self.resize(800,800)
        
        

        



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = Main()
    ui.show()
    app.exec_()