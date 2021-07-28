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
from pylab import rcParams


def candlestick_moving_average(request, df,crypto_name):

    fig = make_subplots(rows=2, cols=1, shared_xaxes=True, subplot_titles=[
            'Price and Moving Averages of {}'.format(str(crypto_name)),
            'Volume of {}'.format(str(crypto_name))])

    trace1 = go.Candlestick(
        x = df.index,
        open = df["Open"],
        high = df["High"],
        low = df["Low"],
        close = df["Close"],
        name = crypto_name)

    data = [trace1]

    for i in range(5, 201, 5):

        sma = go.Scatter(
            x = df.index,
            y = df["Close"].rolling(i).mean(), # Pandas SMA
            name = "SMA" + str(i),
            line = dict(color = "#3E86AB"),
            customdata = df['Name'],
            hovertemplate="<b>%{customdata}</b><br><br>" +
                        "Date: %{x|%d %b %Y} <br>" +
                        "Simple Moving Average Price: %{y:$,.2f}<br>",
            opacity = 0.7,
            visible = False,
        )

        data.append(sma)

    sliders = dict(

        # GENERAL
        steps = [],
        currentvalue = dict(
            font = dict(size = 16),
            prefix = "SMA: ",
            xanchor = "left",
        ),

        x = 0.15,
        y = 0,
        len = 0.85,
        pad = dict(t = 0, b = 0),
        yanchor = "bottom",
        xanchor = "left",
    )

    for i in range((200 // 5) + 1):

        step = dict(
            method = "restyle",
            label = str(i * 5),
            value = str(i * 5),
            args = ["visible", [False] * ((200 // 5) + 1)],
        )

        step['args'][1][0] = True
        step['args'][1][i] = True
        sliders["steps"].append(step)



    layout = dict(

        title = 'Price of {}'.format(str(crypto_name)),

        # ANIMATIONS
        sliders = [sliders],
        xaxis = dict(

            rangeselector = dict(
                activecolor = "#888888",
                bgcolor = "#DDDDDD",
                buttons = [
                            dict(count = 7, step = "day", stepmode = "backward", label = "1W"),
                            dict(count = 1, step = "month", stepmode = "backward", label = "1M"),
                            dict(count = 3, step = "month", stepmode = "backward", label = "3M"),
                            dict(count = 6, step = "month", stepmode = "backward", label = "6M"),
                            dict(count = 1, step = "year", stepmode = "backward", label = "1Y"),
                            dict(count = 2, step = "year", stepmode = "backward", label = "2Y"),
                            dict(count = 5, step = "year", stepmode = "backward", label = "5Y"),
                            dict(count = 1, step = "all", stepmode = "backward", label = "MAX"),
                            dict(count = 1, step = "year", stepmode = "todate", label = "YTD"),
                ]
            ),

        ),
        yaxis = dict(
            tickprefix = "$",
            type = "linear",
            domain = [0.25, 1],
        ),

    )



    fig = go.Figure(data = data, layout = layout)

    candlestick_moving_average = fig.to_html(full_html=False, default_height=1000, default_width=1500)

    return candlestick_moving_average
