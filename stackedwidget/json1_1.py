import json
from club_join import *

class Manager:
    def __init__(self):
        self.infos = None
            # json 파일의 항목이름을 list로 정의 , json 파일의 항목 이름을 동일하게 가져오는 것임
        self.people_info_list = ['name_text', 'age_text', 'hometown_text', 'bloodtype_text', 'motto_text']
           # line edit Object name 정의 , designe의 object name
        self.people_lineEdits = [ui.name_text, ui.age_text, ui.hometown_text, ui.bloodtype_town, ui.motto_text]

        ui.save_bt.clicked.connect(self.save_info)         # save 버튼 누르면 save_info() 함수 호출
             #json 파일을 읽어오기
        self.load_info()
            # 읽어온 json 파일 화면 표시
        self.set_info()

    def load_info(self):
           # json 정보 불러오기, info.json 파일을 읽어서 infos  객체로 불러옴
        with open('./info.json', 'r', encoding='utf-8') as info_file:
            self.infos = json.load(info_file)
    def save_info(self):
        print ('save data')
        for lineEdit, info in zip(self.people_lineEdits, self.people_info_list):
                self.infos[info] = lineEdit.text()
        with open('./info.json', 'w', encoding='utf-8') as info_file:
                json.dump(self.infos, info_file, indent=4)        # List 변수 값들을 json 파일에 씀 
    def set_info(self):
        for lineEdit, info in zip(self.people_lineEdits, self.people_info_list):
                lineEdit.setText(self.infos[info])
if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    manager = Manager()
    MainWindow.show()
    app.exec_()
    sys.exit()
