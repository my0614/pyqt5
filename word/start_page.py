
from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3


class Ui_start_page(QtWidgets.QWidget):

    def __init__(self,pager = None):
        super().__init__()
        self.pager = pager
        self.setupUi()
   

    def setupUi(self):
        self.title = QtWidgets.QLabel(self)
        self.title.setGeometry(QtCore.QRect(260, 50, 261, 91))
        self.title.setStyleSheet("font: 75 36pt \"Agency FB\";")
        self.title.setObjectName("title")
        self.word = QtWidgets.QTextEdit(self)
        self.word.setGeometry(QtCore.QRect(210, 180, 341, 121))
        self.word.setObjectName("word1")
        self.word2 = QtWidgets.QTextEdit(self)
        self.word2.setGeometry(QtCore.QRect(210, 350, 341, 121))
        self.word2.setObjectName("word2")
        self.answer = QtWidgets.QPushButton(self)
        self.answer.setGeometry(QtCore.QRect(320, 610, 141, 51))
        self.answer.setStyleSheet("background-color : gray;\n"
"font: 11pt \"Agency FB\";")
        self.answer.setObjectName("answer")
        self.next = QtWidgets.QPushButton(self)
        self.next.setGeometry(QtCore.QRect(540, 610, 141, 51))
        self.next.setStyleSheet("background-color : gray;\n"
"font: 11pt \"Agency FB\";")
        self.next.setObjectName("next")
        self.add = QtWidgets.QPushButton(self)
        self.add.setGeometry(QtCore.QRect(100, 610, 141, 51))
        self.add.setStyleSheet("background-color : gray;\n"
"font: 11pt \"Agency FB\";")
        self.add.setObjectName("add")
        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)
        
        self.add.clicked.connect(lambda : self.pager.emit(1))
        self.answer.clicked.connect(self.answer_word)
        self.next.clicked.connect(self.next_bt)



    def answer_word(self, form):
        
        con = sqlite3.connect("./hello.db")
        cur = con.cursor()
        cur.execute("CREATE TABLE if not exists hello(one text, two text);")
        
        cur.execute("SELECT * FROM hello LIMIT ?, ?;",(0,1))

        result = cur.fetchall()
        for row in result:
            self.word2.setPlainText("\n".join(row))
        con.commit()
        con.close()


    def next_bt(self, form):
        cnt = 1
        cnt2 = cnt2+ 1
        con = sqlite3.connect("./hello.db")
        cur = con.cursor()
        cur.execute("CREATE TABLE if not exists hello(one text, two text);")


        cur.execute("SELECT * FROM hello LIMIT ?, ?;",(cnt,cnt2))
        cnt2 +=1
        result = cur.fetchall()

        for row in result:
            self.word2.setPlainText("\n".join(row))
        con.commit()
        con.close()

        

    def retranslateUi(self, form):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("self", "self"))
        self.title.setText(_translate("self", "사자성어"))
        self.answer.setText(_translate("self", "정답보기"))
        self.next.setText(_translate("self", "다음"))
        self.add.setText(_translate("self", "추가하기"))
        

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_start_page()
    ui.show()
    sys.exit(app.exec_())
