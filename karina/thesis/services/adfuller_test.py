
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




def adfuller_test(request, data):
    dftest = adfuller(data)
    dfoutput = pd.Series(dftest[0:4], index=['Test Statistic','p-value','#Lags Used','Number of Observations Used'])
    for key,value in dftest[4].items():
        dfoutput['Critical Value (%s)'%key] = value

    dfoutput = pd.DataFrame(dfoutput)
    dfoutput = dfoutput.reset_index()
    dfoutput1 = pd.DataFrame([['stationary', np.where(dftest[1]>0.05, 'Conclude not stationary', 'Conclude  stationary')]], columns=['index', 0])

    dfoutput = pd.concat([dfoutput,dfoutput1])

    dfoutput.to_json(orient='records')
    return dfoutput
