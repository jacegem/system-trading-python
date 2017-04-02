import matplotlib.pyplot as plt
from pandas.tools.plotting import autocorrelation_plot

import exercise.ex01.stock_data as sd

fig, axs = plt.subplots(2, 1)
file = 'samsung.data'
df_samsung = sd.load_stock_data(file)
df_samsung['Close'].plot(ax=axs[0])
autocorrelation_plot(df_samsung['Close'], ax=axs[1])
plt.show()



