from mirror import *
import requests
from bs4 import BeautifulSoup
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTimer
from datetime import datetime
import threading

def Timer_event(self):
    #반복기능_ time
    self.timer = QTimer()
    self.timer.start(1000) #1초마다
    self.timer.timeout.connect(time_crolling)

    #반복기능_ wheather
    self.timer = QTimer()
    self.timer.start(10000) # 10초마다
    self.timer.timeout.connect(wheather_crolling)

    #반복기능_ news
    self.timer = QTimer()
    self.timer.start(60000) # 1분마다
    self.timer.timeout.connect(news_crolling)



def wheather_crolling(self):
        wheather_source = requests.get("https://search.naver.com/search.naver?sm=top_hty&fbm=1&ie=utf8&query=%EB%82%A0%EC%94%A8").text
        wheather_soup = BeautifulSoup(wheather_source, "html.parser")
        temp = wheather_soup.select(".todaytemp")
        temp_sub = wheather_soup.select(".cast_txt")
        self.Weather.setStyleSheet("background-color : white;font : 75 22pt; border-top-right-radius: 15px; border-top-left-radius: 15px;")
        self.Weather_1.setStyleSheet("font : 75 15pt; background-color : white; border-bottom-right-radius: 15px; border-bottom-left-radius: 15px;")
        self.Weather.setText( temp[0].text + "℃\n")
        self.Weather_1.setText(temp_sub[0].text)




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
        # new_crolling 반복      
        self.timer = QTimer()
        self.timer.start(10000)# 10초마다 가져오기
        self.timer.timeout.connect(self.news_crolling)

def news_crolling(self):
    news_source =requests.get("https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=%EB%89%B4%EC%8A%A4%ED%86%A0%ED%94%BD&oquery=%EB%84%A4%EC%9D%B4%EB%B2%84+%EC%8B%A4%EC%8B%9C%EA%B0%84+%EA%B2%80%EC%83%89%EC%96%B4+%EC%88%9C%EC%9C%84&tqi=UzQlmwp0J14ssflcJlsssssssHR-396770").text
    news_soup = BeautifulSoup(news_source, "html.parser")
    sub_key = news_soup.select("span.tit")

    index = 0
    key=2
    self.news.append("뉴스")
    for key in sub_key:
        index += 1
        self.news.append("["+ str(index) + "]  "+str(key))
        if index >= 5:
            break
    
    index = 0
    key = 1
    cnt = 1
    self.news.append("\n연예/스포츠")
    for key in sub_key:
        index += 1
        if index >=11:
            self.news.append("["+ str(cnt) + "]  "+str(key))
            cnt += 1
            if index >= 15:
                break

        


Ui_MainWindow.Timer_event = Timer_event
Ui_MainWindow.time_crolling = time_crolling
Ui_MainWindow.wheather_crolling = wheather_crolling
Ui_MainWindow.news_crolling = news_crolling


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.Timer_event()
    ui.wheather_crolling()
    ui.time_crolling()
    ui.news_crolling()
    MainWindow.show()
    sys.exit(app.exec_())
