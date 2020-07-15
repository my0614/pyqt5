from class_calculator import *

def event(self):
    self.pushButton.clicked.connect(self.result)

def result(self):
    cd = ComboBox(self)
    cd.addItem('Option1')
    
   value1 =  int(self.value.text())
   value2 =  int(self.value2.text())
   self.calculator.setText(str(value1 + value2))
   self.calculator.setText(str(value1 - value2))
   self.calculator.setText(str(value1 * value2))
   self.calculator.setText(str(value1 / value2))


Ui_MainWindow.event = event
Ui_MainWindow.value = result


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.event()
    MainWindow.show()
    sys.exit(app.exec_())