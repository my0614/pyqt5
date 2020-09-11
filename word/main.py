from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from word import *
from add_page import *
        
def event(self):
    self.add.clicked.connect(self.add_click)

def add_click(self):
    #self.pager.connect(self.add_page)
    print('hello')
Ui_MainWindow.event = event
Ui_MainWindow.add_click = add_click

if __name__=="__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.event()
    ui.add_click()
    MainWindow.show()
    sys.exit(app.exec_())