import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from pandas.compat import lmap

import exercise.ex01.stock_data as sd


def get_autocrrelation_dataframe(series):
    def r(h):
        return ((data[:n-h] - mean) * (data[h:] - mean)).sum() / float(n) / c0

    n = len(series)
    data = np.asarray(series)
    mean = np.mean(data)
    c0 = np.sum((data-mean) ** 2) / float(n)
    x = np.arange(n) + 1
    y = lmap(r, x)
    df = pd.DataFrame(y, index=x)
    return df

df_samsung = sd.load_stock_data('samsung.data')
df_samsung_corr = get_autocrrelation_dataframe(df_samsung['Close'])

fig, axs = plt.subplots(2, 1)
axs[1].xaxis.set_visible(False)

df_samsung['Close'].plot(ax=axs[0])
df_samsung_corr[0].plot(kind='bar', ax=axs[1])

plt.show()


