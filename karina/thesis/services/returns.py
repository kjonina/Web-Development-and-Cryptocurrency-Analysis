
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





def returns(request, df, crypto_name):
    fig = make_subplots(rows=4, cols=1, shared_xaxes=False, subplot_titles=[
            'Closing Price of {}'.format(str(crypto_name)),
            'Daily Return of {}'.format(str(crypto_name)),
            'Monthly Return of {}'.format(str(crypto_name)),
            'Annual Return of {}'.format(str(crypto_name))])
    fig.add_trace(go.Scatter(
                            x = df.index,
                            y = df['Close'],
                            mode='lines',
                            customdata = df['Name'], name = 'Closing Price',
                            hovertemplate="<b>%{customdata}</b><br><br>" +
                                            "Date: %{x|%d %b %Y} <br>" +
                                            "Closing Price: %{y:$,.2f}<br>"+
                                            "<extra></extra>"), row = 1, col = 1)

    fig.add_trace(go.Scatter(
                            x = df.index,
                            y = df['daily_return'],
                            mode='lines',
                            customdata = df['Name'], name = 'Daily Return',
                            hovertemplate="<b>%{customdata}</b><br><br>" +
                                            "Date: %{x|%d %b %Y} <br>" +
                                            "Daily Return: %{y:,.0%}<br>"+
                                            "<extra></extra>"), row = 2, col = 1)

    fig.add_trace(go.Scatter(
                            x = df.index,
                            y = df['monthly_return'],
                            mode='lines',
                            customdata = df['Name'], name = 'Monthly Return',
                            hovertemplate="<b>%{customdata}</b><br><br>" +
                                            "Date: %{x|%d %b %Y} <br>" +
                                            "Monthly Return: %{y:,.0%}<br>"+
                                            "<extra></extra>"), row = 3, col = 1)

    fig.add_trace(go.Scatter(
                            x = df.index,
                            y = df['annual_return'],
                            mode='lines',
                            customdata = df['Name'], name = 'Annual Return',
                            hovertemplate="<b>%{customdata}</b><br><br>" +
                                            "Date: %{x|%d %b %Y} <br>" +
                                            "Annual Return: %{y:,.0%}<br>"+
                                            "<extra></extra>"), row = 4, col = 1)

    # Add titles
    fig.update_layout(
            title = 'Price of {}'.format(str(crypto_name)))
    fig['layout']['yaxis1']['title']='US Dollars'
    fig['layout']['yaxis2']['title']='% Return'
    fig['layout']['yaxis3']['title']='% Return'
    fig['layout']['yaxis4']['title']='% Return'
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
    fig.update_layout(xaxis_rangeslider_visible=False)
    fig.update_xaxes(rangeslider= {'visible':False}, row=2, col=1)
    fig.update_xaxes(rangeslider= {'visible':False}, row=3, col=1)
    fig.update_xaxes(rangeslider= {'visible':False}, row=4, col=1)

    fig.update_xaxes(rangeselector= {'visible':False}, row=2, col=1)
    fig.update_xaxes(rangeselector= {'visible':False}, row=3, col=1)
    fig.update_xaxes(rangeselector= {'visible':False}, row=4, col=1)

    fig.update_yaxes(tickprefix = '$', tickformat = ',.', row = 1, col = 1)
    fig.update_yaxes(tickformat = ',.0%', row = 2, col = 1)
    fig.update_yaxes(tickformat = ',.0%', row = 3, col = 1)
    fig.update_yaxes(tickformat = ',.0%', row = 4, col = 1)

    fig.update_layout(showlegend=False)
    returns_chart = fig.to_html(full_html=False, default_height=1000, default_width=1500)

    return returns_chart
