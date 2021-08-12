import pandas as pd
import numpy as np
import datetime as dt


def create_train_and_test(request,y, crypto_name):

    # Train data - 80%
    df_train = y[:int(0.90*(len(y)))]
    # print('============================================================')
    # print('{} Training Set'.format(crypto_name))
    # print('============================================================')
    # print(df_train.head())
    # print('Training set has {} rows and {} columns.'.format(*df_train.shape))

    # Test data - 20%
    df_test = y[int(0.90*(len(y))):]
    # print('============================================================')
    # print('{} Test Set'.format(crypto_name))
    # print('============================================================')
    # print(df_test.head())
    # print('Test set has {} rows and {} columns.'.format(*df_test.shape))
    return df_train, df_test
