from datetime import datetime, timedelta
from pandas_datareader import data, wb
import win32com.client
import re
import sys
import pandas as pd
from multiprocessing import Pool
from console.StockAnalyzer import StockAnalyzer
from console.StockData import StockData


class StockDataManager:

    def __init__(self):
        self.data_source = 'yahoo'
        self.dfDatas = {}

    def save_codes(self):
        code_mgr = win32com.client.Dispatch("CpUtil.CpCodeMgr")
        code_list = code_mgr.GetStockListByMarket(1)

        kospi = {}
        for code in code_list:
            name = code_mgr.CodeToName(code)
            kospi[code] = name

        f = open('..\\data\\kospi.csv', 'w')
        for key, value in kospi.items():
            if self.is_unable_read_code(key, value) is True:
                continue
            f.write("%s,%s\n" % (key, value))
        f.close()

    def load_codes(self, file='..\\data\\kospi.csv'):
        result = []

        f = open(file, 'rt')
        lines = f.readlines()
        for line in lines:
            datas = line.split(',')
            code = datas[0]
            name = datas[1]
            result.append({'code': code.strip(), 'name': name.strip()})
        f.close()

        return result

    def is_unable_read_code(self, code, name):
        pattern = r'^KOSPI|KODEX|SMART|ARIRANG|KBSTAR|TIGER|KINDEX|KOSEF|대신B\d{3}'
        if re.match(pattern, name):
            return True
        if re.match(r'\d+호$', name):
            return True
        if re.match(r'^Q', code):
            return True
        return None


    def get_symbol(self, code):
        if re.match(r'A(\d+)', code) is None:
            return None

        symbol = re.sub(r'A(\d+)', r'\1.KS', code)
        print("Symbol is {0}".format(symbol))
        return symbol


    def get_data_one(self, code_data):
        self.today = datetime.today()
        self.startday = self.today - timedelta(days=200)

        # '005930.KS' 와 같은 형태로 변형해야 함.

        code = code_data['code']
        name = code_data['name']

        pattern = r'A(\d+)'
        if re.match(pattern, code):
            symbol = re.sub(pattern, r'\1.KS', code)
        else:
            return None

        try:
            df = data.DataReader(symbol, self.data_source, self.startday)
        except:
            print("Unexpected error:", sys.exc_info()[0])
            return None

        df = df[df['Volume'] != 0]
        df_adj_close = df['Adj Close']
        df_volume = df['Volume']

        df['MA_5'] = pd.Series(df_adj_close).rolling(window=5).mean()
        df['MA_20'] = pd.Series(df_adj_close).rolling(window=20).mean()
        df['MA_60'] = pd.Series(df_adj_close).rolling(window=60).mean()
        df['MA_120'] = pd.Series(df_adj_close).rolling(window=120).mean()

        df['MV_5'] = pd.Series(df_volume).rolling(window=5).mean()
        df['MV_20'] = pd.Series(df_volume).rolling(window=20).mean()
        df['MV_60'] = pd.Series(df_volume).rolling(window=60).mean()
        df['MV_120'] = pd.Series(df_volume).rolling(window=120).mean()

        df['RA_5'] = df['MA_5'] / df['MA_20']
        df['RA_20'] = df['MA_20'] / df['MA_60']
        df['RA_60'] = df['MA_60'] / df['MA_120']

        stock_data = StockData(code, name)
        stock_data.set_df(df)
        return stock_data

    def get_data_multi(self, code_list, process=4, src='yahoo'):
        self.data_source = src
        pool = Pool(processes=process)  # start 4 worker processes
        datas = pool.map(self.get_data_multi_process, code_list)
        pool.close()
        pool.join()
        return datas

    def get_data_multi_process(self, data):
        print(data)
        df = self.get_data_one(data)
        if df is not None:
            code = data['code']
            self.dfDatas[code] = df
            return df




if __name__ == "__main__":
    sdm = StockDataManager()
    # 1. 저장
    # 2. 불러오기
    list = sdm.load_codes()
    # print(list)
    # 3. 모두 요청
    datas = sdm.get_data_multi(list, process=4, src='yahoo')
    # 4. 하나만 요청
    # code_map = {'name': '방림', 'code': 'A003610'}
    # df = sdm.get_data_one(code_map)
    # print(df)

    sa = StockAnalyzer()

    for stock_data in datas:
        rst = sa.is_ordered(stock_data, 5)
        print("is_ordered", rst)
        rst = sa.is_increase(stock_data, 5)





    # rst = sa.is_ordered(df, 5)



    # rst = sa.for_buy_all(df)
    # stock_analyzer.for_buy_one(df)
    #
    # stock_analyzer.for_sell_all(df)
    # stock_analyzer.for_sell_one(df)



    #stockdata.get_data_multi()
    #A003230,     삼양식품

