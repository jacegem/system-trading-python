class StockData():
    def __init__(self, item ,df):
        self.item = item
        self.df = df
        pass

    def get_code(self):
        return self.item['code']

    def get_df(self):
        return self.df