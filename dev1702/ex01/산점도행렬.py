import matplotlib.pyplot as plt
from pandas.tools.plotting import scatter_matrix

import exercise.ex01.stock_data as sd

file = 'samsung.data'
df = sd.load_stock_data(file)

scatter_matrix(df[['Open', 'High', 'Low', 'Close']], alpha=0.2, figsize=(6, 6), diagonal='kde')
plt.show()

