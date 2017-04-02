# http://pythonstudy.xyz/python/article/103-PyQt-%EC%9C%84%EC%A0%AF
# http://stackoverflow.com/questions/10082299/qvboxlayout-how-to-vertically-align-widgets-to-the-top-instead-of-the-center
# http://stackoverflow.com/questions/805066/call-a-parent-classs-method-from-child-class-in-python


# QTableWidget
# https://wikidocs.net/5240
# http://stackoverflow.com/questions/26620191/adding-dynamically-a-row-in-a-qtablewidget

import os
import sys

from PyQt5.QtCore import *
from PyQt5.QtGui import *

from qt.DataManager import DataManager
from qt.backup.QPlainTextEditLogger import *


class MyMainWindow(QMainWindow):

    def __init__(self, parent=None):
        super(MyMainWindow, self).__init__(parent)
        self.dm = DataManager()
        self.form_widget = FormWidget(self, self.dm)
        self.setCentralWidget(self.form_widget)
        self.statusBar().showMessage('Ready')


    def changeStatusBar(self, msg):
        self.statusBar().showMessage(msg)


class FormWidget(QWidget):
    def __init__(self, parent, dm):
        super(FormWidget, self).__init__(parent)
        self.parent = parent
        self.dm = dm

        self.btnQueryList = QPushButton("종목파일생성")
        self.btnQueryList.clicked.connect(self.writeFile)

        self.btnReadList = QPushButton("종목파일읽기")
        self.btnReadList.clicked.connect(self.readList)

        self.button1 = QPushButton("Button 1")
        self.button2 = QPushButton("Button 2")

        self.textEdit = QPlainTextEdit()
        self.textEdit.setReadOnly(True)
        self.testButton = QPushButton("테스트")
        self.testButton.clicked.connect(self.test)

        self.itemTable = QTableWidget()
        # self.itemTableModel = QStandardItemModel()
        # self.itemTableModel.setHorizontalHeaderLabels((['코드', '이름']))
        # self.itemTable.setModel(self.itemTableModel)
        self.itemTable.setColumnCount(2)
        self.itemTable.setHorizontalHeaderLabels(['코드', '이름'])

        # table.setHorizontalHeaderLabels(QString("HEADER 1,HEADER 2,HEADER 3").split(","))

        # self.tableWidget.insertRow(self.tableWidget.rowCount())
        # self.itemTable.setRowCount(2)
        # self.itemTable.setColumnCount(2)
        # self.itemTable.setItem(0, 0, QTableWidgetItem("(0,0)"))
        # self.itemTable.setItem(0, 1, QTableWidgetItem("(0,1)"))
        # self.itemTable.setItem(1, 0, QTableWidgetItem("(1,0)"))
        # self.itemTable.setItem(1, 1, QTableWidgetItem("(1,1)"))

        self.gridLayout = QGridLayout(self)
        self.gridLayout.addWidget(self.btnQueryList, 0, 0)
        self.gridLayout.addWidget(self.btnReadList, 1, 0)
        self.gridLayout.addWidget(self.testButton, 2, 0, Qt.AlignVCenter)
        self.gridLayout.addWidget(self.textEdit, 0, 1, 2, 1)

        self.gridLayout.addWidget(self.itemTable, 3, 0)
        # self.setLayout(self.gridLayout)


    def writeFile(self):
        f = open('../data/testkospi.csv', 'w')
        f.write("%s,%s\n" % ('key', 'value'))
        f.close()

    def printPath(self):
        print(os.getcwd())  # 현재 디렉토리의
        print(os.path.realpath(__file__))  # 파일
        print(os.path.dirname(os.path.realpath(__file__)))  # 파일이 위치한 디렉토리

    def readList(self):
        """파일을 읽어서, 리스트 위젯에 담는다"""
        self.printPath()
        #file = '..\\data\\kospi.csv'
        #rel_path = '../data/testkospi.csv'
        rel_path = '../data/kospi.csv'

        script_dir = os.path.dirname(__file__)  # <-- absolute dir the script is in
        abs_file_path = os.path.join(script_dir, rel_path)

        # 만약 파일이 열러지 않는다면
        # 다른 프로세스에서 파일을 제어하고 있는지 확인 필요
        itemList = []
        with open(abs_file_path, 'r') as f:
            for line in f:
                datas = line.split(',')
                code = datas[0]
                name = datas[1]
                itemList.append({'code': code.strip(), 'name': name.strip()})

        # 종목 데이터를 메모리에 보관한다
        self.dm.setItemList(itemList)

        self.itemTable.setItem(0, 0, QTableWidgetItem("(0,0)"))
        self.itemTable.setItem(0, 1, QTableWidgetItem("(0,1)"))
        self.itemTable.setItem(1, 0, QTableWidgetItem("(1,0)"))
        self.itemTable.setItem(1, 1, QTableWidgetItem("(1,1)"))

        # 화면에 표출한다.
        for item in itemList:
            row = self.itemTable.rowCount()
            self.itemTable.insertRow(row)
            self.itemTable.setItem(row, 0, QTableWidgetItem(item['code']))
            self.itemTable.setItem(row, 1, QTableWidgetItem(item['name']))

        # 상태표시로 알려준다.
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