import pandas as pd
import numpy as np
import yfinance as yf
import datetime as dt


from thesis.services.create_df import create_df

def create_y(request, crypto_name, crypto_ticket):

    df = create_df(request,crypto_ticket, crypto_name)

    # creating a dataset for selected cryptocurrency
    y = df.copy()
    y = pd.DataFrame(y['Close'], columns = ['Close'])
    y['Name'] = crypto_name
    y.sort_index(inplace = True)

    # examining the pct_change
    y['Close Percentage Change'] = y['Close'].pct_change(1)

    # Creating a new variable, examining the difference for each observation
    y['Close_diff'] = y['Close'].diff()

    # logging the target varialbe due to great variance
    y['log_Close'] = np.log(y['Close'])

    # Creating a new variable, examining the difference for each observation
    y['log_Close_diff'] = y['log_Close'].diff()

    y['Logged Close Percentage Change'] = y['log_Close'].pct_change(1)

    # dropping the first na (because there is no difference)
    y = y.dropna()

    # checking y
    # print(y.head())

    return y
