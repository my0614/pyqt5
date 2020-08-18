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
        MainWindow.setStyleSheet("font: 75 12pt \"Agency FB\";\n"
"border: none;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.calendar = QtWidgets.QCalendarWidget(self.centralwidget)
        self.calendar.setGeometry(QtCore.QRect(0, 0, 1211, 311))
        self.calendar.setStyleSheet("background-color : rgb(255, 170, 127);")
        self.calendar.setObjectName("calendar")
        self.Weather = QtWidgets.QLabel(self.centralwidget)
        self.Weather.setGeometry(QtCore.QRect(70, 340, 481, 91))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.Weather.setFont(font)
        self.Weather.setStyleSheet("background-color : rgb(255, 167, 140);\n"
"font: 75 9pt \"Agency FB\";\n"
"border-top-right-radius : 10px;\n"
"border-top-left-radius : 10px;")
        self.Weather.setText("")
        self.Weather.setAlignment(QtCore.Qt.AlignCenter)
        self.Weather.setObjectName("Weather")
        self.Weather_1 = QtWidgets.QLabel(self.centralwidget)
        self.Weather_1.setGeometry(QtCore.QRect(70, 400, 481, 81))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.Weather_1.setFont(font)
        self.Weather_1.setStyleSheet("background-color : rgb(255, 167, 140);\n"
"font: 75 9pt \"Agency FB\";\n"
"border-bottom-right-radius : 10px;\n"
"border-bottom-left-radius : 10px;")
        self.Weather_1.setText("")
        self.Weather_1.setAlignment(QtCore.Qt.AlignCenter)
        self.Weather_1.setObjectName("Weather_1")
        self.now_time = QtWidgets.QLabel(self.centralwidget)
        self.now_time.setGeometry(QtCore.QRect(600, 340, 531, 141))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.now_time.setFont(font)
        self.now_time.setStyleSheet("background-color : rgb(255,255,255);\n"
"font: 75 9pt \"Agency FB\";\n"
"border-radius : 10px;")
        self.now_time.setText("")
        self.now_time.setAlignment(QtCore.Qt.AlignCenter)
        self.now_time.setObjectName("now_time")
        self.diner_moring = QtWidgets.QTextBrowser(self.centralwidget)
        self.diner_moring.setGeometry(QtCore.QRect(320, 500, 231, 321))
        self.diner_moring.setStyleSheet("barder: none;\n"
"font: 11pt \"Agency FB\";")
        self.diner_moring.setObjectName("diner_moring")
        self.sports = QtWidgets.QTextEdit(self.centralwidget)
        self.sports.setGeometry(QtCore.QRect(600, 500, 201, 321))
        self.sports.setStyleSheet("border-radius : 15px;\n"
"font: 11pt \"Agency FB\";")
        self.sports.setObjectName("sports")
        self.topic = QtWidgets.QTextEdit(self.centralwidget)
        self.topic.setGeometry(QtCore.QRect(820, 500, 311, 321))
        self.topic.setStyleSheet("border-radius : 15px;\n"
"font: 10pt \"Agency FB\";")
        self.topic.setObjectName("topic")
        self.todolist = QtWidgets.QLabel(self.centralwidget)
        self.todolist.setGeometry(QtCore.QRect(70, 500, 231, 71))
        self.todolist.setStyleSheet("background-color : rgb(255,255,255);\n"
"font: 75 14pt \"Agency FB\";\n"
"")
        self.todolist.setObjectName("todolist")
        self.todo1 = QtWidgets.QLineEdit(self.centralwidget)
        self.todo1.setGeometry(QtCore.QRect(70, 570, 231, 46))
        self.todo1.setObjectName("todo1")
        self.todo2 = QtWidgets.QLineEdit(self.centralwidget)
        self.todo2.setGeometry(QtCore.QRect(70, 610, 231, 46))
        self.todo2.setObjectName("todo2")
        self.todo3 = QtWidgets.QLineEdit(self.centralwidget)
        self.todo3.setGeometry(QtCore.QRect(70, 650, 231, 46))
        self.todo3.setObjectName("todo3")
        self.todo5 = QtWidgets.QLineEdit(self.centralwidget)
        self.todo5.setGeometry(QtCore.QRect(70, 730, 231, 46))
        self.todo5.setObjectName("todo5")
        self.todo4 = QtWidgets.QLineEdit(self.centralwidget)
        self.todo4.setGeometry(QtCore.QRect(70, 690, 231, 46))
        self.todo4.setObjectName("todo4")
        self.made = QtWidgets.QLabel(self.centralwidget)
        self.made.setGeometry(QtCore.QRect(70, 770, 231, 51))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.made.setFont(font)
        self.made.setStyleSheet("background-color : rgb(255,255,255);\n"
"border-top : 1px solid gray;\n"
"font :75 14pt;")
        self.made.setObjectName("made")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(270, 580, 20, 20))
        self.pushButton.setStyleSheet("border : 1px solid gray;")
        self.pushButton.setText("")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(270, 620, 20, 20))
        self.pushButton_2.setStyleSheet("border : 1px solid gray;")
        self.pushButton_2.setText("")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(270, 660, 20, 20))
        self.pushButton_3.setStyleSheet("border : 1px solid gray;")
        self.pushButton_3.setText("")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(270, 700, 20, 20))
        self.pushButton_4.setStyleSheet("border : 1px solid gray;")
        self.pushButton_4.setText("")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(270, 740, 20, 20))
        self.pushButton_5.setStyleSheet("border : 1px solid gray;")
        self.pushButton_5.setText("")
        self.pushButton_5.setObjectName("pushButton_5")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1206, 30))
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
        self.todolist.setText(_translate("MainWindow", "To do list"))
        self.todo1.setText(_translate("MainWindow", " No 1."))
        self.todo2.setText(_translate("MainWindow", "No 2."))
        self.todo3.setText(_translate("MainWindow", "No 3."))
        self.todo5.setText(_translate("MainWindow", "No 5."))
        self.todo4.setText(_translate("MainWindow", "No 4."))
        self.made.setText(_translate("MainWindow", "Made by. Min young"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
