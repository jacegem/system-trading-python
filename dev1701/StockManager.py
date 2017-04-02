from datetime import datetime, timedelta
from pandas_datareader import data, wb
import datetime
import console.StockDataManager as StockData
import pandas as pd

class StockManager:
    def __init__(self, src):
        stock_data =  StockData.StockData(src)
        #self.dfData = stock_data.get_data_multi()

    def is_ordered(self, code, day):
        self.end_day = datetime.datetime.today()
        self.start_day = self.end_day -  timedelta(days=day)
        days = pd.date_range(self.start_day, self.end_day, freq='D')

        data = self.dfData[code]

        print(days)


    def get_rises(self, code):
        # 어떤 조건들이 있는가???
        if self.is_ordered(code, 10) == True\
            and self.is_cross(code, 10) == True:
            return 0


        return False

    def get_falls(self):
        return False





if __name__ == "__main__":
    stockManager = StockManager('yahoo')
    stockManager.is_ordered('A003230', 10)
