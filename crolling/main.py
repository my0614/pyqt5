from test import *
import requests
from bs4 import BeautifulSoup

def crolling(self):
        source = requests.get("https://hoc43.ebssw.kr/dsm202023/hmpg/hmpgAlctcrListView.do?menuSn=385047").text
        soup = BeautifulSoup(source, "html.parser")
        hotKeys = soup.select(".ellip ellip-line")

        self.label.setText(hotKeys[0].text)
      


Ui_MainWindow.crolling = crolling


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.crolling()
    MainWindow.show()
    sys.exit(app.exec_())
