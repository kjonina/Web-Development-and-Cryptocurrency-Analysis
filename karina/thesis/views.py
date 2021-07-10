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
from thesis.services.simple_graph import create_simple_graph

# saving the user's input and using that to download data about that ticket from Yahoo Finanace
def crypto_choice(request):
    # getting the user's input
    crypto = request.GET['text'].upper()

    # NEEDS TO GIVE A USER AN ERROR MESSAGE IF THE INPUT IS NOT IN THE FIRST ROW-
    # if input on the first row of the table: pass
    # else: give error

    # creating the dataset
    create_df(request, crypto)
    # returning the crypto choice
    return JsonResponse({'item': crypto}, safe=False)



def thesis(request):
    #thesis = Thesis.objects
    graph = create_simple_graph(request)
    return render(request, 'thesis/thesis_home.html', {
    #'thesis': thesis,
    'tablesinfo': json.loads(get_yahoo_table(request)),
    'graph': graph,

    })
