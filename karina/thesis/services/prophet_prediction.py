# import requests
#
# import numpy as np
# import pandas as pd
# import yfinance as yf
# import plotly.graph_objs as go
# import plotly.express as px
# from plotly.subplots import make_subplots
# import plotly.io as pio
# import mplfinance as mpf
# import yfinance as yf
# import matplotlib.pyplot as plt
# import datetime as dt
# from matplotlib import pyplot
# import datetime
# import plotly.graph_objects as go
# from fbprophet import Prophet
#
# def prophet_prediction(request, df_train, df_test, crypto_name):
#
#     crypto = df_train[['Close', 'Name']]
#     crypto = crypto.reset_index()
#     crypto = crypto.rename(columns={'Date': 'ds', 'Close': 'y'})
#     df_prophet = Prophet(changepoint_prior_scale=0.15,yearly_seasonality=True,daily_seasonality=True)
#     df_prophet.fit(crypto)
#
#     df_forecast = df_prophet.make_future_dataframe(periods= len(df_test), freq='D')
#
#     df_forecast = df_prophet.predict(df_forecast)
#     df_forecast['Name'] = df_test['Name']
#     df_forecast['Name'] = df_forecast['Name'].replace(np.nan, crypto_name)
#     return df_forecast
#
# def prophet_prediction_plot(request, df_forecast, df_train, df_test, crypto_name):
#     df_train = go.Scatter(
#         x = df_train.index,
#         y = df_train['Close'],
#         customdata = df_train['Name'],
#         hovertemplate="<b>%{customdata}</b><br><br>" +
#         "Date: %{x|%d %b %Y} <br>" +
#         "Closing Price: %{y:$,.2f}<br>",
#         name = 'Training Set')
#
#     df_test = go.Scatter(
#         x = df_test.index,
#         y = df_test['Close'],
#         name = 'Test Set',
#         customdata = df_test['Name'],
#         hovertemplate="<b>%{customdata}</b><br><br>" +
#         "Date: %{x|%d %b %Y} <br>" +
#         "Closing Price: %{y:$,.2f}<br>",
#         yaxis="y1")
#
#     trend = go.Scatter(
#         name = 'Trend',
#         mode = 'lines',
#         x = list(df_forecast['ds']),
#         y = list(df_forecast['yhat']),
#         customdata = df_forecast['Name'],
#         hovertemplate="<b>%{customdata}</b><br><br>" +
#                         "Date: %{x|%d %b %Y} <br>" +
#                         "Trend: %{y:$,.2f}<br>",
#         marker=dict(color='red', line=dict(width=3))
#     )
#     upper_band = go.Scatter(
#         name = 'Upper Band',
#         mode = 'lines',
#         x = list(df_forecast['ds']),
#         y = list(df_forecast['yhat_upper']),
#         customdata = df_forecast['Name'],
#         hovertemplate="<b>%{customdata}</b><br><br>" +
#                         "Date: %{x|%d %b %Y} <br>" +
#                         "Upper Band: %{y:$,.2f}<br>",
#         line= dict(color='#57b88f'),
#         fill = 'tonexty'
#     )
#     lower_band = go.Scatter(
#         name= 'Lower Band',
#         mode = 'lines',
#         x = list(df_forecast['ds']),
#         y = list(df_forecast['yhat_lower']),
#         customdata = df_forecast['Name'],
#         hovertemplate="<b>%{customdata}</b><br><br>" +
#                         "Date: %{x|%d %b %Y} <br>" +
#                         "Lower Band: %{y:$,.2f}<br>",
#         line= dict(color='#57b88f')
#        )
#
#
#     data = [df_train, df_test, trend, lower_band, upper_band]
#
#     layout = dict(title='Predicting Closing Price of {} Using FbProphet'.format(crypto_name),
#                  xaxis=dict(title = 'Dates', ticklen=2, zeroline=True))
#
#     fig = go.Figure(data = data, layout=layout)
# #    fig['layout']['yaxis1']['title']='US Dollars'
#     # X-Axes
#     fig.update_xaxes(
#         rangeslider_visible = True,
#         rangeselector = dict(
#             buttons = list([
#                             dict(count = 7, step = "day", stepmode = "backward", label = "1W"),
#                             dict(count = 1, step = "month", stepmode = "backward", label = "1M"),
#                             dict(count = 3, step = "month", stepmode = "backward", label = "3M"),
#                             dict(count = 6, step = "month", stepmode = "backward", label = "6M"),
#                             dict(count = 1, step = "year", stepmode = "backward", label = "1Y"),
#                             dict(count = 2, step = "year", stepmode = "backward", label = "2Y"),
#                             dict(count = 5, step = "year", stepmode = "backward", label = "5Y"),
#                             dict(count = 1, step = "all", stepmode = "backward", label = "MAX"),
#                             dict(count = 1, step = "year", stepmode = "todate", label = "YTD")])))
#     fig.update_layout(xaxis_rangeslider_visible = False)
#     fig.update_yaxes(tickprefix = '$', tickformat = ',.')
#
#
#     fig.update_layout(showlegend=False)
#
#     prophet_prediction = fig.to_html(full_html=False, default_height=1000, default_width=1500)
#
#     return prophet_prediction
#
#
#
# from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error, median_absolute_error, mean_squared_log_error
# from math import sqrt
#
# def prophet_evaluation(request, df_forecast, df_test):
#
#     df_forecast['dtest_trend'] = df_forecast['trend'].iloc[-len(df_test):]
#     df_forecast1= df_forecast[['dtest_trend']].dropna()
#
#     results = pd.DataFrame({'R2 Score':r2_score(df_test['Close'], df_forecast1['dtest_trend']),
#                             }, index=[0])
#     results['Mean Absolute Error'] = '{:.4f}'.format(np.mean(np.abs((df_test['Close'] - df_forecast1['dtest_trend']) / df_test['Close'])) * 100)
#     results['Median Absolute Error'] = '{:.4f}'.format(median_absolute_error(df_test['Close'], df_forecast1['dtest_trend']))
#     results['MSE'] = '{:.4f}'.format(mean_squared_error(df_test['Close'], df_forecast1['dtest_trend']))
#     results['MSLE'] = '{:.4f}'.format(mean_squared_log_error(df_test['Close'], df_forecast1['dtest_trend']))
#     results['MAPE'] = '{:.4f}'.format(np.mean(np.abs((df_test['Close'] - df_forecast1['dtest_trend']) / df_test['Close'])) * 100)
#     results['RMSE'] = '{:.4f}'.format(np.sqrt(float(results['MSE'])))
#
#     results = pd.DataFrame(results).transpose()
#     results = results.reset_index()
#     return results.to_json(orient='records')
