from django.shortcuts import render
import re
import json
import html
import requests
import codecs
from bs4 import BeautifulSoup
import pandas as pd
from pandas.io.json import json_normalize
from django.http import HttpResponse
import operator
from django.http import JsonResponse
from plotly.offline import download_plotlyjs, plot
import plotly.offline as py
import plotly.graph_objs as go
import plotly.graph_objects as go
import plotly.graph_objs as go
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.io as pio
import plotly.offline as py
from plotly.offline import download_plotlyjs, plot

# taking functions from files and using them accordingly
from thesis.services.get_yahoo_table import get_yahoo_table
from thesis.services.get_df_cryptolist import get_df_cryptolist
from thesis.services.create_df import create_df
from thesis.services.create_y import create_y
from thesis.services.candle_stick import candle_stick
from thesis.services.price_sma_volume_chart import price_sma_volume_chart
from thesis.services.hist_box_pct_change import hist_box_pct_change
from thesis.services.rolling_m_sd import rolling_m_sd

from thesis.services.get_crypto_info import get_crypto_info
from thesis.services.get_crypto_name import get_crypto_name
from thesis.services.crypto_choice import crypto_choice


def thesis(request):
    crypto_name = get_crypto_name(request, 'ETH-USD')

    # creating the df dataset
    df = create_df(request,  'ETH-USD', crypto_name)
    #print(df)

    # creating the df dataset
    y = create_y(request,  'ETH-USD', crypto_name)
    #print(y)

    return render(request, 'thesis/thesis_home.html', {
    'get_crypto_info': json.loads(get_crypto_info(request, 'ETH-USD')),
    'tablesinfo': json.loads(get_yahoo_table(request)),
    'price_sma_volume_chart': price_sma_volume_chart(request, df, crypto_name),
    'candle_stick': candle_stick(request, df, crypto_name),
    'hist_box_pct_change': hist_box_pct_change(request, y, crypto_name),
    'rolling_m_sd': rolling_m_sd(request, y, crypto_name)
    })
