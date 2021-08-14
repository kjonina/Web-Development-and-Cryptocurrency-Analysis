from django.shortcuts import render
# from .models import Thesis
import re
import json
import html
import requests
import codecs
from bs4 import BeautifulSoup
import pandas as pd
from pandas.io.json import json_normalize
from django.http import HttpResponse
from django.http import JsonResponse
import operator
from plotly.offline import download_plotlyjs, plot
import plotly.offline as py
import plotly.graph_objs as go
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.io as pio
from fbprophet import Prophet

# taking functions from files and using them accordingly
from thesis.services.get_yahoo_table import get_yahoo_table
from thesis.services.create_df import create_df
from thesis.services.create_y import create_y
from thesis.services.candle_stick import candle_stick
from thesis.services.price_sma_volume_chart import price_sma_volume_chart
from thesis.services.hist_box_pct_change import hist_box_pct_change
from thesis.services.rolling_m_sd import rolling_m_sd
from thesis.services.get_crypto_info import get_crypto_info
from thesis.services.get_crypto_name import get_crypto_name
from thesis.services.df_train_test import create_train_and_test
from thesis.services.returns import returns
from thesis.services.decomposition import decomposition
from thesis.services.plot_acf import acf_and_pacf_plots
from thesis.services.adfuller_test import adfuller_test
from thesis.services.prophet_prediction import prophet_prediction
from thesis.services.prophet_forecast import prophet_forecast
from thesis.services.arima_prediction  import arima_prediction, arima_prediction_plot, arima_evaluation
from thesis.services.arima_forecast import arima_forecast
# from thesis.services.arima_evaluation  import arima_evaluation
# from thesis.services.prophet_evaluation import prophet_evaluation

from thesis.services.candlestick_rolling_average import candlestick_moving_average


def thesis(request):
    df_cryptolist, json_three = get_yahoo_table(request)

    if request.method == 'GET':
        # getting the user's input
        crypto = request.GET.get('crypto_ticket')
        crypto_ticket = str(crypto).upper()
        # print(crypto_ticket)

        cryptolist = []

        index = 0

        while index < len(df_cryptolist.iloc[:,0]):
            try:
                for crypto in df_cryptolist.iloc[:,0]:
                    cryptolist.append(str(crypto))
                    index += 1

            except:
                index = len(df_cryptolist.iloc[:,0])
                break
            # print(cryptolist)

        if crypto_ticket == 'NONE':
            return render(request, 'thesis/thesis_home.html', {'tablesinfo': json.loads(json_three), 'error':'Please write the cryptocurrency symbol of your choice.'})


        elif crypto_ticket in cryptolist:
            # print('You have selected: ', crypto_ticket)

            crypto_name = get_crypto_name(request, crypto_ticket)
            # print(crypto_name)

            # creating the df dataset
            df = create_df(request,  crypto_ticket, crypto_name)
            # print(df)

            # creating the df dataset
            y = create_y(request, crypto_name, crypto_ticket)
            # print(y)
            period = request.GET.get('number_value')
            period = int(period)

            df_train, df_test = create_train_and_test(request,y, crypto_name)
            fcast = arima_prediction(request, df_train, df_test, crypto_name)

            return render(request, 'thesis/thesis_home.html', {'error':'You have selected: {}'.format(str(crypto_name)),
                'get_crypto_info': json.loads(get_crypto_info(request, crypto_ticket)),
                'tablesinfo': json.loads(json_three),
                'price_sma_volume_chart': price_sma_volume_chart(request, df, crypto_name),
                'returns_chart': returns(request, df, crypto_name),
                'candlestick_moving_average': candlestick_moving_average(request, df, crypto_name),
                'hist_box_pct_change': hist_box_pct_change(request, y, crypto_name),
                'rolling_m_sd': rolling_m_sd(request, y, crypto_name, period),
                'decomposition_chart': decomposition(request, df, df['Close'], crypto_name,period),
                # 'adfuller_test': json.loads(adfuller_test(request, df['Close'], crypto_name)),
                'acf_and_pacf_plots': acf_and_pacf_plots(request, y['log_Close_diff'], crypto_name),
                'arima_prediction': arima_prediction_plot(request, fcast, df_train, df_test, crypto_name),
                'arima_evaluation' : json.loads(arima_evaluation(request, df_test, fcast)),
                'arima_forecast': arima_forecast(request, df, crypto_name),
                # 'prophet_prediction': prophet_prediction(request, df_train, df_test, crypto_name),
                # 'prophet_forecast': prophet_forecast(request, df, crypto_name)
                })
        else:
            # print('Sorry. You did not select an available symbol or you misspelled the symbol')
            return render(request, 'thesis/thesis_home.html', {'tablesinfo': json.loads(json_three), 'error':'Sorry. You did not select an available symbol or you misspelled the symbol'})

    else:
        return render(request, 'thesis/thesis_home.html')
