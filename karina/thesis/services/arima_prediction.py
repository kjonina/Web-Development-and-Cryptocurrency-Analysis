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
import re
import json
import requests
import codecs

from pandas.plotting import register_matplotlib_converters

from statsmodels.tsa.arima.model import ARIMA

def arima_prediction(request, df_train, df_test, crypto_name):

    # Instantiate the model
    model =  ARIMA(df_train['Close'], order=(6,1,3))

    # Fit the model
    results = model.fit()

    # Print summary
    # print(results.summary())

#    start_index = df_test.index.min()
#    end_index = df_test.index.max()


    #Predictions
    forecast = results.get_forecast(steps=len(df_test), dynamic = True)

    # Confidence level of 90%
    fcast = forecast.summary_frame(alpha=0.10)
    # print('============================================================')
    # print('Forecast')
    # print('============================================================')
    # print(fcast.tail())
    return fcast

def arima_prediction_plot(request, fcast, df_train, df_test, crypto_name):
    # a plotly graph for training and test set
    df_train = go.Scatter(
        x = df_train.index,
        y = df_train['Close'],
        name = 'Training Set',
        customdata = df_train['Name'],
        hovertemplate="<b>%{customdata}</b><br><br>" +
        "Date: %{x|%d %b %Y} <br>" +
        "Closing Price: %{y:$,.2f}<br>")

    dt_test = go.Scatter(
        x = df_test.index,
        y = df_test['Close'],
        name = 'Test Set',
        customdata = df_test['Name'],
        hovertemplate="<b>%{customdata}</b><br><br>" +
        "Date: %{x|%d %b %Y} <br>" +
        "Closing Price: %{y:$,.2f}<br>",
        yaxis="y1")

    y_upper = fcast['mean_ci_upper']
    y_lower = fcast['mean_ci_lower']

    upper_band = go.Scatter(
        x=df_test.index,
        y=y_upper,
        line= dict(color='#57b88f'),
        name = 'Upper Band',
        customdata = df_test['Name'],
        hovertemplate="<b>%{customdata}</b><br><br>" +
        "Date: %{x|%d %b %Y} <br>" +
        "Predicted Closing Price: %{y:$,.2f}<br>")


    lower_band = go.Scatter(
        x = df_test.index,
        y = y_lower,
        line = dict(color='#57b88f'),
        name = 'Lower Band',
        customdata = df_test['Name'],
        hovertemplate="<b>%{customdata}</b><br><br>" +
        "Date: %{x|%d %b %Y} <br>" +
        "Predicted Closing Price: %{y:$,.2f}<br>",
        fill='tonexty'
        )


    mean = go.Scatter(
        x=df_test.index,
        y=fcast['mean'],
        name = 'Predicted',
        marker=dict(color='red', line=dict(width=3)),
        customdata = df_test['Name'],
        hovertemplate="<b>%{customdata}</b><br><br>" +
        "Date: %{x|%d %b %Y} <br>" +
        "Predicted Closing Price: %{y:$,.2f}<br>")



    data = [df_train, dt_test, upper_band, lower_band, mean]
    fig = go.Figure(data = data)
    fig.update_layout(showlegend=False)

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

    fig.update_layout({'title': {'text': '{} Price Forecasting Estimation Using ARIMA'.format(str(crypto_name))}},
                      yaxis_tickprefix = '$', yaxis_tickformat = ',.')

    arima_prediction = fig.to_html(full_html=False, default_height=1000, default_width=1500)
    return arima_prediction

from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error, median_absolute_error, mean_squared_log_error
from math import sqrt



def arima_evaluation(request, df_test, fcast):
    results = pd.DataFrame({'r2_score':r2_score(df_test['Close'], fcast['mean_se']),
                           }, index=[0])
    results['mean_absolute_error'] = '{:.4f}'.format(np.mean(np.abs((df_test['Close'] - fcast['mean_se']) / df_test['Close'])) * 100)
    results['median_absolute_error'] = '{:.4f}'.format(median_absolute_error(df_test['Close'], fcast['mean_se']))
    results['mse'] = '{:.4f}'.format(mean_squared_error(df_test['Close'], fcast['mean_se']))
    results['msle'] = '{:.4f}'.format(mean_squared_log_error(df_test['Close'], fcast['mean_se']))
    results['mape'] = '{:.4f}'.format(np.mean(np.abs((df_test['Close'] - fcast['mean_se']) / df_test['Close'])) * 100)
    results['rmse'] = '{:.4f}'.format(np.sqrt(float(results['mse'])))

    results = pd.DataFrame(results).transpose()
    results = results.reset_index()
    return results.to_json(orient='records')
