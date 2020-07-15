from second import *

def event(self):
    self.pushButton.clicked.connect(self.str1)

def str1(self):
    a = self.lineEdit.text()
    b = self.lineEdit_2.text()
    self.label.setText(a+b)

Ui_MainWindow.event = event
Ui_MainWindow.str1 = str1

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.event()
    MainWindow.show()
    sys.exit(app.exec_())