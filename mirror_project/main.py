from mirror import *
import requests
from bs4 import BeautifulSoup
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTimer
from datetime import datetime
import threading


def wheather_crolling(self):
        wheather_source = requests.get("https://search.naver.com/search.naver?sm=top_hty&fbm=1&ie=utf8&query=%EB%82%A0%EC%94%A8").text
        wheather_soup = BeautifulSoup(wheather_source, "html.parser")
        temp = wheather_soup.select(".todaytemp")
        temp_sub = wheather_soup.select(".cast_txt")
        self.Weather.setStyleSheet("background-color : white;font : 75 22pt; border-top-right-radius: 15px; border-top-left-radius: 15px;")
        self.Weather_1.setStyleSheet("font : 75 15pt; background-color : white; border-bottom-right-radius: 15px; border-bottom-left-radius: 15px;")
        self.Weather.setText( temp[0].text + "℃\n")
        self.Weather_1.setText(temp_sub[0].text)

        # 현재시간 가지고 오기
        self.timer = QTimer()
        self.timer.start(1000)# 1초마다 가져오기
        self.timer.timeout.connect(self.time_crolling)

def time_crolling(self):
    clock =0
    clock = datetime.today()
    self.now_time.setStyleSheet("font : 75 25pt; background-color : white; border-radius : 15px;")
    if clock.hour >= 12:
        if clock.second >= 10 and clock.minute >=10:
            self.now_time.setText("PM " + str(clock.hour) + " : " + str(clock.minute) + " : " + str(clock.second))
        elif clock.second >= 10 and clock.minute <= 10:
            self.now_time.setText("PM " + str(clock.hour) + " : 0" + str(clock.minute) + " : " + str(clock.second))
        elif clock.second <= 10 and clock.minute >= 10:
            self.now_time.setText("PM " + str(clock.hour) + " : " + str(clock.minute) + " : 0" + str(clock.second))
        if clock.second <= 10 and clock.minute <= 10:
            self.now_time.setText("PM " + str(clock.hour) + " : 0" + str(clock.minute) + " : 0" + str(clock.second))

    else:
        if clock.second >= 10 and clock.minute >=10:
            self.now_time.setText("AM " + str(clock.hour) + " : " + str(clock.minute) + " : " + str(clock.second))
        elif clock.second >= 10 and clock.minute <= 10:
            self.now_time.setText("AM " + str(clock.hour) + " : " + str(clock.minute) + " : " + str(clock.second))
        elif clock.second <= 10 and clock.minute >= 10:
            self.now_time.setText("AM " + str(clock.hour) + " : " + str(clock.minute) + " : " + str(clock.second))
        if clock.second <=10 and clock.minute <= 10:
            self.now_time.setText("AM " + str(clock.hour) + " : " + str(clock.minute) + " : " + str(clock.second))        

#def news_crolling(self):
 #   news_source = requests.get("https://www.naver.com/").text
  #  news_soup = BeautifulSoup(news_source, "html.parser")
   # temp = news_soup.select(".keyword")
    #self.news.setText(temp[].text)





Ui_MainWindow.time_crolling = time_crolling
Ui_MainWindow.wheather_crolling = wheather_crolling

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
   # ui.basic()
    ui.setupUi(MainWindow)
    ui.wheather_crolling()
    ui.time_crolling()
    MainWindow.show()
    sys.exit(app.exec_())
