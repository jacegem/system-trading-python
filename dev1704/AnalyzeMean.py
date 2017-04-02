"""
이평선을 기준으로 분석한 결과를 반환합니다.
분석 수치는 100% 를 기준으로 50% 이상이면 구매 대상입니다
"""
from datetime import datetime, timedelta


class AnalyzeMean():
    ADJ_CLOSE = 'Adj Close'

    def __init__(self, stock_data):
        """이평선을 기준으로 구매 대상을 분석합니다"""
        self.stock_data = stock_data
        self.df = self.stock_data.get_df()

    def has_data(self, target_date):
        date_str = target_date.strftime('%Y-%m-%d')
        if date_str in self.df.index:
            return True
        else:
            return False


    def is_worth_buying(self, target_date):
        """사도 되는 것인지 판단"""
        # 대상 날짜의 인덱스를 얻는다.
        date_str = target_date.strftime('%Y-%m-%d')
        self.idx = self.df.index.get_loc(date_str)

        if not self.is_ordered(target_date, 3): return False
        #if not self.is_increse(target_date, 3): return False
        return True

    def is_ordered(self, target_date, days):
        """순차적인지 확인한다. """
        df = self.stock_data.get_df()
        for i in reversed(range(0, days)):
            data = self.df.ix[self.idx - i]
            #if not data.MA_5 < data.MA_20 < data.MA_60 < data.MA_120:
            if not data.MA_5 < data.MA_20 < data.MA_60:
                return False
        return True

    def is_increase(self, target_date, days):
        """종가가 계속해서 증가하고 있는지 판단"""
        adj_prev = -1
        df = self.stock_data.get_df()
        for i in reversed(range(days)):
            modify_date = target_date - timedelta(days=i)
            date_str = modify_date.strftime('%Y-%m-%d')
            data = df.loc[date_str]
            adj = data[AnalyzeMean.ADJ_CLOSE]
            if adj_prev < 0:
                adj_prev = adj
            elif adj_prev > adj:
                return False
        return True
