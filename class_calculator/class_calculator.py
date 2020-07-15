# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'class_calculator.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 454)
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.CrossCursor))
        MainWindow.setAutoFillBackground(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.value = QtWidgets.QLineEdit(self.centralwidget)
        self.value.setGeometry(QtCore.QRect(20, 60, 113, 21))
        self.value.setObjectName("value")
        self.value2 = QtWidgets.QLineEdit(self.centralwidget)
        self.value2.setGeometry(QtCore.QRect(240, 60, 113, 21))
        self.value2.setObjectName("value2")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(140, 60, 94, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(360, 60, 21, 16))
        self.label.setObjectName("label")
        self.result = QtWidgets.QLineEdit(self.centralwidget)
        self.result.setGeometry(QtCore.QRect(380, 60, 113, 21))
        self.result.setObjectName("result")
        self.clear = QtWidgets.QPushButton(self.centralwidget)
        self.clear.setGeometry(QtCore.QRect(30, 130, 231, 71))
        self.clear.setObjectName("clear")
        self.calculator_bt = QtWidgets.QPushButton(self.centralwidget)
        self.calculator_bt.setGeometry(QtCore.QRect(270, 130, 231, 71))
        self.calculator_bt.setObjectName("calculator_bt")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.clear.clicked.connect(self.value.clear)
        self.clear.clicked.connect(self.value2.clear)
        self.clear.clicked.connect(self.result.clear)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.comboBox.setItemText(0, _translate("MainWindow", "+"))
        self.comboBox.setItemText(1, _translate("MainWindow", "-"))
        self.comboBox.setItemText(2, _translate("MainWindow", "*"))
        self.comboBox.setItemText(3, _translate("MainWindow", "/"))
        self.label.setText(_translate("MainWindow", "="))
        self.clear.setText(_translate("MainWindow", "Clear"))
        self.calculator_bt.setText(_translate("MainWindow", "Calculate"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
