import math

import numpy as np
import pandas as pd
from datetime import datetime
from pandas.io.data import DataReader
import matplotlib.pyplot as plt

start = datetime(2013, 1, 1)
end = datetime(2013, 12, 30)
df = DataReader('005930.KS', 'yahoo', start, end)
#  거래량('Volume')이 0인 row 제거
df = df[df['Volume'] != 0]

df['Ret'] = np.log(df['Adj Close'] / df['Adj Close'].shift(1))
head = df.head()
print(head)


#df['Ret'].plot(figsize=(16, 4))
df['Ret'].hist(bins=50, color='r', alpha=0.5, figsize=(10,5))

plt.axhline(color='k')
plt.show()




