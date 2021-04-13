# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\club_join.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, bloodtype_tex):
        bloodtype_tex.setObjectName("bloodtype_tex")
        bloodtype_tex.resize(830, 701)
        bloodtype_tex.setStyleSheet("background-color: rgb(170, 85, 255);")
        self.centralwidget = QtWidgets.QWidget(bloodtype_tex)
        self.centralwidget.setObjectName("centralwidget")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(20, 10, 771, 531))
        self.stackedWidget.setObjectName("stackedWidget")
        self.info = QtWidgets.QWidget()
        self.info.setObjectName("info")
        self.dream_text = QtWidgets.QLineEdit(self.info)
        self.dream_text.setGeometry(QtCore.QRect(280, 170, 311, 51))
        self.dream_text.setStyleSheet("\n"
"background-color: rgb(255, 255, 255);")
        self.dream_text.setObjectName("dream_text")
        self.favoritefood_text = QtWidgets.QLineEdit(self.info)
        self.favoritefood_text.setGeometry(QtCore.QRect(280, 240, 311, 51))
        self.favoritefood_text.setStyleSheet("\n"
"background-color: rgb(255, 255, 255);")
        self.favoritefood_text.setObjectName("favoritefood_text")
        self.name_6 = QtWidgets.QLabel(self.info)
        self.name_6.setGeometry(QtCore.QRect(140, 30, 511, 111))
        self.name_6.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.name_6.setStyleSheet("font: 75 35pt \"Agency FB\";\n"
"color: white;")
        self.name_6.setAlignment(QtCore.Qt.AlignCenter)
        self.name_6.setObjectName("name_6")
        self.bucketlist = QtWidgets.QLabel(self.info)
        self.bucketlist.setGeometry(QtCore.QRect(100, 390, 161, 41))
        self.bucketlist.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.bucketlist.setStyleSheet("font: 75 23pt \"Agency FB\";")
        self.bucketlist.setAlignment(QtCore.Qt.AlignCenter)
        self.bucketlist.setObjectName("bucketlist")
        self.favortie_food = QtWidgets.QLabel(self.info)
        self.favortie_food.setGeometry(QtCore.QRect(80, 240, 181, 51))
        self.favortie_food.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.favortie_food.setStyleSheet("font: 75 23pt \"Agency FB\";")
        self.favortie_food.setAlignment(QtCore.Qt.AlignCenter)
        self.favortie_food.setObjectName("favortie_food")
        self.favorite_color = QtWidgets.QLabel(self.info)
        self.favorite_color.setGeometry(QtCore.QRect(90, 320, 171, 41))
        self.favorite_color.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.favorite_color.setStyleSheet("font: 75 23pt \"Agency FB\";")
        self.favorite_color.setAlignment(QtCore.Qt.AlignCenter)
        self.favorite_color.setObjectName("favorite_color")
        self.Dream = QtWidgets.QLabel(self.info)
        self.Dream.setGeometry(QtCore.QRect(150, 170, 91, 41))
        self.Dream.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Dream.setStyleSheet("font: 75 23pt \"Agency FB\";")
        self.Dream.setAlignment(QtCore.Qt.AlignCenter)
        self.Dream.setObjectName("Dream")
        self.other_bt = QtWidgets.QPushButton(self.info)
        self.other_bt.setGeometry(QtCore.QRect(650, 470, 93, 28))
        self.other_bt.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"font: 75 14pt \"Agency FB\";\n"
"color : white;")
        self.other_bt.setObjectName("other_bt")
        self.favoritecolor_text = QtWidgets.QLineEdit(self.info)
        self.favoritecolor_text.setGeometry(QtCore.QRect(280, 320, 311, 51))
        self.favoritecolor_text.setStyleSheet("\n"
"background-color: rgb(255, 255, 255);")
        self.favoritecolor_text.setObjectName("favoritecolor_text")
        self.bucketlist_text = QtWidgets.QLineEdit(self.info)
        self.bucketlist_text.setGeometry(QtCore.QRect(280, 390, 311, 51))
        self.bucketlist_text.setStyleSheet("\n"
"background-color: rgb(255, 255, 255);")
        self.bucketlist_text.setObjectName("bucketlist_text")
        self.stackedWidget.addWidget(self.info)
        self.info2 = QtWidgets.QWidget()
        self.info2.setObjectName("info2")
        self.name_5 = QtWidgets.QLabel(self.info2)
        self.name_5.setGeometry(QtCore.QRect(180, 20, 511, 111))
        self.name_5.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.name_5.setStyleSheet("font: 75 35pt \"Agency FB\";\n"
"color: white;")
        self.name_5.setAlignment(QtCore.Qt.AlignCenter)
        self.name_5.setObjectName("name_5")
        self.name_text = QtWidgets.QLineEdit(self.info2)
        self.name_text.setGeometry(QtCore.QRect(280, 150, 311, 51))
        self.name_text.setStyleSheet("\n"
"background-color: rgb(255, 255, 255);")
        self.name_text.setObjectName("name_text")
        self.name = QtWidgets.QLabel(self.info2)
        self.name.setGeometry(QtCore.QRect(160, 150, 91, 41))
        self.name.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.name.setStyleSheet("font: 75 23pt \"Agency FB\";")
        self.name.setAlignment(QtCore.Qt.AlignCenter)
        self.name.setObjectName("name")
        self.club_bt = QtWidgets.QPushButton(self.info2)
        self.club_bt.setGeometry(QtCore.QRect(650, 490, 93, 28))
        self.club_bt.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"font: 75 14pt \"Agency FB\";\n"
