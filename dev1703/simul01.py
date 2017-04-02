"""시뮬레이션 한다"""
import os
import sys

from qt.AnalyzeMean import *
from qt.DataManager import *
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

    def __init__(self, parent, dm):
        super(FormWidget, self).__init__(parent)

        self.gridLayout = QGridLayout(self)

        # 대상 (코드)
        # 시작날짜
        # 종료날짜
        # 종목 최대 보유금액

        self.gridRow = 0
        self.gridCol = 0

        # 대상 (코드)
        self.editCode = QLineEdit()
        self.gridLayout.addWidget(self.editCode, self.add_row(), 0)
        self.editCode.setText('A018670')

        # 대상 (코드)
        self.editMoneyMax = QLineEdit()
        self.gridLayout.addWidget(self.editMoneyMax, self.add_row(), 0)
        self.editMoneyMax.setText('1000000')

        # 시작날짜
        self.dateStart = QDateEdit()
        self.gridLayout.addWidget(self.dateStart, self.add_row(), 0)
        self.startDate = QDate(2010,1,2)
        self.dateStart.setDate(self.startDate)

        # 종료날짜
        self.dateEnd = QDateEdit()
        self.gridLayout.addWidget(self.dateEnd, self.add_row(), 0)
        self.endDate = QDate(QDate.currentDate())
        self.dateEnd.setDate(self.endDate)

        # 시작 버튼
        self.btnStart = QPushButton("시작")
        self.btnStart.clicked.connect(self.start_simulator)
        self.gridLayout.addWidget(self.btnStart, self.add_row(), 0)

    def add_row(self):
        self.gridRow += 1
        return self.gridRow

    def add_col(self):
        self.gridCol += 1
        return self.gridCol

    def start_simulator(self):
        # 코드, 최대금액, 시작날짜 종료날짜, 시작
        # 코드 가져오기
        code = self.editCode.text()
        moneyMax = self.editMoneyMax.text()
        startDate = self.dateStart.date()
        endDate = self.dateEnd.date()

        # 데이터 가져오기
        item_list = []
        item_list.append({'code': code, 'name': '테스트대상'})

        # 시작, 종료
        data_manager = DataManager(startDate, endDate)
        data_manager.set_item_list(item_list)

        analyzeMean = AnalyzeMean()
        targetDate = startDate
        while targetDate < datetime:
            # 날짜, 데이터, 살까, 팔까?
            if analyzeMean.isWorthBuying(code, targetDate, stockData):
            # 구입 최대금액 구하기
            targetDate =targetDate.addDays(1)








if __name__ == "__main__":
    app = QApplication([])
    dialog = MyMainWindow()
    dialog.show()
    sys.exit(app.exec_())


