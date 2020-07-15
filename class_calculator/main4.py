from class_calculator import *

def event(self):
    self.calculator_bt.clicked.connect(self.valuea)

def valuea(self):
    value1 =  self.value.text()
    value2 =  self.value2.text()
    operate = self.comboBox.currentText()
    c = eval(value1+ operate + value2)
    self.result.setText(str(c))



Ui_MainWindow.event = event
Ui_MainWindow.valuea = valuea


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.event()
    MainWindow.show()
    sys.exit(app.exec_())