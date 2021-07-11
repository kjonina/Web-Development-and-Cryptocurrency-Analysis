import pandas as pd
import numpy as np
import yfinance as yf
import datetime as dt

def create_y(request,x):

    global y

    start = "2009-01-01"
    end = dt.datetime.now()
    short_sma = 50
    long_sma = 200

    # creating a dataset for selected cryptocurrency
    y = yf.download(x, start, end,interval = '1d')
    y = pd.DataFrame(y.dropna(), columns = ['Open', 'High','Low','Close', 'Adj Close', 'Volume'])
    y = pd.DataFrame(y['Close'], columns = ['Close'])
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

    return y
