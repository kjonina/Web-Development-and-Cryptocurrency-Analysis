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
#
# def prophet_forecast(request, df, crypto_name):
#
#     crypto = df[['Close', 'Name']]
#     crypto = crypto.reset_index()
#     crypto = crypto.rename(columns={'Date': 'ds', 'Close': 'y'})
#     df_prophet = Prophet(changepoint_prior_scale=0.15,yearly_seasonality=True,daily_seasonality=True)
#     df_prophet.fit(crypto)
#
#     df_forecast = df_prophet.make_future_dataframe(periods= 120, freq='D')
#
#     df_forecast = df_prophet.predict(df_forecast)
#     df_forecast['Name'] = crypto['Name']
#     df_forecast['Name'] = df_forecast['Name'].replace(np.nan, crypto_name)
#
#     actual = go.Scatter(
#         x = df.index,
#         y = df['Close'],
#         customdata = df['Name'],
#         hovertemplate="<b>%{customdata}</b><br><br>" +
#         "Date: %{x|%d %b %Y} <br>" +
#         "Closing Price: %{y:$,.2f}<br>",
#         name = 'Actual Price',
#         marker = dict(line = dict(width=1))
#         )
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
#
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
#
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
#     data = [trend, lower_band, upper_band, actual]
#
#     layout = dict(title='Forecasting Closing Price of {} Using FbProphet'.format(crypto_name),
#                 title_font_size=30, xaxis=dict(title = 'Dates', ticklen=2, zeroline=True))
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
#     fig.update_layout(showlegend=False)
#
#     prophet_forecast = fig.to_html(full_html=False, default_height=1000, default_width=1500)
#
#     return prophet_forecast
