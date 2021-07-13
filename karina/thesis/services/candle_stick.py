import numpy as np
import pandas as pd
import yfinance as yf
from matplotlib import pyplot
import matplotlib.pyplot as plt
from datetime import datetime
import datetime as dt
import plotly.graph_objects as go
import plotly.graph_objs as go
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.io as pio
import plotly.offline as py
from plotly.offline import download_plotlyjs, plot

def candle_stick(request, df, crypto_name):
    fig = go.Figure()

#    hovertext=[]
#    for i in range(len(df.Open)):
#        hovertext.append('Date: '+str(df.index[i])+
#                        '<br>Open: '+str(df.Open[i])+
#                        '<br>High: '+str(df.High[i])+
#                        '<br>Low: '+str(df.Open[i])+
#                         '<br>Close: '+str(df.Close[i]))


    # Candlestick
    fig.add_trace(go.Candlestick(x = df.index,
                    open = df['Open'],
                    high = df['High'],
                    low = df['Low'],
                    close = df['Close'],
#                    text=hovertext,
#                    hoverinfo='text',
                    name = 'market data'))

    # Add titles
    fig.update_layout(
            title = 'Price of {}'.format(str(crypto_name)))
    fig['layout']['yaxis']['title']='US Dollars'

    # X-Axes
    fig.update_xaxes(
        rangeslider_visible = True,
        rangeselector = dict(
            buttons = list([
                            dict(count = 7, step = "day", stepmode = "backward", label = "1W"),
                            dict(count = 1, step = "month", stepmode = "backward", label = "1M"),
                            dict(count = 3, step = "month", stepmode = "backward", label = "3M"),
                            dict(count = 6, step = "month", stepmode = "backward", label = "6M"),
                            dict(count = 1, step = "year", stepmode = "backward", label = "1Y"),
                            dict(count = 2, step = "year", stepmode = "backward", label = "2Y"),
                            dict(count = 5, step = "year", stepmode = "backward", label = "5Y"),
                            dict(count = 1, step = "all", stepmode = "backward", label = "MAX"),
                            dict(count = 1, step = "year", stepmode = "todate", label = "YTD")])))
    fig.update_layout(xaxis_rangeslider_visible = False)
    fig.update_yaxes(tickprefix = '$', tickformat = ',.')

    candle_stick = fig.to_html(full_html=False, default_height=1000, default_width=1500)

    return candle_stick

"""
TO FIX
- fix hovertemplate for Candlestick
- create a slider for short and long SMA
"""
