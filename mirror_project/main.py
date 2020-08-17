from mirror import *
import requests
from bs4 import BeautifulSoup
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTimer
from datetime import datetime
import threading

def timer_event(self):
    #now_time 
    self.timer = QTimer()
    self.timer.start(1000) #1초마다
    self.timer.timeout.connect(self.time_crolling)


def wheather_crolling(self):
        wheather_source = requests.get("https://search.naver.com/search.naver?sm=top_hty&fbm=1&ie=utf8&query=%EB%82%A0%EC%94%A8").text
        wheather_soup = BeautifulSoup(wheather_source, "html.parser")
        temp = wheather_soup.select(".todaytemp")
        temp_sub = wheather_soup.select(".cast_txt")
        self.Weather.setStyleSheet("background-color : rgb(255,255,255); font : 75 22pt; border-top-right-radius: 15px; border-top-left-radius: 15px;")
        self.Weather_1.setStyleSheet("background-color : rgb(255,255,255); font : 75 15pt;border-bottom-right-radius: 15px; border-bottom-left-radius: 15px;")
        self.Weather.setText( temp[0].text + "℃\n")
        self.Weather_1.setText(temp_sub[0].text)

def time_crolling(self):
    
    clock =0
    clock = datetime.today()
    self.now_time.setStyleSheet("background-color :  rgb(255, 167, 140); font : 75 25pt;  border-radius : 15px; ")
    if clock.hour >= 12:
        if clock.second >= 10 and clock.minute >=10:
            self.now_time.setText("PM " + str(clock.hour) + " : " + str(clock.minute) + " : " + str(clock.second))
        elif clock.second >= 10 and clock.minute <= 10:
            self.now_time.setText("PM " + str(clock.hour) + " : 0" + str(clock.minute) + " : " + str(clock.second))
        elif clock.second <= 10 and clock.minute >= 10:
            self.now_time.setText("PM " + str(clock.hour) + " : " + str(clock.minute) + " : 0" + str(clock.second))
        if clock.second <= 10 and clock.minute <= 10:
            self.now_time.setText("PM " + str(clock.hour) + " : 0" + str(clock.minute) + " : 0" + str(clock.second))

    elif clock.hour == 0:
        if clock.second >= 10 and clock.minute >=10:
            self.now_time.setText("AM  0" + str(clock.hour) + " : " + str(clock.minute) + " : " + str(clock.second))
        elif clock.second >= 10 and clock.minute <= 10:
            self.now_time.setText("AM  0" + str(clock.hour) + " : 0" + str(clock.minute) + " : " + str(clock.second))
        elif clock.second <= 10 and clock.minute >= 10:
            self.now_time.setText("AM  0" + str(clock.hour) + " : " + str(clock.minute) + " : 0" + str(clock.second))
        if clock.second <=10 and clock.minute <= 10:
            self.now_time.setText("AM " + str(clock.hour) + " : 0" + str(clock.minute) + " : 0" + str(clock.second))

    else:
        if clock.second >= 10 and clock.minute >=10:
            self.now_time.setText("AM  0" + str(clock.hour) + " : " + str(clock.minute) + " : " + str(clock.second))
        elif clock.second >= 10 and clock.minute <= 10:
            self.now_time.setText("AM  0" + str(clock.hour) + " : 0" + str(clock.minute) + " : " + str(clock.second))
        elif clock.second <= 10 and clock.minute >= 10:
            self.now_time.setText("AM  0" + str(clock.hour) + " : " + str(clock.minute) + " : 0" + str(clock.second))
        if clock.second <=10 and clock.minute <= 10:
            self.now_time.setText("AM " + str(clock.hour) + " : 0" + str(clock.minute) + " : 0" + str(clock.second))
        
    
        

def news_crolling(self):
    self.topic.setStyleSheet("font : 75 12pt; ")
    news_source =requests.get("https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=%EB%89%B4%EC%8A%A4%ED%86%A0%ED%94%BD&oquery=%EB%84%A4%EC%9D%B4%EB%B2%84+%EC%8B%A4%EC%8B%9C%EA%B0%84+%EA%B2%80%EC%83%89%EC%96%B4+%EC%88%9C%EC%9C%84&tqi=UzQlmwp0J14ssflcJlsssssssHR-396770").text
    news_soup = BeautifulSoup(news_source, "html.parser")
    sub_key = news_soup.select("span.tit")

    index = 0
    key=2
    self.topic.append("뉴스")
    for key in sub_key:
        index += 1
        self.topic.append("["+ str(index) + "]  "+str(key))
        if index >= 5:
            break
    
    index = 0
    key = 1
    cnt = 1
    self.topic.append("\n연예/스포츠")
    for key in sub_key:
        index += 1
        if index >=11:
            self.topic.append("["+ str(cnt) + "]  "+str(key))
            cnt += 1
            if index >= 15:
                break
    
   
def baseball_crolling(self):
    self.sports.setStyleSheet("font : 75 12pt;")
    baseball_source = requests.get("https://sports.media.daum.net/sports/baseball/").text
    baseball_soup = BeautifulSoup(baseball_source,"html.parser")
    rank = baseball_soup.select("span.txt_team")
    self.sports.append("2020 프로야구 순위")
    
    index = 0
    for i in rank:
        index +=1
        #print(str(index))
        self.sports.append(str(index)+"등 "+str(i))
        if index >= 10:
            break


def Myinfo(self):
    self.myinfo.append("기본 프로필")
    self.myinfo.append("2002.06.14 김민영")
    self.myinfo.append("대덕소프트웨어마이스터")
    self.myinfo.append("임베디드SW 재학")


def diner(self):
    diner_source = requests.get("https://www.dsm-dms.com/").text
    diner_soup = BeautifulSoup(diner_source, "html.parser")
    blackfirst = diner_soup.select("span.meal--card--temp")
    self.diner_moring.append("아침")

    cnt = 0
    for i in blackfirst:
        cnt += 1
        print(cnt)
        self.diner_moring.append(str(i))
        if index >= 2:
            break



Ui_MainWindow.timer_event = timer_event
Ui_MainWindow.wheather_crolling = wheather_crolling
Ui_MainWindow.time_crolling = time_crolling
Ui_MainWindow.news_crolling = news_crolling
Ui_MainWindow.baseball_crolling =baseball_crolling
Ui_MainWindow.diner = diner
Ui_MainWindow.Myinfo = Myinfo


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.timer_event()
    ui.setupUi(MainWindow)
    ui.wheather_crolling()
    ui.time_crolling()
    ui.news_crolling()
    ui.baseball_crolling()
    ui.diner()
    ui.Myinfo()
    MainWindow.show()
    sys.exit(app.exec_())
