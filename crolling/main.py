from test import *
import requests
from bs4 import BeautifulSoup

def crolling(self):
        source = requests.get("http://bible.godpia.com/index.asp").text
        soup = BeautifulSoup(source, "html.parser")
        hotKeys = soup.select(".main-tit")

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
