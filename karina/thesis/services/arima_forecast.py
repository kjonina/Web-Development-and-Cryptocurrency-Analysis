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

from pandas.plotting import register_matplotlib_converters

from statsmodels.tsa.arima.model import ARIMA

def arima_forecast(request, df, crypto_name, forecasting_period):

    # Construct the model
    #    mod = sm.tsa.SARIMAX(y[['Close']], order=(1, 0, 0), trend='c')

    mod =ARIMA(df['Close'], order=(6,1,3))
    # Estimate the parameters
    res = mod.fit()
    # print(res.summary())


    # Forecasting out-of-sample
    forecast = res.get_forecast(steps=forecasting_period, dynamic = True)

    # # Confidence level of 90%
    # print('============================================================')
    # print('Forecast')
    # print('============================================================')
    # print(forecast.summary_frame(alpha=0.10).tail())

    # Construct the forecasts
    fcast = res.get_forecast('2021-09-30').summary_frame()

    # print(fcast.index)
    y_upper = fcast['mean_ci_upper']
    y_lower = fcast['mean_ci_lower']

    # a plotly graph for training and test set
    actual = go.Scatter(
        x = df.index,
        y = df['Close'],
        customdata = df['Name'],name = 'Acutal Price',
        hovertemplate="<b>%{customdata}</b><br><br>" +
        "Date: %{x|%d %b %Y} <br>" +
        "Closing Price: %{y:$,.2f}<br>")


    upper_band = go.Scatter(
        x=y_upper.index,
        y=y_upper,
        name = 'Upper Band',
        customdata = df['Name'],
        hovertemplate="<b>%{customdata}</b><br><br>" +
        "Date: %{x|%d %b %Y} <br>" +
        "Predicted Closing Price: %{y:$,.2f}<br>",
        line= dict(color='#57b88f')
        )


    lower_band = go.Scatter(
        x=y_lower.index,
        y= y_lower,
        name = 'Lower Band',
        line= dict(color='#57b88f'),
        customdata = df['Name'],
        hovertemplate="<b>%{customdata}</b><br><br>" +
        "Date: %{x|%d %b %Y} <br>" +
        "Predicted Closing Price: %{y:$,.2f}<br>",
        fill='tonexty',

        )


    mean = go.Scatter(
        x=fcast['mean_ci_upper'].index,
        y=fcast['mean'],name = 'Predicted',
        marker=dict(color='red', line=dict(width=3)),
        customdata = df['Name'],
        hovertemplate="<b>%{customdata}</b><br><br>" +
        "Date: %{x|%d %b %Y} <br>" +
        "Predicted Closing Price: %{y:$,.2f}<br>")



    data = [actual, upper_band, lower_band, mean]
    fig = go.Figure(data = data)
    fig.update_layout(showlegend=False)
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

    fig.update_layout(title = 'Forecasting Closing Price of {} Using ARIMA for {} days'.format(str(crypto_name), forecasting_period),
            title_font_size=30)

    fig.update_layout(yaxis_tickprefix = '$', yaxis_tickformat = ',.')

    arima_forecast = fig.to_html(full_html=False, default_height=1000, default_width=1500)
    return arima_forecast
