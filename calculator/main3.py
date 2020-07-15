from calculator import *

def event(self):
    self.pushButton.clicked.connect(self.value)

def value(self):
   value1 =  int(self.lineEdit.text())
   value2 =  int(self.lineEdit_2.text())
   self.label.setText(str(value1 + value2))
   self.label_2.setText(str(value1 - value2))
   self.label_3.setText(str(value1 * value2))
   self.label_4.setText(str(value1 / value2))


Ui_MainWindow.event = event
Ui_MainWindow.value = value


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.event()
    MainWindow.show()
    sys.exit(app.exec_())