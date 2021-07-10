import pandas as pd
import numpy as np
import yfinance as yf
import datetime as dt

def create_df(request,x):
    global df
    global y

    start = "2009-01-01"
    end = dt.datetime.now()
    short_sma = 50
    long_sma = 200

    # creating a dataset for selected cryptocurrency
    df = yf.download(x, start, end,interval = '1d')
    df = pd.DataFrame(df.dropna(), columns = ['Open', 'High','Low','Close', 'Adj Close', 'Volume'])
    df['short_SMA'] = df.iloc[:,1].rolling(window = short_sma).mean()
    df['long_SMA'] = df.iloc[:,1].rolling(window = long_sma).mean()

    y = pd.DataFrame(df['Close'], columns = ['Close'])
    y.sort_index(inplace = True)

    # examining the pct_change
    y['Close Percentage Change'] = y['Close'].pct_change(1)

    # Creating a new variable, examining the difference for each observation
    y['diff'] = y['Close'].diff()

    # logging the target varialbe due to great variance
    y['log_Close'] = np.log(y['Close'])

    # Creating a new variable, examining the difference for each observation
    y['log_Close_diff'] = y['log_Close'].diff()

    y['Logged Close Percentage Change'] = y['log_Close'].pct_change(1)

    # logging the target varialbe due to great variance
    y['sqrt_Close'] = np.sqrt(y['Close'])

    y['Square Root Close Percentage Change'] = y['sqrt_Close'].pct_change(1)

    # Creating a new variable, examining the difference for each observation
    y['sqrt_Close_diff'] = y['sqrt_Close'].diff()

    # dropping the first na (because there is no difference)
    y = y.dropna()

#    # CHECKING Y
#    print(y.head())

#    # CHECKING DF
#    print(df.head())
    return df