"color : white;")
        self.club_bt.setObjectName("club_bt")
        self.age_text = QtWidgets.QLineEdit(self.info2)
        self.age_text.setGeometry(QtCore.QRect(280, 230, 311, 51))
        self.age_text.setStyleSheet("\n"
"background-color: rgb(255, 255, 255);")
        self.age_text.setObjectName("age_text")
        self.age = QtWidgets.QLabel(self.info2)
        self.age.setGeometry(QtCore.QRect(160, 220, 91, 51))
        self.age.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.age.setStyleSheet("font: 75 23pt \"Agency FB\";")
        self.age.setAlignment(QtCore.Qt.AlignCenter)
        self.age.setObjectName("age")
        self.howetown = QtWidgets.QLabel(self.info2)
        self.howetown.setGeometry(QtCore.QRect(100, 310, 171, 41))
        self.howetown.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.howetown.setStyleSheet("font: 75 23pt \"Agency FB\";")
        self.howetown.setAlignment(QtCore.Qt.AlignCenter)
        self.howetown.setObjectName("howetown")
        self.bloodtype = QtWidgets.QLabel(self.info2)
        self.bloodtype.setGeometry(QtCore.QRect(110, 380, 161, 41))
        self.bloodtype.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.bloodtype.setStyleSheet("font: 75 23pt \"Agency FB\";")
        self.bloodtype.setAlignment(QtCore.Qt.AlignCenter)
        self.bloodtype.setObjectName("bloodtype")
        self.motto = QtWidgets.QLabel(self.info2)
        self.motto.setGeometry(QtCore.QRect(100, 450, 161, 41))
        self.motto.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.motto.setStyleSheet("font: 75 23pt \"Agency FB\";")
        self.motto.setAlignment(QtCore.Qt.AlignCenter)
        self.motto.setObjectName("motto")
        self.motto_text = QtWidgets.QLineEdit(self.info2)
        self.motto_text.setGeometry(QtCore.QRect(280, 450, 311, 51))
        self.motto_text.setStyleSheet("\n"
"background-color: rgb(255, 255, 255);")
        self.motto_text.setText("")
        self.motto_text.setObjectName("motto_text")
        self.hometown_text = QtWidgets.QLineEdit(self.info2)
        self.hometown_text.setGeometry(QtCore.QRect(280, 310, 311, 51))
        self.hometown_text.setStyleSheet("\n"
"background-color: rgb(255, 255, 255);")
        self.hometown_text.setObjectName("hometown_text")
        self.bloodtype_text = QtWidgets.QLineEdit(self.info2)
        self.bloodtype_text.setGeometry(QtCore.QRect(280, 380, 311, 51))
        self.bloodtype_text.setStyleSheet("\n"
"background-color: rgb(255, 255, 255);")
        self.bloodtype_text.setObjectName("bloodtype_text")
        self.stackedWidget.addWidget(self.info2)
        self.club_info = QtWidgets.QPushButton(self.centralwidget)
        self.club_info.setGeometry(QtCore.QRect(120, 600, 121, 51))
        self.club_info.setObjectName("club_info")
        self.other_info = QtWidgets.QPushButton(self.centralwidget)
        self.other_info.setGeometry(QtCore.QRect(250, 600, 121, 51))
        self.other_info.setObjectName("other_info")
        bloodtype_tex.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(bloodtype_tex)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 830, 26))
        self.menubar.setObjectName("menubar")
        bloodtype_tex.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(bloodtype_tex)
        self.statusbar.setObjectName("statusbar")
        bloodtype_tex.setStatusBar(self.statusbar)

        self.retranslateUi(bloodtype_tex)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(bloodtype_tex)

    def retranslateUi(self, bloodtype_tex):
        _translate = QtCore.QCoreApplication.translate
        bloodtype_tex.setWindowTitle(_translate("bloodtype_tex", "MainWindow"))
        self.name_6.setText(_translate("bloodtype_tex", "기본정보"))
        self.bucketlist.setText(_translate("bloodtype_tex", "bucket list"))
        self.favortie_food.setText(_translate("bloodtype_tex", "favorite Food"))
        self.favorite_color.setText(_translate("bloodtype_tex", "favorite Color"))
        self.Dream.setText(_translate("bloodtype_tex", "Dream"))
        self.other_bt.setText(_translate("bloodtype_tex", "SAVE"))
        self.name_5.setText(_translate("bloodtype_tex", "동아리 회원가입"))
        self.name.setText(_translate("bloodtype_tex", "name"))
        self.club_bt.setText(_translate("bloodtype_tex", "SAVE"))
        self.age.setText(_translate("bloodtype_tex", "age"))
        self.howetown.setText(_translate("bloodtype_tex", "Hometown"))
        self.bloodtype.setText(_translate("bloodtype_tex", "blood_type"))
        self.motto.setText(_translate("bloodtype_tex", "motto"))
        self.club_info.setText(_translate("bloodtype_tex", "동아리가입"))
        self.other_info.setText(_translate("bloodtype_tex", "기타정보"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    bloodtype_tex = QtWidgets.QMainWindow()
    ui = Ui_bloodtype_tex()
    ui.setupUi(bloodtype_tex)
    bloodtype_tex.show()
    sys.exit(app.exec_())
