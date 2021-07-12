import pandas as pd
import numpy as np
import yfinance as yf
import datetime as dt

def create_df(request,x, crypto_name):
    global df

    start = "2009-01-01"
    end = dt.datetime.now()
    short_sma = 50
    long_sma = 200

    # creating a dataset for selected cryptocurrency
    df = yf.download(x, start, end,interval = '1d')
    df = pd.DataFrame(df.dropna(), columns = ['Open', 'High','Low','Close', 'Adj Close', 'Volume'])
    df['short_SMA'] = df.iloc[:,1].rolling(window = short_sma).mean()
    df['long_SMA'] = df.iloc[:,1].rolling(window = long_sma).mean()
    df['Name'] = crypto_name
    return df
