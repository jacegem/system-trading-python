import pandas as pd
#import pandas.io.data as web
import pandas_datareader.data as web
import datetime
import matplotlib.pyplot as plt

def download_stock_data(file_name, company_code, year1, month1, date1, year2, month2, date2):
    start = datetime.datetime(year1, month1, date1)
    end = datetime.datetime(year2, month2, date2)
    df = web.DataReader("%s.KS" % (company_code), "yahoo", start, end)

    df.to_pickle(file_name)

    return df

def load_stock_data(file_name):
    df = pd.read_pickle(file_name)
    return df

if __name__ == "__main__":
    file = 'samsung.data'
    download_stock_data(file, '005930', 2015, 1, 1, 2015, 11, 30)
    df = load_stock_data(file)
    print(df.describe())

    df = load_stock_data(file)
    (n, bins, patched) = plt.hist(df['Open'])
    plt.axvline(df['Open'].mean(), color='red')
    plt.show()
    for index in range(len(n)):
        print("Bin: %0.f, Frequency= %0.f" % (bins[index], n[index]))

