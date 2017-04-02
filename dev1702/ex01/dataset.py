import datetime

import pandas as pd
import numpy as np


def make_dataset(df, time_lags=5):
    df_lag = pd.DataFrame(index=df.index)
    df_lag["Close"] = df["Close"]
    df_lag['Volume'] = df['Volume']

    df_lag['Close_Lag%s' % str(time_lags)] = df['Close'].shift(time_lags)
    df_lag['Close_Lag%s_Change' % str(time_lags)] = df_lag['Close_Lag%s' % str(time_lags)].pct_change()*100.0

    df_lag['Volume_Lag%s' % str(time_lags)] = df['Volume'].shift(time_lags)
    df_lag['Volume_Lag%s_Change' % str(time_lags)] = df_lag['Volume_Lag%s' % str(time_lags)].pct_change()*100.0

    df_lag['Close_Direction'] = np.sign(df_lag['Close_Lag%s_Change' % str(time_lags)])
    df_lag['Volume_Direction'] = np.sign(df_lag['Volume_Lag%s_Change' % str(time_lags)])

    return df_lag.dropna(how='any')


'''
df_lag["Close] 는 종가
df_lag["Volume"]은 거래량
df_lag["Close_Lag%s"]와 df_lag["Volume_Lag%"]는 사용자가 지정한 일자만큼의 종가 거래량을 나타내는 입력변수다
'''

'''
### 4.7.2 데이터셋 나누기
make_dataset() 함수를 이용해 주가방향 예측변수에 사용할 데이터셋을 만들었으면 이를 학습에 사용할 데이터셋과 테스트에 사용할 데이터셋으로 나누어야 한다 split_dataset()함수는 주어진 데이터셋을 사용자가 지정한 입력변수와 출력변수로 일정 비율로 나누어 준다.
'''

def split_dataset(df, input_column_array, output_column, split_ratio):
    split_date = get_date_by_percent(df.index[0], df.index[df.shape[0]-1], split_ratio)

    input_data = df[input_column_array]
    output_data = df[output_column]

    X_train = input_data[input_data.index < split_date]
    X_test = input_data[input_data.index >= split_date]
    Y_train = output_data[output_data.index < split_date]
    Y_test = output_data[output_data.index >= split_date]

    return X_train, X_test, Y_train, Y_test

def get_date_by_percent(start_date, end_date, percent):
    days = (end_date - start_date).days
    target_days = np.trunc(days * percent)
    target_date = start_date + datetime.timedelta(days=target_days)
    return target_date



def do_logistic_regression(x_train, y_train):
    classifier = LogistricRegression()
    classifier.fit(x_train, y_train)
    return classifier

def do_random_forest(x_train, y_train):
    classifier = RandomForestClassifier()
    classifier.fit(x_train, y_train)
    return classifier

def do_svm(x_train, y_train):
    classifier = SVC()
    classifier.fit(x_train, y_train)
    return classifier




