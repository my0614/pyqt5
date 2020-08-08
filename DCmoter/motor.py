# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'motor.ui'
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
        self.LEFT = QtWidgets.QPushButton(self.centralwidget)
        self.LEFT.setGeometry(QtCore.QRect(80, 210, 151, 161))
        self.LEFT.setObjectName("LEFT")
        self.RIGHT = QtWidgets.QPushButton(self.centralwidget)
        self.RIGHT.setGeometry(QtCore.QRect(510, 220, 151, 161))
        self.RIGHT.setObjectName("RIGHT")
        self.FORWARD = QtWidgets.QPushButton(self.centralwidget)
        self.FORWARD.setGeometry(QtCore.QRect(300, 50, 151, 161))
        self.FORWARD.setObjectName("FORWARD")
        self.BACK = QtWidgets.QPushButton(self.centralwidget)
        self.BACK.setGeometry(QtCore.QRect(300, 370, 151, 161))
        self.BACK.setObjectName("BACK")
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
        self.LEFT.setText(_translate("MainWindow", "LEFT"))
        self.RIGHT.setText(_translate("MainWindow", "RIGHT"))
        self.FORWARD.setText(_translate("MainWindow", "FOWARD"))
        self.BACK.setText(_translate("MainWindow", "back"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
