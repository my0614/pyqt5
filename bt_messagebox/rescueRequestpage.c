from PyQt5 import QtGui ,QtCore, QtWidgets
from PyQt5.QtWidgets import *

class Ui_rescueRequestpage(QtWidgets.QWidget):
    def __init__(self,pager):
        super().__init__() # 부모 클래스 호출
        self.pager = pager
        self.setObjectName("rescueResquestPage")
        self.resize(800,480)
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(0,0,800,180))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("Ui_rescueRequestpage")
        self.label.setText("충돌이 감지되었습니다")      
        
       

        # 구조요청 버튼
        pybutton = QtWidgets.QPushButton('구조 요청', self) 
        pybutton.resize(200, 250)
        pybutton.move(150, 150)
        pybutton.setStyleSheet("font: 40 25pt Arial;")
        pybutton.clicked.connect(self.bt_click)
        
        # 취소 버튼
        pybutton = QtWidgets.QPushButton('취 소', self) 
        pybutton.resize(200, 250)
        pybutton.move(450, 150)
        pybutton.setStyleSheet("font: 60 30pt Arial;")
        pybutton.clicked.connect(self.bt_click2)

    def bt_click2(self,event):  
        buttonReply = QMessageBox.information(
            self, 'PyQt5', "Message Box", 
            QMessageBox.Yes | QMessageBox.No,        QMessageBox.No
            )
 
        if buttonReply == QMessageBox.Yes:
            print('Yes clicked.')
            
        else:
            print('No clicked.')


    def bt_click(self,event):
        self.pager.emit(0)

    

         

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    rescueReqestpage = QtWidgets.QWidget()
    ui = Ui_rescueReqestpage()
    ui.setupUi(rescueReqestpage)
    rescueReqestpage.show()
    sys.exit(app.exec_())

