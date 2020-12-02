# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\rgb.ui'
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
        self.title = QtWidgets.QLabel(self.centralwidget)
        self.title.setGeometry(QtCore.QRect(310, 50, 181, 71))
        self.title.setStyleSheet("font: 75 28pt \"Agency FB\";")
        self.title.setAlignment(QtCore.Qt.AlignCenter)
        self.title.setObjectName("title")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(120, 430, 91, 31))
        self.label_2.setStyleSheet("font: 75 18pt \"Agency FB\";")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(370, 430, 91, 51))
        self.label_3.setStyleSheet("font: 75 18pt \"Agency FB\";")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(600, 430, 91, 31))
        self.label_6.setStyleSheet("font: 75 18pt \"Agency FB\";")
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.red_text = QtWidgets.QTextEdit(self.centralwidget)
        self.red_text.setGeometry(QtCore.QRect(80, 280, 171, 151))
        self.red_text.setObjectName("red_text")
        self.blue_text = QtWidgets.QTextEdit(self.centralwidget)
        self.blue_text.setGeometry(QtCore.QRect(550, 280, 171, 151))
        self.blue_text.setObjectName("blue_text")
        self.green_text = QtWidgets.QTextEdit(self.centralwidget)
        self.green_text.setGeometry(QtCore.QRect(320, 280, 171, 151))
        self.green_text.setObjectName("green_text")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(290, 160, 231, 71))
        self.pushButton.setObjectName("pushButton")
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
        self.title.setText(_translate("MainWindow", "RGB LED"))
        self.label_2.setText(_translate("MainWindow", "red"))
        self.label_3.setText(_translate("MainWindow", "green"))
        self.label_6.setText(_translate("MainWindow", "blue"))
        self.pushButton.setText(_translate("MainWindow", "send"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
