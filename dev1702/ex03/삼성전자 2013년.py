import requests
import pandas as pd
from io import StringIO
import matplotlib.pyplot as plt

url = 'http://real-chart.finance.yahoo.com/table.csv?s=005930.KS&a=0&b=1&c=2013&d=11&e=31&f=2013&g=d'
r=requests.get(url)
# lines = r.content.splitlines()
# print(lines[:10])
# df = pd.read_csv(StringIO(r.content.decode('utf-8')))
# print(df.head())

# df=pd.read_csv(StringIO(r.content.decode('utf-8')), index_col='Date', parse_dates={'Date'})
# df['Adj Close'].plot(figsize=(16, 4))

# pd.to_datetime(df['Date'])
# df = df.set_index('Date')
# print(df.head())

df=pd.read_csv(StringIO(r.content.decode('utf-8')), index_col='Date', parse_dates=['Date'])
print(df.head())

df['Adj Close'].plot(figsize=(16, 4))
df['Volume'].plot(figsize=(16,4), style='g')

plt.show()