import re
import sys
import pandas as pd
from datetime import datetime, timedelta
from pandas_datareader import data, wb
from multiprocessing import Pool
from qt.ThreadWorker import *

class DataManager:
    def __init__(self):
        self.item_list = {}     # 아이템 목록
        self.data_source = 'yahoo'
        self.today = datetime.today()
        self.start_day = self.today - timedelta(days=200)
        self.item_datas = {}    # 아이템 결과 데이터
        self.stock_datas = {}
        pass

    def set_item_list(self, item_list):
        # itemList
        # item['code'], item['name']
        main = Tasks(item_list)
        self.stock_datas = main.start()

    def print_datas(self):
        for key, value in self.stock_datas.items():
            print(key, value)

    def get_stock_datas(self):
        return self.stock_datas