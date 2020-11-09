from mirror import *
from schapi import SchoolAPI
import requests
from bs4 import BeautifulSoup
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTimer
from datetime import datetime
import calendar
from multiprocessing import Process


def timer_event(self):
    #now_time 
    self.timer = QTimer()
    self.timer.start(1000) #1초마다
    self.timer.timeout.connect(self.time_crolling)

def dinner_event(self):
    self.timer2 = QTimer()
    self.timer2.start(1000)
    self.timer2.timeout.connect(self.meal)

def wheather_event(self):
    self.timer3 = QTimer()
    self.timer3.start(60000) #1분마다
    self.timer3.timeout.connect(self.wheather_crolling)

def news_event(self):
    self.timer4 = QTimer()
    self.timer4.start(60000) #1분마다
    self.timer4.timeout.connect(self.news_crolling)

def todo_event(self):
    self.timer5 = QTimer()
    self.timer5.start(1000)
    self.timer5.timeout.connect(self.todo)

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
    self.now_time.setStyleSheet(" background-color : rgb(255, 170, 127); font : 75 25pt;  border-radius : 15px; ")
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
            self.now_time.setText("AM 0" + str(clock.hour) + " : 0" + str(clock.minute) + " : 0" + str(clock.second))

    elif clock.hour <= 10:
        if clock.second >= 10 and clock.minute >=10:
            self.now_time.setText("AM  0" + str(clock.hour) + " : " + str(clock.minute) + " : " + str(clock.second))
        elif clock.second >= 10 and clock.minute <= 10:
            self.now_time.setText("AM  0" + str(clock.hour) + " : 0" + str(clock.minute) + " : " + str(clock.second))
        elif clock.second <= 10 and clock.minute >= 10:
            self.now_time.setText("AM  0" + str(clock.hour) + " : " + str(clock.minute) + " : 0" + str(clock.second))
        if clock.second <=10 and clock.minute <= 10:
            self.now_time.setText("AM " + str(clock.hour) + " : 0" + str(clock.minute) + " : 0" + str(clock.second))
    
    elif clock.hour >= 10 and clock.hour <=12:
        if clock.second >= 10 and clock.minute >=10:
            self.now_time.setText("AM  " + str(clock.hour) + " : " + str(clock.minute) + " : " + str(clock.second))
        elif clock.second >= 10 and clock.minute <= 10:
            self.now_time.setText("AM  " + str(clock.hour) + " : 0" + str(clock.minute) + " : " + str(clock.second))
        elif clock.second <= 10 and clock.minute >= 10:
            self.now_time.setText("AM  " + str(clock.hour) + " : " + str(clock.minute) + " : 0" + str(clock.second))
        if clock.second <=10 and clock.minute <= 10:
            self.now_time.setText("AM " + str(clock.hour) + " : 0" + str(clock.minute) + " : 0" + str(clock.second))
        
    
        

def news_crolling(self):
    #self.topic.setStyleSheet("font : 75 12pt; ")
    news_source =requests.get("https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=%EB%89%B4%EC%8A%A4%ED%86%A0%ED%94%BD&oquery=%EB%84%A4%EC%9D%B4%EB%B2%84+%EC%8B%A4%EC%8B%9C%EA%B0%84+%EA%B2%80%EC%83%89%EC%96%B4+%EC%88%9C%EC%9C%84&tqi=UzQlmwp0J14ssflcJlsssssssHR-396770").text
    news_soup = BeautifulSoup(news_source, "html.parser")
    sub_key = news_soup.select("span.tit")

    index = 0
    key= 1
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
    #self.sports.setStyleSheet("font : 75 12pt;")
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


def todo(self):
    
    self.todolist.setStyleSheet("border-bottom : 2px solid gray; background-color : white; font : 100 22pt;")
    self.todolist.setAlignment(QtCore.Qt.AlignCenter)
 


def meal(self):
    self.diner_moring.clear()
    date = self.calendar.selectedDate() #QDate 타입
    print(date)
    clock2 = datetime.today()
    api = SchoolAPI(SchoolAPI.Region.DAEJEON, 'G100000170')
    meals = api.get_monthly_menus(date.year(), date.month())

    
    if clock2.hour >=6 and clock2.hour <=10:
        self.diner_moring.append("<아침 메뉴>")
        self.diner_moring.append('\n'.join(meals[10].breakfast)) # 아침 : breakfast 점심 : lunch 저녁 : dinner
    elif clock2.hour >= 11 and clock2.hour <= 14:
        self.diner_moring.append("<점심 메뉴>")
        self.diner_moring.append('\n'.join(meals[10].lunch)) # 아침 : breakfast 점심 : lunch 저녁 : dinner
    else:
        self.diner_moring.append("<저녁 메뉴>")
        self.diner_moring.append('\n'.join(meals[10].dinner))
   
   

Ui_MainWindow.timer_event = timer_event
Ui_MainWindow.wheather_crolling = wheather_crolling
Ui_MainWindow.time_crolling = time_crolling
Ui_MainWindow.news_crolling = news_crolling
Ui_MainWindow.baseball_crolling =baseball_crolling
Ui_MainWindow.meal = meal
Ui_MainWindow.todo = todo
Ui_MainWindow.news_event = news_event
Ui_MainWindow.wheather_event = wheather_event
Ui_MainWindow.dinner_event = dinner_event


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
    
    ui.todo()
    ui.news_event()
    ui.wheather_event()
    ui.dinner_event()
    MainWindow.show()
    sys.exit(app.exec_())
