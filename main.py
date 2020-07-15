from frist import *

def event(self):
    self.pushButton.clicked.connect(self.load)

def load(self):
    a = str(self.comboBox.currentText())
    self.label.setText(a)

Ui_MainWindow.event = event
Ui_MainWindow.load = load

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.event()
    MainWindow.show()
    sys.exit(app.exec_())