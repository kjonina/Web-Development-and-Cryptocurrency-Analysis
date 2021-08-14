import requests

import numpy as np
import pandas as pd
import yfinance as yf
import plotly.graph_objs as go
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.io as pio
import mplfinance as mpf
import yfinance as yf
import matplotlib.pyplot as plt
import datetime as dt
from matplotlib import pyplot
import datetime
import plotly.graph_objects as go
from fbprophet import Prophet

def prophet_prediction(request, df_train, df_test, crypto_name):

    crypto = df_train[['Close', 'Name']]
    crypto = crypto.reset_index()
    crypto = crypto.rename(columns={'Date': 'ds', 'Close': 'y'})
    df_prophet = Prophet(changepoint_prior_scale=0.15,yearly_seasonality=True,daily_seasonality=True)
    df_prophet.fit(crypto)

    df_forecast = df_prophet.make_future_dataframe(periods= len(df_test), freq='D')

    df_forecast = df_prophet.predict(df_forecast)
    df_forecast['Name'] = df_test['Name']
    df_forecast['Name'] = df_forecast['Name'].replace(np.nan, crypto_name)
    return df_forecast

def prophet_prediction_plot(request, df_forecast, df_train, df_test, crypto_name):
    df_train = go.Scatter(
        x = df_train.index,
        y = df_train['Close'],
        customdata = df_train['Name'],
        hovertemplate="<b>%{customdata}</b><br><br>" +
        "Date: %{x|%d %b %Y} <br>" +
        "Closing Price: %{y:$,.2f}<br>",
        name = 'Training Set')

    df_test = go.Scatter(
        x = df_test.index,
        y = df_test['Close'],
        name = 'Test Set',
        customdata = df_test['Name'],
        hovertemplate="<b>%{customdata}</b><br><br>" +
        "Date: %{x|%d %b %Y} <br>" +
        "Closing Price: %{y:$,.2f}<br>",
        yaxis="y1")

    trend = go.Scatter(
        name = 'Trend',
        mode = 'lines',
        x = list(df_forecast['ds']),
        y = list(df_forecast['yhat']),
        customdata = df_forecast['Name'],
        hovertemplate="<b>%{customdata}</b><br><br>" +
                        "Date: %{x|%d %b %Y} <br>" +
                        "Trend: %{y:$,.2f}<br>",
        marker=dict(color='red', line=dict(width=3))
    )
    upper_band = go.Scatter(
        name = 'Upper Band',
        mode = 'lines',
        x = list(df_forecast['ds']),
        y = list(df_forecast['yhat_upper']),
        customdata = df_forecast['Name'],
        hovertemplate="<b>%{customdata}</b><br><br>" +
                        "Date: %{x|%d %b %Y} <br>" +
                        "Upper Band: %{y:$,.2f}<br>",
        line= dict(color='#57b88f'),
        fill = 'tonexty'
    )
    lower_band = go.Scatter(
        name= 'Lower Band',
        mode = 'lines',
        x = list(df_forecast['ds']),
        y = list(df_forecast['yhat_lower']),
        customdata = df_forecast['Name'],
        hovertemplate="<b>%{customdata}</b><br><br>" +
                        "Date: %{x|%d %b %Y} <br>" +
                        "Lower Band: %{y:$,.2f}<br>",
        line= dict(color='#57b88f')
       )


    data = [df_train, df_test, trend, lower_band, upper_band]

    layout = dict(title='Predicting Closing Price of {} Using FbProphet'.format(crypto_name),
                 xaxis=dict(title = 'Dates', ticklen=2, zeroline=True))

    fig = go.Figure(data = data, layout=layout)
#    fig['layout']['yaxis1']['title']='US Dollars'
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


    fig.update_layout(showlegend=False)

    prophet_prediction = fig.to_html(full_html=False, default_height=1000, default_width=1500)

    return prophet_prediction



def prophet_evaluation(request, df_forecast, df_test):

    df_forecast['dtest_trend'] = df_forecast['trend'].iloc[-len(df_test):]
    df_forecast1= df_forecast[['dtest_trend']].dropna()

    results = pd.DataFrame({'R2 Score':r2_score(df_test['Close'], df_forecast1['dtest_trend']),
                            }, index=[0])
    results['Mean Absolute Error'] = '{:.4f}'.format(np.mean(np.abs((df_test['Close'] - df_forecast1['dtest_trend']) / df_test['Close'])) * 100)
    results['Median Absolute Error'] = '{:.4f}'.format(median_absolute_error(df_test['Close'], df_forecast1['dtest_trend']))
    results['MSE'] = '{:.4f}'.format(mean_squared_error(df_test['Close'], df_forecast1['dtest_trend']))
    results['MSLE'] = '{:.4f}'.format(mean_squared_log_error(df_test['Close'], df_forecast1['dtest_trend']))
    results['MAPE'] = '{:.4f}'.format(np.mean(np.abs((df_test['Close'] - df_forecast1['dtest_trend']) / df_test['Close'])) * 100)
    results['RMSE'] = '{:.4f}'.format(np.sqrt(float(results['MSE'])))

    results = pd.DataFrame(results).transpose()
    results = results.reset_index()
    return results.to_json(orient='records')
