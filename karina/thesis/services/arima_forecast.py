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

def arima_forecast(request, df, crypto_name):

    # Construct the model
    #    mod = sm.tsa.SARIMAX(y[['Close']], order=(1, 0, 0), trend='c')

    mod =ARIMA(df['Close'], order=(6,1,3))
    # Estimate the parameters
    res = mod.fit()
    # print(res.summary())


    # Forecasting out-of-sample
    forecast = res.get_forecast(steps=120, dynamic = True)

    # # Confidence level of 90%
    # print('============================================================')
    # print('Forecast')
    # print('============================================================')
    # print(forecast.summary_frame(alpha=0.10).tail())

    # Construct the forecasts
    fcast = res.get_forecast('2021-12-30').summary_frame()

    # print(fcast.index)
    y_upper = fcast['mean_ci_upper']
    y_lower = fcast['mean_ci_lower']

    # a plotly graph for training and test set
    trace1 = go.Scatter(
        x = df.index,
        y = df['Close'],
        customdata = df['Name'],
        hovertemplate="<b>%{customdata}</b><br><br>" +
        "Date: %{x|%d %b %Y} <br>" +
        "Closing Price: %{y:$,.2f}<br>"+
        "<extra></extra>")


    trace2 = go.Scatter(
        x=y_upper.index,
        y=y_upper,
        line = dict(color='green'),
#        name = 'Predicted2',
        customdata = df['Name'],
        hovertemplate="<b>%{customdata}</b><br><br>" +
        "Date: %{x|%d %b %Y} <br>" +
        "Predicted Closing Price: %{y:$,.2f}<br>"+
        "<extra></extra>")


    trace3 = go.Scatter(
        x=y_lower.index,
        y= y_lower,
        line = dict(color='green'),
#        name = 'Predicted Lower Confidence ',
        customdata = df['Name'],
        hovertemplate="<b>%{customdata}</b><br><br>" +
        "Date: %{x|%d %b %Y} <br>" +
        "Predicted Closing Price: %{y:$,.2f}<br>"+
        "<extra></extra>",
        fill='tonexty'
        )


    trace4 = go.Scatter(
        x=fcast['mean_ci_upper'].index,
        y=fcast['mean'],
#        name = 'Predicted',
        line = dict(color='firebrick', width=4, dash='dot'),
        customdata = df['Name'],
        hovertemplate="<b>%{customdata}</b><br><br>" +
        "Date: %{x|%d %b %Y} <br>" +
        "Predicted Closing Price: %{y:$,.2f}<br>"+
        "<extra></extra>")



    data = [trace1, trace2, trace3, trace4]
    fig = go.Figure(data = data)
    fig.update_layout(showlegend=False)

    fig.update_layout({'title': {'text':'ARIMA Forecasting of {}'.format(str(crypto_name))}},
                      yaxis_tickprefix = '$', yaxis_tickformat = ',.')

    arima_forecast = fig.to_html(full_html=False, default_height=1000, default_width=1500)
    return arima_forecast
