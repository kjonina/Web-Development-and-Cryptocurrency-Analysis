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
                dict(count = 7, label = "1W", step = "day", stepmode = "backward"),
                dict(count = 28, label = "1M", step = "day", stepmode = "backward"),
                dict(count = 6, label = "6M", step = "month", stepmode = "backward"),
                dict(count = 1, label = "YTD", step = "year", stepmode = "todate"),
                dict(count = 1, label = "1Y", step = "year", stepmode = "backward"),
                dict(count = 3, label = "3Y", step = "year", stepmode = "backward"),
                dict(count = 5, label = "5Y", step = "year", stepmode = "backward"),
                dict(step = "all")])))
    fig.update_layout(xaxis_rangeslider_visible = False)
    fig.update_yaxes(tickprefix = '$', tickformat = ',.')

    candle_stick = fig.to_html(full_html=False, default_height=1000, default_width=1500)

    return candle_stick

"""
TO FIX
- fix hovertemplate for Candlestick
- create a slider for short and long SMA
"""
