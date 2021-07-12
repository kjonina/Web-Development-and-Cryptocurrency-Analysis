import pandas as pd
import numpy as np
import yfinance as yf
import datetime as dt

def create_y(request,x, crypto_name):

    global y

    start = "2009-01-01"
    end = dt.datetime.now()
    short_sma = 50
    long_sma = 200

    # creating a dataset for selected cryptocurrency
    y = yf.download(x, start, end,interval = '1d')
    y = pd.DataFrame(y.dropna(), columns = ['Open', 'High','Low','Close', 'Adj Close', 'Volume'])
    y = pd.DataFrame(y['Close'], columns = ['Close'])
    y['Name'] = crypto_name
    y.sort_index(inplace = True)

    # examining the pct_change
    y['Close Percentage Change'] = y['Close'].pct_change(1)

    # Creating a new variable, examining the difference for each observation
    y['Close Difference'] = y['Close'].diff()

    # logging the target varialbe due to great variance
    y['Logged Close'] = np.log(y['Close'])

    # Creating a new variable, examining the difference for each observation
    y['Logged Close Diff'] = y['Logged Close'].diff()

    y['Logged Close Percentage Change'] = y['Logged Close'].pct_change(1)

    # logging the target varialbe due to great variance
    y['Square Root Close'] = np.sqrt(y['Close'])

    y['Square Root Close Percentage Change'] = y['Square Root Close'].pct_change(1)

    # Creating a new variable, examining the difference for each observation
    y['Square Root Close Difference'] = y['Square Root Close'].diff()

    # dropping the first na (because there is no difference)
    y = y.dropna()

#    # CHECKING Y
#    print(y.head())

    return y
