import pandas as pd
import numpy as np
import yfinance as yf
import datetime as dt

def create_df(request,x, crypto_name):

    start = "2009-01-01"
    end = dt.datetime.now()
    short_sma = 50
    long_sma = 200

    # creating a dataset for selected cryptocurrency
    df = yf.download(x, start, end,interval = '1d')
    df = pd.DataFrame(df.dropna(), columns = ['Open', 'High','Low','Close', 'Adj Close', 'Volume'])
    # Create short SMA
    df['short_SMA'] = df.iloc[:,1].rolling(window = short_sma).mean()

    # Create Long SMA
    df['long_SMA'] = df.iloc[:,1].rolling(window = long_sma).mean()

    # Create daily_return
    df['daily_return'] = df['Close'].pct_change(periods=1)

    # Create monthly_return
    df['monthly_return'] = df['Close'].pct_change(periods=30)

    # Create annual_return
    df['annual_return'] = df['Close'].pct_change(periods=365)
    df['Name'] = crypto_name

    # preparing data from time series analysis
    # eliminating any NAs
    df.index = pd.to_datetime(df.index)
    df = df.asfreq('D')
    # print('Nan in each columns' , df.isna().sum())
    df = df.bfill()
    # print('Nan in each columns' , df.isna().sum())


    return df
