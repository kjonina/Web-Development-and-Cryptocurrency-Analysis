
# Downloading necessary Packages
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from statsmodels.graphics.tsaplots import plot_acf
from statsmodels.graphics.tsaplots import plot_pacf
from statsmodels.tsa.stattools import pacf, adfuller, kpss



# # Dickey Fuller Test
# def adfuller_test(data):
#     dftest = adfuller(data)
#     dfoutput = pd.Series(dftest[0:4], index=['Test Statistic','p-value','#Lags Used','Number of Observations Used'])
#     for key,value in dftest[4].items():
#         dfoutput['Critical Value (%s)'%key] = value
#     print('============================================================')
#     print('Results of Dickey-Fuller Test for {}:'.format(crypto_name))
#     print('============================================================')
#     print (dfoutput)
#     if dftest[1]>0.05:
#         print('Conclude not stationary')
#     else:
#         print('Conclude stationary')


# def simple_plot_acf(request, data, no_lags):
#     fig, (ax1, ax2) = plt.subplots(1,2, figsize = (14,5))
#     ax1.plot(data)
#     ax1.set_title('Original')
#     plot_pacf(data, lags=no_lags, ax=ax2);
#
#     simple_plot_acf = fig.to_html(full_html=False, default_height=1000, default_width=1500)
#
#     return simple_plot_acf


# def simple_plot_pacf(data, no_lags):
#     fig, (ax1, ax2) = plt.subplots(1,2, figsize = (14,5))
#     ax1.plot(data)
#     ax1.set_title('Original')
#     plot_acf(data, lags=no_lags, ax=ax2);
#     plt.show()
