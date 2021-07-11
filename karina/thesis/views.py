from django.shortcuts import render
from .models import Thesis
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
from thesis.services.create_df import create_df
from thesis.services.create_y import create_y
from thesis.services.simple_graph import create_simple_graph
from thesis.services.create_first_graph import create_first_graph
from thesis.services.candle_stick import candle_stick
from thesis.services.price_sma_volume_chart import price_sma_volume_chart

# saving the user's input and using that to download data about that ticket from Yahoo Finanace
def crypto_choice(request):
    global crypto
    # getting the user's input
    crypto = request.GET['text'].upper()

    # NEEDS TO GIVE A USER AN ERROR MESSAGE IF THE INPUT IS NOT IN THE FIRST ROW-
    # if input on the first row of the table: pass
    # else: give error

    # returning the crypto choice
    return JsonResponse({'item': crypto}, safe=False)


def thesis(request):

    # creating the df dataset
    df = create_df(request,  'BTC-USD')
    #print(df)

    # creating the df dataset
    y = create_y(request,  'BTC-USD')
    #print(y)

    return render(request, 'thesis/thesis_home.html', {
    'tablesinfo': json.loads(get_yahoo_table(request)),
    'price_sma_volume_chart': price_sma_volume_chart(request, df, 'Bitcoin'),
    'candle_stick': candle_stick(request, df, 'Bitcoin')
    })
