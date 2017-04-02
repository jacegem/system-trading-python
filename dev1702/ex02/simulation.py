import numpy as np
t = np.random.randint(-1, 2, size=100)
walk = t.cumsum()
print(walk)

import matplotlib.pyplot as plt
plt.plot(walk)
#plt.show()

import pandas as pd
#from pandas.io.data import DataReader
from pandas_datareader import data, wb

aapl = data.DataReader('AAPL', 'yahoo', start='2014')
#print(aapl)
#returns = aapl['Adj Close'].pct_change()
#plt.plot_date(aapl['Date'], returns)
#plt.show()



