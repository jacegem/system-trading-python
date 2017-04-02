

class AnalyzeBasic():
    ADJ_CLOSE = 'Adj Close'

    def __init__(self, stock_data):
        """이평선을 기준으로 구매 대상을 분석합니다"""
        self.stock_data = stock_data
        self.df = self.stock_data.get_df()
        self.idx = 0

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

        # 전날 보다 올랐으면 산다
        adj_close_today = self.df.ix[self.idx][AnalyzeBasic.ADJ_CLOSE]
        adj_close_last = self.df.ix[self.idx - 1][AnalyzeBasic.ADJ_CLOSE]

        if adj_close_today > adj_close_last:
            return True
        else:
            return False

    def should_i_sell(self, target_date):
        """팔아야 하는가"""
        # 대상 날짜의 인덱스를 얻는다.
        date_str = target_date.strftime('%Y-%m-%d')
        self.idx = self.df.index.get_loc(date_str)

        # 전날 보다 떨어졌으면 판다.
        adj_close_today = self.df.ix[self.idx][AnalyzeBasic.ADJ_CLOSE]
        adj_close_last = self.df.ix[self.idx - 1][AnalyzeBasic.ADJ_CLOSE]

        if adj_close_today < adj_close_last:
            return True
        else:
            return False
