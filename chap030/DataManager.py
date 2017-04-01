import re
import sys
import pandas as pd
from datetime import datetime, timedelta
from pandas_datareader import data, wb
from multiprocessing import Pool
from chap030.ThreadWorker import *

class DataManager:
    # 시작일, 종료일,
    def __init__(self, start_date, end_date):
        self.item_list = {}     # 아이템 목록
        self.data_source = 'yahoo'
        self.start_date = start_date - timedelta(days=200)
        self.end_date = end_date
        self.item_datas = {}    # 아이템 결과 데이터
        self.stock_datas = {}

    def set_item_list(self, item_list):
        """가져올 대상 아이템(주식코드)들을 지정한다."""
        # itemList
        # item['code'], item['name']
        main = Tasks(item_list)
        self.stock_datas = main.start()

    def print_datas(self):
        for key, value in self.stock_datas.items():
            print(key, value)

    def get_stock_datas(self):
        return self.stock_datas