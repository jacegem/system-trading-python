# https://wikidocs.net/1918

import pandas as pd
import datetime
import pandas.io.data as web

start = datetime.datetime(2014,1,1)
end = datetime.datetime(2015,2,15)

soil = web.DataReader("010950.KS", "yahoo", start, end)

print(soil.tail())

soil['MA5'] = pd.stats.moments.rolling_mean(soil['Adj Close'], 5)
soil['MA20'] = pd.stats.moments.rolling_mean(soil['Adj Close'], 20)
soil['MA60'] = pd.stats.moments.rolling_mean(soil['Adj Close'], 60)
soil['MA120'] = pd.stats.moments.rolling_mean(soil['Adj Close'], 120)

print(soil.tail())






