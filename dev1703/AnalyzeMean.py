"""
이평선을 기준으로 분석한 결과를 반환합니다.
분석 수치는 100% 를 기준으로 50% 이상이면 구매 대상입니다
"""

class AnalyzeMean():
    def __init__(self, stock_datas):
        #TODO: 이평선을 기준으로 구매 대상을 분석합니다
        self.datas = stock_datas

        result = []
        for stock_data in stock_datas:
            if self.is_good_buy(stock_data):
                result.append(stock_data)

    def is_good_buy(self, stock_data):
        """사도 되는 것인지 판단"""
        if not self.is_ordered(stock_data, 5): return False
        if not self.is_increse(stock_data, 5): return False


        return True


    def is_ordered(self, stock_data, days):
        """순차적인지 확인한다. """
        df = stock_data.get_df()
        for i in range(0, days):
            data = df.iloc[-i]
            if data.MA_5 > data.MA_20 \
                or data.MA_20 > data.MA_60 \
                or data.MA_60 > data.MA_120:
                return False
        return True

    def is_increase(self, stock_data, days):
        df = stock_data.get_df()
        for i in range(0, days):
            data = df.iloc[-i]
            #if df