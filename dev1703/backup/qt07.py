import os
import sys

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

        self.gridLayout = QGridLayout(self)

        # 종목 생성 버튼
        self.btnQueryList = QPushButton("종목파일생성")
        self.btnQueryList.clicked.connect(self.writeFile)
        self.gridLayout.addWidget(self.btnQueryList, 0, 0)

        # 종목 읽기 버튼
        self.btnReadList = QPushButton("종목파일읽기")
        self.btnReadList.clicked.connect(self.readList)
        self.gridLayout.addWidget(self.btnReadList, 1, 0)

        # 종목 테이블
        self.itemTable = QTableWidget()
        self.itemTable.setColumnCount(2)
        self.itemTable.setHorizontalHeaderLabels(['코드', '이름'])
        self.gridLayout.addWidget(self.itemTable, 3, 0)

        # 분석 시작 버튼
        combo = QComboBox()
        combo.addItem("평균 반등", 'mean')
        combo.addItem("다음 전략", 'a')
        combo.addItem("Perl")
        combo.addItem("Java")
        combo.addItem("C++")
        self.gridLayout.addWidget(combo, 0, 1)

        # 분석 시작 버튼
        self.btnAnalyze = QPushButton("종목분석")
        self.btnAnalyze.clicked.connect(self.itemAnalyze)
        self.gridLayout.addWidget(self.btnAnalyze, 1, 1)

        # 분석 결과 테이블
        self.analyzeTable = QTableWidget()
        self.analyzeTable.setColumnCount(3)
        self.analyzeTable.setHorizontalHeaderLabels(['코드', '이름', '예상값'])
        self.gridLayout.addWidget(self.analyzeTable, 3, 1)

    def itemAnalyze(self):
        # 전체 대상 분석
        pass


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
        rel_path = '../data/kospi.csv'

        script_dir = os.path.dirname(__file__)  # <-- absolute dir the script is in
        abs_file_path = os.path.join(script_dir, rel_path)

        # 만약 파일이 열러지 않는다면
        # 다른 프로세스에서 파일을 제어하고 있는지 확인 필요
        item_list = []
        with open(abs_file_path, 'r') as f:
            for line in f:
                datas = line.split(',')
                code = datas[0]
                name = datas[1]
                item_list.append({'code': code.strip(), 'name': name.strip()})

        # 화면에 표출한다.
        for item in item_list:
            row = self.itemTable.rowCount()
            self.itemTable.insertRow(row)
            self.itemTable.setItem(row, 0, QTableWidgetItem(item['code']))
            self.itemTable.setItem(row, 1, QTableWidgetItem(item['name']))

        # 종목 데이터를 메모리에 보관한다
        self.dm.set_item_list(item_list)

        # 상태표시로 알려준다.
        sender = self.sender()
        self.parent.changeStatusBar(sender.text() + ' was pressed')


if __name__ == "__main__":
    app = QApplication([])
    foo = MyMainWindow()
    foo.show()
    sys.exit(app.exec_())