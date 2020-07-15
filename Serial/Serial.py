# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Serial.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.LED1 = QtWidgets.QPushButton(self.centralwidget)
        self.LED1.setGeometry(QtCore.QRect(260, 130, 261, 91))
        self.LED1.setObjectName("LED1")
        self.LED2 = QtWidgets.QPushButton(self.centralwidget)
        self.LED2.setGeometry(QtCore.QRect(260, 260, 261, 91))
        self.LED2.setObjectName("LED2")
        self.LED3 = QtWidgets.QPushButton(self.centralwidget)
        self.LED3.setGeometry(QtCore.QRect(260, 400, 261, 91))
        self.LED3.setObjectName("LED3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.LED1.setText(_translate("MainWindow", "LED1"))
        self.LED2.setText(_translate("MainWindow", "LED2"))
        self.LED3.setText(_translate("MainWindow", "LED3"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
