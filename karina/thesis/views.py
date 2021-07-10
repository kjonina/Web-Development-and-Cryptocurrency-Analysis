from django.shortcuts import render
from .models import Thesis
import re
import json
import requests
import codecs
from bs4 import BeautifulSoup
import pandas as pd
from pandas.io.json import json_normalize
from django.http import HttpResponse
import operator
from django.http import JsonResponse

# including python
from thesis.services.get_yahoo_table import get_yahoo_table
from thesis.services.create_df import create_df
from thesis.services.create_first_graph import create_first_graph




def crypto_choice(request):
    crypto = request.GET['text']
    create_df(request, crypto)
    create_first_graph(request)
    return JsonResponse({'item': crypto}, safe=False)

def thesis(request):
    #thesis = Thesis.objects
    return render(request, 'thesis/thesis_home.html', {
    #'thesis': thesis,
    'tablesinfo': json.loads(get_yahoo_table(request)),
#    'insert_crypto': insert_crypto
    })
