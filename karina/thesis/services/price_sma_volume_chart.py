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


def price_sma_volume_chart(request, df, crypto_name):
    fig = make_subplots(rows=2, cols=1, shared_xaxes=True, subplot_titles=[
            'Price and Death Cross of {}'.format(str(crypto_name)),
            'Volume of {}'.format(str(crypto_name))])

    # Lineplots of price and moving averages
    fig.add_trace(go.Scatter(
                            x = df.index,
                            y = df['Close'],
                            name = crypto_name,
                            mode='lines',
                            customdata = df['Name'],
                            hovertemplate="<b>%{customdata}</b><br><br>" +
                                            "Date: %{x|%d %b %Y} <br>" +
                                            "Closing Price: %{y:$,.2f}<br>" ,
                            line = dict(color="black")), row = 1, col = 1)

    fig.add_trace(go.Scatter(x = df.index,
                             y = df['short_SMA'],
                             name = 'Short SMA 50-Day',
                             mode = 'lines',
                             customdata = df['Name'],
                             hovertemplate="<b>%{customdata}</b><br><br>" +
                                            "Date: %{x|%d %b %Y} <br>" +
                                            "Short (50-Day) Moving Average Price: %{y:$,.2f}<br>",
                             line = dict(color="red")), row = 1, col = 1)

    fig.add_trace(go.Scatter(x = df.index,
                             y = df['long_SMA'],
                             name = 'Long SMA 200-Day',
                             mode = 'lines',
                             customdata = df['Name'],
                             hovertemplate="<b>%{customdata}</b><br><br>" +
                                            "Date: %{x|%d %b %Y} <br>" +
                                            "Long (200-Day) Moving Average Price: %{y:$,.2f}<br>",
                             line = dict(color="green")), row = 1, col = 1)
    # Barplot of volume
    fig.add_trace(go.Bar(x = df.index,
                    y = df['Volume'],
                    name = 'Volume',
                    customdata = df['Name'],
                    hovertemplate="<b>%{customdata}</b><br><br>" +
                                    "Date: %{x|%d %b %Y} <br>" +
                                    "Volume: %{y:,.}<br>" +
                                    "<extra></extra>",
                    marker = dict(color="black", opacity = True)), row = 2, col = 1)
    # Add titles
    fig.update_layout(
            title = 'Summary of {}'.format(str(crypto_name)))
    fig['layout']['yaxis1']['title']='US Dollars'
    fig['layout']['yaxis2']['title']='Volume'
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
    fig.update_yaxes(tickprefix = '$', tickformat = ',.', row = 1, col = 1)
    #time buttons
    fig.update_xaxes(rangeselector= {'visible' :False}, row = 2, col = 1)

    # fig.update_layout(showlegend=False)

    price_sma_volume_chart = fig.to_html(full_html=False, default_height=1000, default_width=1500)

    return price_sma_volume_chart
