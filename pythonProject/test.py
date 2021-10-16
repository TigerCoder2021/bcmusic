import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class Communicate(QObject):

    closeApp = pyqtSignal()


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('출결 현황 카카오톡 메세지 보내기')
        self.setWindowIcon(QIcon('bclogo_60_60.jpg'))
        self.setFixedSize(500, 250)

        btn1 = QPushButton('메시지 보내기', self)
        btn1.move(80, 13)
        btn2 = QPushButton('종료', self)
        btn2.move(80, 53)

        self.show()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())