# http://pythonstudy.xyz/python/article/103-PyQt-%EC%9C%84%EC%A0%AF
# http://stackoverflow.com/questions/10082299/qvboxlayout-how-to-vertically-align-widgets-to-the-top-instead-of-the-center
# http://stackoverflow.com/questions/805066/call-a-parent-classs-method-from-child-class-in-python


import sys

from PyQt5.QtCore import *
from PyQt5.QtGui import *

from qt.backup.QPlainTextEditLogger import *


class MyMainWindow(QMainWindow):

    def __init__(self, parent=None):
        super(MyMainWindow, self).__init__(parent)
        self.form_widget = FormWidget(self)
        self.setCentralWidget(self.form_widget)
        self.statusBar().showMessage('Ready')

    def changeStatusBar(self, msg):
        self.statusBar().showMessage(msg)


class FormWidget(QWidget):

    def __init__(self, parent):
        super(FormWidget, self).__init__(parent)
        self.parent = parent

        self.btnQueryList = QPushButton("종목조회")

        self.btnReadList = QPushButton("목록불러오기")
        self.btnReadList.clicked.connect(self.readList)

        self.button1 = QPushButton("Button 1")
        self.button2 = QPushButton("Button 2")

        self.textEdit = QPlainTextEdit()
        self.textEdit.setReadOnly(True)
        self.testButton = QPushButton("테스트")
        self.testButton.clicked.connect(self.test)

        # self.layout = QVBoxLayout(self)
        # self.layout.addWidget(self.btnQueryList)
        # self.layout.addWidget(self.button1)
        # self.layout.addWidget(self.button2)

        self.gridLayout = QGridLayout(self)
        self.gridLayout.addWidget(self.btnQueryList, 0, 0)
        self.gridLayout.addWidget(self.btnReadList, 1, 0)
        self.gridLayout.addWidget(self.testButton, 2, 0, Qt.AlignVCenter)
        self.gridLayout.addWidget(self.textEdit, 0, 1, 2, 1)


        # self.setLayout(self.gridLayout)

    def readList(self):
        """파일을 읽어서, 리스트 위젯에 담는다"""
        file = '..\\data\\kospi.csv'
        result = []

        f = open(file, 'rt')
        lines = f.readlines()
        for line in lines:
            datas = line.split(',')
            code = datas[0]
            name = datas[1]
            result.append({'code': code.strip(), 'name': name.strip()})
        f.close()

        sender = self.sender()
        self.parent.changeStatusBar(sender.text() + ' was pressed')

    def test(self):
        self.textEdit.appendPlainText('damn, a bug')
        sender = self.sender()
        self.parent.changeStatusBar(sender.text() + ' was pressed')

if __name__ == "__main__":
    app = QApplication([])
    foo = MyMainWindow()
    foo.show()
    sys.exit(app.exec_())