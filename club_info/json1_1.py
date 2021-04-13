import json
from club_join import *
from PyQt5.QtWidgets import *

class Manager:
    def __init__(self):
        self.infos = None
            # json 파일의 항목이름을 list로 정의 , json 파일의 항목 이름을 동일하게 가져오는 것임
        self.people_info_list = ['name_text', 'age_text', 'hometown_text', 'bloodtype_text', 'motto_text']
           # line edit Object name 정의 , designe의 object name
        self.people_lineEdits = [ui.name_text, ui.age_text, ui.hometown_text, ui.bloodtype_text, ui.motto_text]
        self.other_info_list = ['dream_text', 'favoritefood_text', 'favoritecolor_text', 'bucketlist_text']
           # line edit Object name 정의 , designe의 object name
        self.other_lineEdits = [ui.dream_text, ui.favoritefood_text, ui.favoritecolor_text, ui.bucketlist_text]
        ui.club_info.clicked.connect(lambda : self.set_info('other_info'))
        ui.club_info.clicked.connect(lambda: ui.stackedWidget.setCurrentIndex(1))
        ui.other_info.clicked.connect(lambda : self.set_info('club_info'))
        ui.other_info.clicked.connect(lambda: ui.stackedWidget.setCurrentIndex(0))
         # save 버튼 누르면 save_info() 함수 호출
        ui.other_bt.clicked.connect(lambda : self.save_info('other_info'))
        ui.club_bt.clicked.connect(lambda : self.save_info('club_info'))
                
        #json 파일을 읽어오기
        self.load_info()
            # 읽어온 json 파일 화면 표시
        self.set_info('club_info')
        self.set_info('other_info')
    def load_info(self):
           # json 정보 불러오기, info.json 파일을 읽어서 infos  객체로 불러옴
        with open('./info.json', 'r', encoding='utf-8') as info_file:
            self.infos = json.load(info_file)
    def save_info(self, page):
        if (page=='club_info') :
            print('save_club')
            for lineEdit, info in zip(self.people_lineEdits, self.people_info_list):
                self.infos['club_info'][info] = lineEdit.text()
            with open('./info.json', 'w', encoding='utf-8') as info_file:
                json.dump(self.infos, info_file, indent=4)
        elif (page=='other_info'):
            print('save_other')
            for lineEdit, info in zip(self.other_lineEdits, self.other_info_list):
                self.infos['other_info'][info] = lineEdit.text()
            with open('./info.json', 'w', encoding='utf-8') as info_file:
                json.dump(self.infos, info_file, indent=4)
        else:
            with open('./info.json', 'w', encoding='utf-8') as info_file:
                json.dump(self.infos, info_file, indent=4)
    def set_info(self, page):
        if page == 'club_info':
            print ('club_info')
            for lineEdit, info in zip(self.people_lineEdits, self.people_info_list):
                lineEdit.setText(self.infos['club_info'][info])
        else:
            print ('other_info')
            for lineEdit, info in zip(self.other_lineEdits, self.other_info_list):
                lineEdit.setText(self.infos['other_info'][info])

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    manager = Manager()
    MainWindow.show()
    app.exec_()
    manager.save_info('all')
    sys.exit()

