from DailyBIBLE import *
import requests
from bs4 import BeautifulSoup

def event(self):
    self.pushButton.clicked.connect(self.crolling)

def crolling(self):
        source = requests.get("http://bible.godpia.com/index.asp").text
        soup = BeautifulSoup(source, "html.parser")
        hotKeys = soup.select(".main-tit")
        subKeys = soup.select(".main-sub-tit")
        self.bible.append(hotKeys[0].text)
        self.bible.append(subKeys[0].text)



Ui_MainWindow.event = event
Ui_MainWindow.crolling = crolling


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.event()
    MainWindow.show()
    sys.exit(app.exec_())
