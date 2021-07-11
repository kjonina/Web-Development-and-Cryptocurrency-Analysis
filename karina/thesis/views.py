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


# taking functions from files and using them accordingly
from thesis.services.get_yahoo_table import get_yahoo_table
from thesis.services.create_df import create_df
from thesis.services.create_y import create_y
from thesis.services.simple_graph import create_simple_graph
from thesis.services.create_first_graph import create_first_graph

# saving the user's input and using that to download data about that ticket from Yahoo Finanace
def crypto_choice(request):
    global crypto, graph
    # getting the user's input
    crypto = request.GET['text'].upper()

    # NEEDS TO GIVE A USER AN ERROR MESSAGE IF THE INPUT IS NOT IN THE FIRST ROW-
    # if input on the first row of the table: pass
    # else: give error

    # creating the df dataset
    df = create_df(request, crypto)
    #print(df)

    # creating the df dataset
    y = create_y(request, crypto)
    #print(y)

    # returning the crypto choice
    return JsonResponse({'item': crypto,
    }, safe=False)

def thesis(request):

    simple_graph = create_simple_graph(request),
    #thesis = Thesis.objects
    return render(request, 'thesis/thesis_home.html', {
    #'thesis': thesis,
    'simple_graph': simple_graph,
    'tablesinfo': json.loads(get_yahoo_table(request)),


    })
