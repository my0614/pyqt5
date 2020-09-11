from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class add_page(QtWidget):
    def __init__(self, pager = None):
        super().__init__()
        self.pager = pager

    def mousePressEvent(slef, event):
        self.pager.emit(0)

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    ui = add_page()
    ui.show()
    sys.exit(app.exec_())