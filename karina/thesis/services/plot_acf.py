
# Downloading necessary Packages
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import mpld3
from statsmodels.graphics.tsaplots import plot_acf
from statsmodels.graphics.tsaplots import plot_pacf
from statsmodels.tsa.stattools import pacf, adfuller, kpss

# fixing bugs with
# To register the converters:
# >>> from pandas.plotting
# import register_matplotlib_converters >>> register_matplotlib_converters()

import pandas.plotting # import register_matplotlib_conververs
pandas.plotting.register_matplotlib_converters()

import base64
from io import BytesIO

def get_graph(request):
    buffer = BytesIO()
    plt.savefig(buffer, format = 'png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    graph =  base64.b64encode(image_png)
    graph = graph.decode('utf-8')
    buffer.close()
    return graph


def acf_and_pacf_plots(request, data, crypto_name):
    plt.switch_backend('AGG')


    sns.set_style('darkgrid')
#    fig, (ax1, ax2,ax3) = plt.subplots(3,1, figsize = (8,15)) # graphs in a column
    fig, (ax1, ax2,ax3) = plt.subplots(1,3, figsize = (20,5)) # graphs in a row
    fig.suptitle('ACF and PACF plots of Logged Closing Price Difference for {}'.format(crypto_name), fontsize=16)
    ax1.plot(data)
    ax1.set_title('Original')
    plot_acf(data, lags=40, ax=ax2);
    plot_pacf(data, lags=40, ax=ax3);
    acf_and_pacf_plots = get_graph(request)

    return acf_and_pacf_plots
