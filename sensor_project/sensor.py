# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\sensor.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1056, 652)
        MainWindow.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.title = QtWidgets.QLabel(self.centralwidget)
        self.title.setGeometry(QtCore.QRect(250, 20, 571, 81))
        self.title.setStyleSheet("font: 200 22pt \"Arial Narrow\";\n"
"background-color: rgb(0, 0, 0);\n"
"color : white;\n"
"border-radius : 15px;\n"
"")
        self.title.setAlignment(QtCore.Qt.AlignCenter)
        self.title.setObjectName("title")
        self.background = QtWidgets.QLabel(self.centralwidget)
        self.background.setGeometry(QtCore.QRect(0, -10, 1056, 641))
        self.background.setStyleSheet("\n"
"background-color: rgb(255, 243, 73);")
        self.background.setText("")
        self.background.setObjectName("background")
        self.sensor = QtWidgets.QLabel(self.centralwidget)
        self.sensor.setGeometry(QtCore.QRect(560, 130, 471, 431))
        self.sensor.setStyleSheet("border-radius : 20px;")
        self.sensor.setText("")
        self.sensor.setObjectName("sensor")
        self.picture = QtWidgets.QPushButton(self.centralwidget)
        self.picture.setGeometry(QtCore.QRect(650, 160, 301, 241))
        self.picture.setStyleSheet("background-image: url(:/newPrefix/door.png);\n"
"border:none;\n"
"")
        self.picture.setText("")
        self.picture.setObjectName("picture")
        self.sensor_text = QtWidgets.QLabel(self.centralwidget)
        self.sensor_text.setGeometry(QtCore.QRect(690, 450, 221, 51))
        self.sensor_text.setStyleSheet("font: 75 17pt \"Agency FB\";")
        self.sensor_text.setObjectName("sensor_text")
        self.password = QtWidgets.QLabel(self.centralwidget)
        self.password.setGeometry(QtCore.QRect(20, 130, 471, 431))
        self.password.setStyleSheet("border-radius : 20px;")
        self.password.setText("")
        self.password.setObjectName("password")
        self.password_pic = QtWidgets.QPushButton(self.centralwidget)
        self.password_pic.setGeometry(QtCore.QRect(80, 140, 361, 261))
        self.password_pic.setStyleSheet("background-image: url(:/newPrefix/password.png);")
        self.password_pic.setText("")
        self.password_pic.setObjectName("password_pic")
        self.password_bt = QtWidgets.QPushButton(self.centralwidget)
        self.password_bt.setGeometry(QtCore.QRect(100, 480, 321, 61))
        self.password_bt.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"font: 75 15pt \"Agency FB\";\n"
"color : white;")
        self.password_bt.setObjectName("password_bt")
        self.ch_password = QtWidgets.QTextEdit(self.centralwidget)
        self.ch_password.setGeometry(QtCore.QRect(130, 410, 261, 61))
        self.ch_password.setStyleSheet("font: 75 11pt \"Arial\";")
        self.ch_password.setObjectName("ch_password")
        self.background.raise_()
        self.title.raise_()
        self.sensor.raise_()
        self.picture.raise_()
        self.sensor_text.raise_()
        self.password.raise_()
        self.password_pic.raise_()
        self.password_bt.raise_()
        self.ch_password.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1056, 26))
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
        self.title.setText(_translate("MainWindow", " 침입자 감지 시스템"))
        self.sensor_text.setText(_translate("MainWindow", "도어락 센서 감지"))
        self.password_bt.setText(_translate("MainWindow", "비밀번호 변경하기"))
        
import door_qrc
import knock_qrc
import password_qrc
import sound_qrc
import ultrasonic_qrc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
