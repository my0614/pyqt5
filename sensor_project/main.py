
from sensor import *
import serial
#import threading
#from threading import Thread
#import time

ser = serial.Serial(port='COM5',
                    baudrate=9600,
                    parity=serial.PARITY_NONE,
                    stopbits=serial.STOPBITS_ONE,
                    bytesize=serial.EIGHTBITS,
                    timeout=1)

def signals(self):
    self.password_bt.clicked.connect(self.password_ch) #비밀번호변경함수호출
    self.picture() #picture함수호출


def picture(self):
    global value
    while True:
        ser_data = ser.readline() #sensor_count
        if(ser_data):
            print(ser_data)

            value = int(ser_data[3:4]) #센서번호가지고 오기
            #초음파센서감지
            if(value == 1):
                print("초음파센서감지")
                self.sensor_text.setText("초음파센서 감지")
            #sound센서
            if(value == 2):
                print("사운드센서감지")
                self.sensor_text.setText("사운드센서 감지")
            
            if(value == 3):
                print("노크모듈센서감지")
                self.sensor_text.setText("노크모듈센서 감지")

#비밀번호변경 함수
def password_ch(self):
    ps = self.ch_password.setText() #비밀번호 저장
    print(str(ps)) #비밀번호출력
    bt_event = QMessageBox.information(self, 'PyQt5',"비밀")
    



Ui_MainWindow.picture = picture
if __name__=="__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow(
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.picture()
    #th = threading.Thread(target = picture,args=(ui,))
    #th.daemon = True
    #th.start()
    MainWindow.show()
    sys.exit(app.exec_())