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

def arima_prediction_plot(request, fcast, df_train, df_test,  test_period, crypto_name):
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


    fig.update_layout(title = 'Predicting Closing Price of {} Using ARIMA for {} days'.format(test_period, crypto_name),
            title_font_size=30)
    fig.update_layout(yaxis_tickprefix = '$', yaxis_tickformat = ',.')

    arima_prediction = fig.to_html(full_html=False, default_height=1000, default_width=1500)
    return arima_prediction

from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error, median_absolute_error, mean_squared_log_error
from math import sqrt



def arima_evaluation(request, df_test, fcast):
    results = pd.DataFrame({'R2 Score':r2_score(df_test['Close'], fcast['mean_se']),
                           }, index=[0])
    results['Mean Absolute Error'] = '{:.4f}'.format(np.mean(np.abs((df_test['Close'] - fcast['mean_se']) / df_test['Close'])) * 100)
    results['Median Absolute Error'] = '{:.4f}'.format(median_absolute_error(df_test['Close'], fcast['mean_se']))
    results['MSE'] = '{:.4f}'.format(mean_squared_error(df_test['Close'], fcast['mean_se']))
    results['MSLE'] = '{:.4f}'.format(mean_squared_log_error(df_test['Close'], fcast['mean_se']))
    results['MAPE'] = '{:.4f}'.format(np.mean(np.abs((df_test['Close'] - fcast['mean_se']) / df_test['Close'])) * 100)
    results['RMSE'] = '{:.4f}'.format(np.sqrt(float(results['MSE'])))

    results = pd.DataFrame(results).transpose()
    results = results.reset_index()
    return results.to_json(orient='records')
