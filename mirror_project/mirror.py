# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mirror.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1206, 880)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.calendar = QtWidgets.QCalendarWidget(self.centralwidget)
        self.calendar.setGeometry(QtCore.QRect(0, 0, 1211, 311))
        self.calendar.setObjectName("calendar")
        self.now_time = QtWidgets.QLCDNumber(self.centralwidget)
        self.now_time.setGeometry(QtCore.QRect(70, 650, 545, 91))
        self.now_time.setStyleSheet("background-color : rgb(203, 203, 203);")
        self.now_time.setObjectName("now_time")
        self.Weather = QtWidgets.QLabel(self.centralwidget)
        self.Weather.setGeometry(QtCore.QRect(10, 320, 481, 111))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.Weather.setFont(font)
        self.Weather.setStyleSheet("background-color : rgb(255, 255, 255);\n"
"font: 75 9pt \"Agency FB\";")
        self.Weather.setText("")
        self.Weather.setAlignment(QtCore.Qt.AlignCenter)
        self.Weather.setObjectName("Weather")
        self.Weather_1 = QtWidgets.QLabel(self.centralwidget)
        self.Weather_1.setGeometry(QtCore.QRect(10, 430, 481, 61))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.Weather_1.setFont(font)
        self.Weather_1.setStyleSheet("background-color : rgb(255, 255, 255);\n"
"font: 75 9pt \"Agency FB\";")
        self.Weather_1.setText("")
        self.Weather_1.setAlignment(QtCore.Qt.AlignCenter)
        self.Weather_1.setObjectName("Weather_1")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1206, 26))
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


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
