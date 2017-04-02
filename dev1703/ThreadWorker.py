# http://stackoverflow.com/questions/13909195/how-run-two-different-threads-simultaneously-in-pyqt
# https://nikolak.com/pyqt-threading-tutorial/
# http://stackoverflow.com/questions/30843876/using-qthreadpool-with-qrunnable-in-pyqt4

import re
import sys
import pandas as pd
from datetime import datetime, timedelta
from pandas_datareader import data, wb
from multiprocessing import Pool
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from qt.StockData import StockData


class WorkerSignals(QObject):
    result = pyqtSignal(dict)


class Worker(QRunnable):
    def __init__(self, item, parent):
        super(Worker, self).__init__()
        self.item = item
        self.signals = WorkerSignals()
        self.data_source = 'yahoo'
        self.today = datetime.today()
        self.start_day = self.today - timedelta(days=200)
        self.parent = parent

    def run(self):
        print('Sending', self.item)
        df = self.get_data_one(self.item)
        result = {'code':self.item, 'data':df}
        self.signals.result.emit(result)
        self.parent.process_result(result)

    def get_data_one(self, code_data):
        # '005930.KS' 와 같은 형태로 변형해야 함.
        code = code_data['code']
        name = code_data['name']

        pattern = r'A(\d+)'
        if re.match(pattern, code):
            symbol = re.sub(pattern, r'\1.KS', code)
        else:
            return None

        try:
            df = data.DataReader(symbol, self.data_source, self.start_day)
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

        return df

class Tasks(QObject):
    def __init__(self, item_list):
        super(Tasks, self).__init__()

        self.pool = QThreadPool.globalInstance()
        self.pool.setMaxThreadCount(4)
        self.item_list = item_list
        self.stock_datas = {}

    def process_result(self, result_dict):
        print('Receiving', result_dict)
        stock_data = StockData(result_dict['code'], result_dict['data'])
        self.stock_datas[stock_data.get_code()] = stock_data

    def start(self):
        for item in self.item_list:
            worker = Worker(item, self)
            worker.signals.result.connect(self.process_result)

            self.pool.start(worker)

        rst = self.pool.waitForDone()
        print("done", rst)
        return self.stock_datas



if __name__ == "__main__":
    item_list = []
    item_list.append({'name': '동양우', 'code': 'A001525'})
    item_list.append({'code': 'A001525', 'name': '동양우'})
    item_list.append({'code': 'A023350', 'name': '한국종합기술'})
    item_list.append({'code': 'A018670', 'name': 'SK가스'})
    item_list.append({'code': 'A037710', 'name': '광주신세계'})
    item_list.append({'code': 'A009410', 'name': '태영건설'})
    item_list.append({'code': 'A003620', 'name': '쌍용차'})
    item_list.append({'code': 'A000040', 'name': 'KR모터스'})
    item_list.append({'code': 'A004440', 'name': '대림씨엔에스'})
    item_list.append({'code': 'A003610', 'name': '방림'})
    item_list.append({'code': 'A005257', 'name': '녹십자홀딩스2우'})

    main = Tasks(item_list)
    main.start()