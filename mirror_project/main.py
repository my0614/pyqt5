from mirror import *
import requests
from bs4 import BeautifulSoup


def wheather_crolling(self):
        wheather_source = requests.get("https://search.naver.com/search.naver?sm=top_hty&fbm=1&ie=utf8&query=%EB%82%A0%EC%94%A8").text
        wheather_soup = BeautifulSoup(wheather_source, "html.parser")
        temp = soup.select(".todaytemp")
        temp_sub = soup.select(".cast_txt")
        self.Weather.setStyleSheet("background-color : white;font : 75 30pt;")
        self.Weather_1.setStyleSheet("font : 75 15pt; background-color : white;")
        self.Weather.setText(temp[0].text + "℃\n")
        self.Weather_1.setText(temp_sub[0].text)

#def time_crolling(self):
 #   time_source = requests.get("https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=%EC%8B%9C%EA%B0%84&oquery=%EB%82%A0%EC%94%A8&tqi=UzkuasprvTossifqjFsssssstbo-426794").text
  #  time_soup = BeautifulSoup(time_source, "html.parser")
   # time = soup.select(".")
   # self.now_time.display(3)
        

# Ui_MainWindow.event = event
Ui_MainWindow.wheather_crolling = wheather_crolling

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.wheather_crolling()
    MainWindow.show()
    sys.exit(app.exec_())
