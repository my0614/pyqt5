# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'image.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(901, 594)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.wolf = QtWidgets.QPushButton(self.centralwidget)
        self.wolf.setGeometry(QtCore.QRect(10, 70, 411, 421))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.wolf.setFont(font)
        self.wolf.setAutoFillBackground(False)
        self.wolf.setStyleSheet("background-image: url(:/newPrefix/늑대.jpg);\n"
"QPushButton#click:pressed {\n"
"    text : click ;\n"
"    font : 20pt;\n"
"    color : black;\n"
"    backgound : white;\n"
"    background-image: url(:/image/picture.png);\n"
"\n"
"}\n"
"")
        self.wolf.setText("")
        self.wolf.setObjectName("wolf")
        self.cat = QtWidgets.QPushButton(self.centralwidget)
        self.cat.setGeometry(QtCore.QRect(420, 90, 471, 331))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.cat.setFont(font)
        self.cat.setStyleSheet("background-image: url(:/newPrefix/고양이.jpg);\n"
"QPushButton#click:pressed {\n"
"    text : click ;\n"
"    font : 20pt;\n"
"    color : black;\n"
"    backgound : white;\n"
"    background-image: url(:/image/picture.png);\n"
"\n"
"}\n"
"")
        self.cat.setText("")
        self.cat.setObjectName("cat")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(170, 510, 141, 41))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(580, 470, 141, 41))
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "PRESS PICTURE"))
        self.label_2.setText(_translate("MainWindow", "PRESS PICTURE"))
import pyqt_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
