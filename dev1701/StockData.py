from datetime import datetime, timedelta
from pandas_datareader import data, wb
import re
import pandas as pd
from multiprocessing import Pool

class StockData:

    def __init__(self, src):
        self.src = src
        self.today = datetime.today();
        self.startday = self.today - timedelta(days=200)
        self.dfDatas = {}

    def get_symbol(self, code):
        if re.match(r'A(\d+)', code) == None: return None

        symbol = re.sub(r'A(\d+)', r'\1.KS', code)
        print("Symbol is {0}".format(symbol))
        return symbol

    # dataframe
    def get_data_one(self, code):
        # '005930.KS' 와 같은 형태로 변형해야 함.
        symbol = self.get_symbol(code)

        try:
            df = data.DataReader(symbol, self.src, self.startday)
        except:
            return None

        df = df[df['Volume'] != 0]
        dfAdjClose = df['Adj Close']
        dfVolume = df['Volume']

        # df['MA_5'] = pd.stats.moments.rolling_mean(df[adjClose], 5)
        # df['MA_60'] = pd.stats.moments.rolling_mean(df[adjClose], 60)
        # df['MA_120'] = pd.stats.moments.rolling_mean(df[adjClose], 120)
        # df['MV_5'] = pd.stats.moments.rolling_mean(df[volume], 5)
        # df['MV_20'] = pd.stats.moments.rolling_mean(df[volume], 20)
        # df['MV_60'] = pd.stats.moments.rolling_mean(df[volume], 60)
        # df['MV_120'] = pd.stats.moments.rolling_mean(df[volume], 120)

        df['MA_5'] = pd.Series(dfAdjClose).rolling(window=5).mean()
        df['MA_20'] = pd.Series(dfAdjClose).rolling(window=20).mean()
        df['MA_60'] = pd.Series(dfAdjClose).rolling(window=60).mean()
        df['MA_120'] = pd.Series(dfAdjClose).rolling(window=120).mean()

        df['MV_5'] = pd.Series(dfVolume).rolling(window=5).mean()
        df['MV_20'] = pd.Series(dfVolume).rolling(window=20).mean()
        df['MV_60'] = pd.Series(dfVolume).rolling(window=60).mean()
        df['MV_120'] = pd.Series(dfVolume).rolling(window=120).mean()

        df['RA_5'] = df['MA_5'] / df['MA_20']
        df['RA_20'] = df['MA_20'] / df['MA_60']
        df['RA_60'] = df['MA_60'] / df['MA_120']

        return df

    def get_data(self, line):
        datas = line.split(',')
        code = datas[0]
        name = datas[1]
        print (code, name)
        df = self.get_data_one(code)
        if df is not None:
            self.dfDatas[code] = df

    def get_data_multi(self):
        f = open('..\\data\\kospi.csv', 'rt')
        lines = f.readlines()
        pool = Pool(processes=8)  # start 4 worker processes
        pool.map(self.get_data, lines)

if __name__ == "__main__":
    stockdata = StockData('yahoo')
    stockdata.get_data_multi()
    #A003230,     삼양식품

