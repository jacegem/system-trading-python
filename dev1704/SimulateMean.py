"""시뮬레이션 한다"""
import os
import sys
from datetime import datetime, timedelta
from dev1704.AnalyzeMean import *
from dev1704.AnalyzeBasic import *
from dev1704.AccountManager import *
from dev1704.DataManager import *
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
        self.editCode.setText('A023350')

        # 투자 최대 금액
        self.editMoneyMax = QLineEdit()
        self.gridLayout.addWidget(self.editMoneyMax, self.add_row(), 0)
        self.editMoneyMax.setText('1000000')

        # 시작날짜
        self.dateStart = QDateEdit()
        self.gridLayout.addWidget(self.dateStart, self.add_row(), 0)
        self.startDate = QDate(2017,1,1)
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

        # 결과 창
        self.logOutput = QTextEdit(parent)
        self.logOutput.setReadOnly(True)
        self.logOutput.setFixedWidth(800)
        self.logOutput.setLineWrapMode(QTextEdit.NoWrap)
        self.gridLayout.addWidget(self.logOutput, self.init_row(), self.add_col(), 6, 1)

    def add_log(self, text):
        """참고: http://stackoverflow.com/questions/16568451/pyqt-how-to-make-a-textarea-to-write-messages-to-kinda-like-printing-to-a-co"""
        print(text)
        self.logOutput.moveCursor(QTextCursor.End)
        # self.logOutput.setCurrentFont(font)
        # self.logOutput.setTextColor(color)
        self.logOutput.insertPlainText(text + "\n")
        sb = self.logOutput.verticalScrollBar()
        sb.setValue(sb.maximum())

    def add_row(self):
        self.gridRow += 1
        return self.gridRow

    def init_row(self):
        self.gridRow = 1
        return self.gridRow

    def add_col(self):
        self.gridCol += 1
        return self.gridCol

    def init_col(self):
        self.gridCol = 1
        return self.gridCol


    def showEvent(self, QShowEvent):
        """시작하면 데이터를 가져온다."""
        self.get_stock_data()

    def get_stock_data(self):
        self.code = self.editCode.text()
        money_max = self.editMoneyMax.text()
        self.start_datetime = self.get_datetime(self.dateStart.date())
        self.end_datetime = self.get_datetime(self.dateEnd.date())

        # 데이터 가져오기
        item_list = []
        item_list.append({'code': self.code, 'name': '테스트대상'})
        self.data_manager = DataManager(self.start_datetime, self.end_datetime)
        self.data_manager.set_item_list(item_list)

        # 계정 관리자
        self.account_manager = AccountManager(money_max, self.data_manager)

    def start_simulator(self):
        # 로그 지우기
        self.logOutput.clear()

        # 코드, 최대금액, 시작날짜 종료날짜, 시작
        # 코드 가져오기
        stock_data = self.data_manager.get_stock_data(self.code)

        # 분석 모듈
        # analyzer = AnalyzeMean(stock_data)
        analyzer = AnalyzeBasic(stock_data)
        target_date = self.start_datetime

        while target_date < self.end_datetime:
            # 오늘 몇일
            time_str = target_date.strftime("%Y-%m-%d")

            # 데이터가 있는가?
            if analyzer.has_data(target_date):
                adj_close = self.data_manager.get_adj_close(self.code, target_date)

                # 팔아야 할까?
                if analyzer.should_i_sell(target_date):
                    sell_price = self.account_manager.sell(self.code)
                    cash = self.account_manager.get_cash()
                    text = '{} : {} / 판매 / 판매금 : {} / 현금 : {}'.format(time_str, adj_close, sell_price, cash)
                    self.add_log(text)

                if analyzer.is_worth_buying(target_date):
                    # 얼마나 살수 있는가? # 최대 구매 금액 # 보유주 (수 + 량)
                    quantity = self.account_manager.get_buy_quantity(self.code, target_date)
                    self.account_manager.buy(self.code, adj_close, quantity)
                    # code, '구매', 가격, 수량, 보유주평가금액, 현금
                    stock_price = self.account_manager.get_stock_price(self.code)
                    cash = self.account_manager.get_cash()
                    text = '{} : {} / 구매 / 수량 : {} / 평가금 : {} / 현금 : {} / 합 : {}'.format(time_str, adj_close, quantity, stock_price, cash, stock_price + cash)
                    self.add_log(text)
            else:
                self.add_log(time_str + " : " + "데이터 없음")

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


