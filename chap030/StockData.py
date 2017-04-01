class StockData():
    """
    주식정보 데이터 주식의 날짜별 데이터 관리
    """
    def __init__(self, item, df):
        """
        :param item: code, name 으로 구성됨
        :param df: Pandas DataFrame
        """
        self.item = item
        self.df = df
        pass

    def get_code(self):
        return self.item['code']

    def get_df(self):
        return self.df