
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import mpld3
from statsmodels.graphics.tsaplots import plot_acf
from statsmodels.graphics.tsaplots import plot_pacf
from statsmodels.tsa.stattools import pacf, adfuller, kpss
from pandas.io.json import json_normalize
import json
import requests
import codecs



def adfuller_test(request, data, crypto_name):
    dftest = adfuller(data)
    dfoutput = pd.Series(dftest[0:4], index=['Test Statistic','p-value','#Lags Used','Number of Observations Used'])
    for key,value in dftest[4].items():
        dfoutput['Critical Value (%s)'%key] = value

    dfoutput = pd.DataFrame(dfoutput)
    dfoutput = dfoutput.reset_index()
    dfoutput = dfoutput.rename(columns={'index': crypto_name, '0': 0})
    dfoutput1 = pd.DataFrame([['Stationary', np.where(dftest[1]>0.05, 'Conclude not stationary', 'Conclude stationary')]], columns=[crypto_name, 0])

    dfoutput = pd.concat([dfoutput,dfoutput1], sort=False).reset_index(drop=True)

    print(type(dfoutput))

    print(dfoutput.index)
# does not work, why???
    return dfoutput.to_json(orient="records")
