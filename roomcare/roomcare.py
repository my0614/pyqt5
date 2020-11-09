# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\roomcare.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 600)
        MainWindow.setStyleSheet("background-color : rgb(112,173,71);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.title = QtWidgets.QLabel(self.centralwidget)
        self.title.setGeometry(QtCore.QRect(340, 10, 361, 101))
        self.title.setStyleSheet("font: 34pt \"Arial Rounded MT Bold\";\n"
"color : white;")
        self.title.setObjectName("title")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(110, 170, 160, 320))
        self.label.setStyleSheet("background-color : white;\n"
"border-radius : 15px;")
        self.label.setText("")
        self.label.setObjectName("label")
        self.box2 = QtWidgets.QLabel(self.centralwidget)
        self.box2.setGeometry(QtCore.QRect(330, 170, 160, 320))
        self.box2.setStyleSheet("background-color : white;\n"
"border-radius : 15px;")
        self.box2.setText("")
        self.box2.setObjectName("box2")
        self.box3 = QtWidgets.QLabel(self.centralwidget)
        self.box3.setGeometry(QtCore.QRect(550, 170, 160, 320))
        self.box3.setStyleSheet("background-color : white;\n"
"border-radius : 15px;")
        self.box3.setText("")
        self.box3.setObjectName("box3")
        self.temp = QtWidgets.QLabel(self.centralwidget)
        self.temp.setGeometry(QtCore.QRect(770, 170, 160, 130))
        self.temp.setStyleSheet("background-color : white;\n"
"border-radius : 15px;")
        self.temp.setText("")
        self.temp.setObjectName("temp")
        self.humi = QtWidgets.QLabel(self.centralwidget)
        self.temp.setStyleSheet("font-size: 20pt; background-color : white; border-radius : 15px; font-weight : bold;")
        self.humi.setGeometry(QtCore.QRect(770, 360, 160, 130))
        self.humi.setStyleSheet("font-size: 20pt; background-color : white; border-radius : 15px; font-weight : bold;")
        self.humi.setText("")
        self.humi.setObjectName("humi")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(150, 110, 81, 51))
        self.lineEdit.setStyleSheet("border : none;\n"
"font: 200 18pt \"Arial Black\";")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(360, 110, 101, 51))
        self.lineEdit_2.setStyleSheet("border : none;\n"
"font: 87 18pt \"Arial Black\";")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(600, 110, 91, 41))
        self.lineEdit_3.setStyleSheet("border : none;\n"
"font: 87 18pt \"Arial Black\";")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(810, 120, 91, 41))
        self.lineEdit_4.setStyleSheet("border : none;\n"
"font: 87 18pt \"Arial Black\";")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setGeometry(QtCore.QRect(810, 310, 101, 41))
        self.lineEdit_5.setStyleSheet("border : none;\n"
"font: 87 18pt \"Arial Black\";")
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.LED1 = QtWidgets.QPushButton(self.centralwidget)
        self.LED1.setGeometry(QtCore.QRect(120, 180, 141, 111))
        self.LED1.setStyleSheet("border-radius :15px;\n"
"color : white;\n"
"font: 87 16pt \"Arial Black\";font-wieght : bold;")
        self.LED1.setObjectName("LED1")
        self.LED3 = QtWidgets.QPushButton(self.centralwidget)
        self.LED3.setGeometry(QtCore.QRect(560, 180, 141, 111))
        self.LED3.setStyleSheet("border-radius :15px;\n"
"color : white;\n"
"font: 87 16pt \"Arial Black\";font-wieght : bold;")
        self.LED3.setObjectName("LED3")
        self.LED2 = QtWidgets.QPushButton(self.centralwidget)
        self.LED2.setGeometry(QtCore.QRect(340, 370, 141, 111))
        self.LED2.setStyleSheet("border-radius :15px;\n"
"color : white;\n"
"font: 87 16pt \"Arial Black\"; font-wieght : bold;")
        self.LED2.setObjectName("LED2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.title.setText(_translate("MainWindow", "Room Care"))
        self.lineEdit.setText(_translate("MainWindow", "거실"))
        self.lineEdit_2.setText(_translate("MainWindow", "화장실"))
        self.lineEdit_3.setText(_translate("MainWindow", "주방"))
        self.lineEdit_4.setText(_translate("MainWindow", "온도"))
        self.lineEdit_5.setText(_translate("MainWindow", "습도"))
        self.LED1.setText(_translate("MainWindow", "ON"))
        self.LED3.setText(_translate("MainWindow", "ON"))
        self.LED2.setText(_translate("MainWindow", "OFF"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
