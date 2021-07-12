# Downloading necessary files
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

def rolling_m_sd(request, y, crypto_name):
    #Determing rolling statistics
    rolmean = y['Close'].rolling(window = 12).mean()
    rolstd = y['Close'].rolling(window = 12).std()

    #Plot rolling statistics:
    fig = go.Figure()
    fig.add_trace(go.Scatter(x = y.index,
                                y = y['Close'],
                                name = 'Original',
                                mode='lines',
                            #    customdata = df['Name'],
                            #    hovertemplate="<b>%{customdata}</b><br><br>" +
                            #        "Date: %{x|%d %b %Y} <br>" +
                            #        "Closing Price: %{y:$,.2f}<br>" +
                            #        "<extra></extra>",
                                line = dict(color="blue")))
    fig.add_trace(go.Scatter(x = y.index,
                                y = rolmean,
                                name = 'Rolling Mean',
                                mode='lines',
                            #    customdata = df['Name'],
                            #    hovertemplate="<b>%{customdata}</b><br><br>" +
                            #        "Date: %{x|%d %b %Y} <br>" +
                            #        "Rolling Mean Price: %{y:$,.2f}<br>" +
                            #        "<extra></extra>",
                                line = dict(color="red")))
    fig.add_trace(go.Scatter(x = y.index,
                                y = rolstd,
                                name = 'Rolling Std',
                                mode='lines',
                            #    customdata = df['Name'],
                            #    hovertemplate="<b>%{customdata}</b><br><br>" +
                            #        "Date: %{x|%d %b %Y} <br>" +
                            #        "Rolling Std: %{y:$,.2f}<br>" +
                            #        "<extra></extra>",
                                line = dict(color="black")))
    # Add titles
    fig.update_layout(
            title = 'Rolling Mean & Standard Deviation of {}'.format(crypto_name),
            yaxis_title = 'US Dollars',
            yaxis_tickprefix = '$', yaxis_tickformat = ',.')

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

    rolling_m_sd = fig.to_html(full_html=False, default_height=1000, default_width=1500)

    return rolling_m_sd
