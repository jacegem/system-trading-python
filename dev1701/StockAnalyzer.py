

class StockAnalyzer:
    """df 의 값을 보고 결정한 한다"""


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
            if df


    def for_buy_all(self, df, days):
        for i in range(0, days):
            print(i)

        return 0


