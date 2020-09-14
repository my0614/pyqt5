# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\first_page.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_first_page(QtWidgets.QWidget):
    def __init__(self,pager = None):
        super().__init__()
        self.pager = pager
        self.setupUi()

    def setupUi(self):
        self.setObjectName("self")
        self.resize(800, 600)
        self.textEdit = QtWidgets.QTextEdit(self)
        self.textEdit.setGeometry(QtCore.QRect(250, 110, 301, 111))
        self.textEdit.setObjectName("textEdit")
        self.textEdit_2 = QtWidgets.QTextEdit(self)
        self.textEdit_2.setGeometry(QtCore.QRect(250, 290, 301, 111))
        self.textEdit_2.setObjectName("textEdit_2")
        self.pushButton = QtWidgets.QPushButton(self)
        self.pushButton.setGeometry(QtCore.QRect(290, 450, 231, 61))
        self.pushButton.setObjectName("pushButton")
        self.korean_2 = QtWidgets.QLabel(self)
        self.korean_2.setGeometry(QtCore.QRect(380, 230, 51, 41))
        self.korean_2.setStyleSheet("font: 11pt \"Agency FB\";")
        self.korean_2.setObjectName("korean_2")
        self.korean = QtWidgets.QLabel(self)
        self.korean.setGeometry(QtCore.QRect(390, 60, 51, 41))
        self.korean.setStyleSheet("font: 11pt \"Agency FB\";")
        self.korean.setObjectName("korean")

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, form):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("self", "self"))
        self.pushButton.setText(_translate("self", "추가하기"))
        self.korean_2.setText(_translate("self", "한자"))
        self.korean.setText(_translate("self", "한글"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_first_page()
    Form.show()
    sys.exit(app.exec_())
