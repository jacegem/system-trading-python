import os
import sys

from qt.DataManager import *
from qt.AnalyzeMean import *
from PyQt5.QtWidgets import *

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
    # 분석 전략 구분
    ANALYZE_MEAN = 'mean'

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
        self.tbItem = QTableWidget()
        self.tbItem.setColumnCount(2)
        self.tbItem.setHorizontalHeaderLabels(['코드', '이름'])
        self.gridLayout.addWidget(self.tbItem, 3, 0)

        # 분석 선택 콤보
        self.cbAnalyze = QComboBox()
        self.cbAnalyze.addItem("평균 반등", self.ANALYZE_MEAN)
        self.cbAnalyze.addItem("다음 전략", 'a')
        self.cbAnalyze.addItem("Perl")
        self.cbAnalyze.addItem("Java")
        self.cbAnalyze.addItem("C++")
        self.gridLayout.addWidget(self.cbAnalyze, 0, 1)

        # 분석 시작 버튼
        self.btnAnalyze = QPushButton("종목분석")
        self.btnAnalyze.clicked.connect(self.itemAnalyze)
        self.gridLayout.addWidget(self.btnAnalyze, 1, 1)

        # 분석 결과 테이블
        self.tbAnalyze = QTableWidget()
        self.tbAnalyze.setColumnCount(3)
        self.tbAnalyze.setHorizontalHeaderLabels(['코드', '이름', '예상값'])
        self.gridLayout.addWidget(self.tbAnalyze, 3, 1)

        # 시작시 버튼 클릭
        #self.readList()

    def itemAnalyze(self):
        """전체 대상에 대해서 분석합니다"""
        # 데이터 가져오기
        datas = self.dm.get_stock_datas()

        # 분석 타입 가져오기
        cbData = self.cbAnalyze.itemData(self.cbAnalyze.currentIndex())

        if (cbData == self.ANALYZE_MEAN):
            print(cbData)
            mean = AnalyzeMean(datas)           # 설정값들을 파라미터로 전송
            result = mean.get_result()

        # 테이블의 모든 정보를 지운다.
        self.tbAnalyze.setRowCount(0)

        for key, value in result.itmes():
            row = self.tbItem.rowCount()
            self.tbAnalyze.insertRow(row)
            self.tbAnalyze.setItem(row, 0, QTableWidgetItem(result.get_code))
            self.tbAnalyze.setItem(row, 1, QTableWidgetItem(result.get_name))
            self.tbAnalyze.setItem(row, 2, QTableWidgetItem(result.get_result))

        # 상태표시로 알려준다.
        sender = self.sender()
        self.parent.changeStatusBar(sender.text() + ' was pressed')

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

        # 테이블의 모든 정보를 지운다.
        self.tbItem.setRowCount(0)

        # 화면에 표출한다.
        for item in item_list:
            row = self.tbItem.rowCount()
            self.tbItem.insertRow(row)
            self.tbItem.setItem(row, 0, QTableWidgetItem(item['code']))
            self.tbItem.setItem(row, 1, QTableWidgetItem(item['name']))

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