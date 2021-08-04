
# Downloading necessary Packages
import numpy as np
import pandas as pd
import yfinance as yf
import plotly.graph_objs as go
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.io as pio
import matplotlib.pyplot as plt
from matplotlib import pyplot
from datetime import datetime
import plotly.graph_objects as go
import statsmodels.api as sm



def decomposition(request, df, data, crypto_name):

    decomposition = sm.tsa.seasonal_decompose(data)

    #seasonality
    decomp_seasonal = decomposition.seasonal

    #trend
    decomp_trend = decomposition.trend

    #residual
    decomp_resid = decomposition.resid


    fig = make_subplots(rows=4, cols=1, shared_xaxes=True, subplot_titles=[
            'Price  of {}'.format(str(crypto_name)),
            'Trend values of {}'.format(str(crypto_name)),
            'Seasonal values of {}'.format(str(crypto_name)),
            'Residual values of {}'.format(str(crypto_name))])


    fig.add_trace(go.Scatter(x = df.index,
                            y = data,
                            name = crypto_name,
                            mode='lines'),row = 1, col = 1)


    fig.add_trace(go.Scatter(x = df.index,
                            y = decomp_trend,
                            name = 'Trend',
                            mode='lines'),row = 2, col = 1)


    fig.add_trace(go.Scatter(x = df.index,
                            y = decomp_seasonal,
                            name = 'Seasonality',
                            mode='lines'),row = 3, col = 1)

    fig.add_trace(go.Scatter(x = df.index,
                            y = decomp_resid,
                            name = 'Residual',
                            mode='lines'),row = 4, col = 1)

    # Add titles
    fig.update_layout(
            title = 'Decomposition of {}'.format(str(crypto_name)))
    fig['layout']['yaxis1']['title']='US Dollars'
    fig['layout']['yaxis2']['title']='Trend'
    fig['layout']['yaxis3']['title']='Seasonality'
    fig['layout']['yaxis4']['title']='Residual'

    decomposition = fig.to_html(full_html=False, default_height=1000, default_width=1500)

    return decomposition
