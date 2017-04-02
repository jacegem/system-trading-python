
import pandas as pd
from datetime import datetime
from pandas.io.data import DataReader
import matplotlib.pyplot as plt

start = datetime(2013, 1, 1)
end = datetime(2013, 12, 30)

df = DataReader('005930.KS', 'yahoo', start, end)
df['MA_5'] = pd.stats.moments.rolling_mean(df['Adj Close'], 5)
df['MA_20'] = pd.stats.moments.rolling_mean(df['Adj Close'], 20)
df['diff'] = df['MA_5'] - df['MA_20']
head = df.head(10)

print(df)


