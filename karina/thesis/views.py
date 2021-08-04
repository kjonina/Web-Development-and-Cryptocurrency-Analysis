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
from thesis.services.training_and_test_plot import training_and_test_plot
from thesis.services.returns import returns
from thesis.services.decomposition import decomposition
from thesis.services.prediction1 import prediction1
from thesis.services.prediction2 import prediction2
from thesis.services.prediction3 import prediction3

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
            y = create_y(request,  crypto_ticket, crypto_name)
            # print(y)

            df_train, df_test = create_train_and_test(request,y, crypto_name)

            return render(request, 'thesis/thesis_home.html', {'error':'You have selected: {}'.format(str(crypto_name)),
                'get_crypto_info': json.loads(get_crypto_info(request, crypto_ticket)),
                'tablesinfo': json.loads(json_three),
                'price_sma_volume_chart': price_sma_volume_chart(request, df, crypto_name),
                'candlestick_moving_average': candlestick_moving_average(request, df, crypto_name),
                'hist_box_pct_change': hist_box_pct_change(request, y, crypto_name),
                'training_and_test_plot': training_and_test_plot(request,df_train, df_test, crypto_name),
                'rolling_m_sd': rolling_m_sd(request, y, crypto_name),
                'decomposition_chart': decomposition(request, df, df['Close'], crypto_name),
                'prediction1': prediction1(request, df_train, df_test, crypto_name),
                'prediction2': prediction2(request, df_train, df_test, crypto_name),
                'prediction3': prediction3(request, df, crypto_name),
                'returns_chart': returns(request, df, crypto_name)})
        else:
            # print('Sorry. You did not select an available symbol or you misspelled the symbol')
            return render(request, 'thesis/thesis_home.html', {'tablesinfo': json.loads(json_three), 'error':'Sorry. You did not select an available symbol or you misspelled the symbol'})

    else:
        return render(request, 'thesis/thesis_home.html')
