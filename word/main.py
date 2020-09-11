from PyQt5 import QtCore, QtGui, QtWidgets
from add_page import *


class Main(QtWidgets.QStackedWidget):
    pager = pyqtSignal(int)
    def __init__(self):
        super().__init__()

    add = add_page(self.pager)
    self.addWidget(add_page)

if __name__=="__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.button_click()
    ui.add()
    MainWindow.show()
    sys.exit(app.exec_())