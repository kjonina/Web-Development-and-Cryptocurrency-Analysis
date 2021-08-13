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
    forecast = results.get_forecast(steps=219, dynamic = True)

    # Confidence level of 90%
    fcast = forecast.summary_frame(alpha=0.10)
    # print('============================================================')
    # print('Forecast')
    # print('============================================================')
    # print(fcast.tail())

    # a plotly graph for training and test set
    trace1 = go.Scatter(
        x = df_train.index,
        y = df_train['Close'],
        customdata = df_train['Name'],
        hovertemplate="<b>%{customdata}</b><br><br>" +
        "Date: %{x|%d %b %Y} <br>" +
        "Closing Price: %{y:$,.2f}<br>"+
        "<extra></extra>")

    trace5 = go.Scatter(
        x = df_test.index,
        y = df_test['Close'],
        name = 'Test Set',
        customdata = df_test['Name'],
        hovertemplate="<b>%{customdata}</b><br><br>" +
        "Date: %{x|%d %b %Y} <br>" +
        "Closing Price: %{y:$,.2f}<br>"+
        "<extra></extra>",
        yaxis="y1")

    y_upper = fcast['mean_ci_upper']
    y_lower = fcast['mean_ci_lower']

    trace2 = go.Scatter(
        x=df_test.index,
        y=y_upper,
        line = dict(color='green'),
#        name = 'Predicted2',
        customdata = df_test['Name'],
        hovertemplate="<b>%{customdata}</b><br><br>" +
        "Date: %{x|%d %b %Y} <br>" +
        "Predicted Closing Price: %{y:$,.2f}<br>"+
        "<extra></extra>")


    trace3 = go.Scatter(
        x=df_test.index,
        y= y_lower,
        line = dict(color='green'),
#        name = 'Predicted Lower Confidence ',
        customdata = df_test['Name'],
        hovertemplate="<b>%{customdata}</b><br><br>" +
        "Date: %{x|%d %b %Y} <br>" +
        "Predicted Closing Price: %{y:$,.2f}<br>"+
        "<extra></extra>",
        fill='tonexty'
        )


    trace4 = go.Scatter(
        x=df_test.index,
        y=fcast['mean'],
#        name = 'Predicted',
        line = dict(color='firebrick', width=4, dash='dot'),
        customdata = df_test['Name'],
        hovertemplate="<b>%{customdata}</b><br><br>" +
        "Date: %{x|%d %b %Y} <br>" +
        "Predicted Closing Price: %{y:$,.2f}<br>"+
        "<extra></extra>")



    data = [trace1, trace2, trace3, trace4, trace5]
    fig = go.Figure(data = data)
    fig.update_layout(showlegend=False)

    fig.update_layout({'title': {'text':'ARIMA Forecasting of {}'.format(str(crypto_name))}},
                      yaxis_tickprefix = '$', yaxis_tickformat = ',.')

    arima_prediction = fig.to_html(full_html=False, default_height=1000, default_width=1500)
    return arima_prediction
