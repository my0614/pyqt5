


from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3

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
        self.pushButton.setGeometry(QtCore.QRect(60, 470, 231, 61))
        self.pushButton.setObjectName("pushButton")
        self.korean_2 = QtWidgets.QLabel(self)
        self.korean_2.setGeometry(QtCore.QRect(380, 230, 51, 41))
        self.korean_2.setStyleSheet("font: 11pt \"Agency FB\";")
        self.korean_2.setObjectName("korean_2")
        self.korean = QtWidgets.QLabel(self)
        self.korean.setStyleSheet("font: 11pt \"Agency FB\";")
        self.korean.setObjectName("korean")
        self.pushButton_2 = QtWidgets.QPushButton(self)
        self.pushButton_2.setGeometry(QtCore.QRect(440, 480, 231, 61))
        self.pushButton_2.setObjectName("pushButton_2")
        #click event
        self.pushButton.clicked.connect(lambda : self.pager.emit(0))
        self.pushButton_2.clicked.connect(lambda : self.pager.emit(0))

        con = sqlite3.connect("./hello.db")
        cur = con.cursor()
        cur.execute("CREATE TABLE if not exists hello(one text, two text);")

        word = self.textEdit.toPlainText
        word_mean = 'young'
        cur.execute("INSERT INTO hello(one, two) values('mmi','young');")
        cur.execute("INSERT INTO hello values('poi','u');")

        con.commit()
        con.close()
        print(str(cur))
        print("finish")


        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, form):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("self", "self"))
        self.pushButton.setText(_translate("self", "추가하기"))
        self.korean_2.setText(_translate("self", "한자"))
        self.korean.setText(_translate("self", "한글"))
        self.pushButton_2.setText(_translate("self", "돌아가기"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_first_page
    Form.show()
    sys.exit(app.exec_())
