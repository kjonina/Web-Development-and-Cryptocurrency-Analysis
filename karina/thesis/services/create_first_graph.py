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

# will this import the dataset from the file?
#from thesis.views import df

def create_graphs(request, crypto_name):
    fig = make_subplots(rows=2, cols=1, shared_xaxes=True,  subplot_titles=[
            'Price and Moving Averages of {}'.format(str(crypto_name)),
            'Volume of {}'.format(str(crypto_name))])
    # Lineplots of price and moving averages
    fig.add_trace(go.Scatter(
                            x = df.index,
                            y = df['Close'],
                            name = crypto_name,
                            mode='lines',
                            customdata = df['Name'],
                            # corrects hovertemplate labels!
                            hovertemplate="<b>%{customdata}</b><br><br>" +
                                            "Date: %{x|%d %b %Y} <br>" +
                                            "Closing Price: %{y:$,.2f}<br>" +
                                            "<extra></extra>",
                            line = dict(color="black")), row = 1, col = 1)
    fig.add_trace(go.Scatter(x = df.index,
                             y = df['short_SMA'],
                             name = 'Short SMA',
                             mode = 'lines', customdata = df['Name'],
                             hovertemplate="<b>%{customdata}</b><br><br>" +
                                            "Date: %{x|%d %b %Y} <br>" +
                                            "Short Moving Average Price: %{y:$,.2f}<br>" +
                                            "<extra></extra>",
                             line = dict(color="red")), row = 1, col = 1)
    fig.add_trace(go.Scatter(x = df.index,
                             y = df['long_SMA'],
                             name = 'Long SMA',
                             mode = 'lines',customdata = df['Name'],
                             hovertemplate="<b>%{customdata}</b><br><br>" +
                                            "Date: %{x|%d %b %Y} <br>" +
                                            "Long Moving Average Price: %{y:$,.2f}<br>"+
                                            "<extra></extra>",
                             line = dict(color="green")), row = 1, col = 1)
    # Barplot of volume
    fig.add_trace(go.Bar(x = df.index,
                    y = df['Volume'],
                    name = 'Volume',
                    # corrects hovertemplate labels!
                    customdata = df['Name'],
                    hovertemplate="<b>%{customdata}</b><br><br>" +
                                    "Date: %{x|%d %b %Y} <br>" +
                                    "Volume: %{y:,.}<br>" +
                                    "<extra></extra>",
                    marker = dict(color="black", opacity = True)), row = 2, col = 1)
    # Add titles
    fig.update_layout(
            title = 'Price of {}'.format(str(crypto_name)))
    fig['layout']['yaxis1']['title']='US Dollars'
    fig['layout']['yaxis2']['title']='Volume'
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
    fig.update_yaxes(tickprefix = '$', tickformat = ',.', row = 1, col = 1)
    #time buttons
    fig.update_xaxes(rangeselector= {'visible' :False}, row = 2, col = 1)
