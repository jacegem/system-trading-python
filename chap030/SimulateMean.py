"""시뮬레이션 한다"""
import os
import sys
from datetime import datetime, timedelta
from chap030.AnalyzeMean import *
from chap030.DataManager import *
from PyQt5.QtWidgets import *

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
        self.startDate = QDate(2017,3,1)
        self.dateStart.setDate(self.startDate)

        # 종료날짜
        self.dateEnd = QDateEdit()
        self.gridLayout.addWidget(self.dateEnd, self.add_row(), 0)
        self.endDate = QDate(QDate.currentDate())
        self.dateEnd.setDate(self.endDate)

        # 시작 버튼
        self.btnStart = QPushButton("데이터 가져오기")
        self.btnStart.clicked.connect(self.get_stock_data)
        self.gridLayout.addWidget(self.btnStart, self.add_row(), 0)

        # 분석 버튼
        self.btnStart = QPushButton("분석")
        self.btnStart.clicked.connect(self.start_simulator)
        self.gridLayout.addWidget(self.btnStart, self.add_row(), 0)

    def add_row(self):
        self.gridRow += 1
        return self.gridRow

    def add_col(self):
        self.gridCol += 1
        return self.gridCol

    def showEvent(self, QShowEvent):
        """시작하면 데이터를 가져온다."""
        self.get_stock_data()

    def get_stock_data(self):
        self.code = self.editCode.text()
        self.money_max = self.editMoneyMax.text()
        self.start_datetime = self.get_datetime(self.dateStart.date())
        self.end_datetime = self.get_datetime(self.dateEnd.date())

        # 데이터 가져오기
        item_list = []
        item_list.append({'code': self.code, 'name': '테스트대상'})
        self.data_manager = DataManager(self.start_datetime, self.end_datetime)
        self.data_manager.set_item_list(item_list)

    def start_simulator(self):
        # 코드, 최대금액, 시작날짜 종료날짜, 시작
        # 코드 가져오기

        #from datetime import datetime
        #datetime_object = datetime.strptime('Jun 1 2005  1:33PM', '%b %d %Y %I:%M%p')

        stock_data = self.data_manager.get_stock_data(self.code)

        # 분석 모듈
        analyze_mean = AnalyzeMean(stock_data)
        target_date = self.start_datetime

        while target_date < self.end_datetime:
            # 오늘 몇일
            # print(target_date)
            rst = analyze_mean.is_worth_buying(target_date)
            print(target_date, ":", rst)

            # 날짜, 데이터, 살까, 팔까?
            # if analyze_mean.is_worth_buying(target_date):
            #     pass
            # 구입 최대금액 구하기
            target_date = target_date + timedelta(days=1)

    @staticmethod
    def get_datetime(date):
        year = date.year()
        month = date.month()
        day = date.day()
        dt = datetime(year=year, month=month, day=day)
        return dt





if __name__ == "__main__":
    app = QApplication([])
    dialog = MyMainWindow()
    dialog.show()
    sys.exit(app.exec_())


