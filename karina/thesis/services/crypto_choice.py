from django.shortcuts import render
import re
import json
import html
import requests
import codecs
from bs4 import BeautifulSoup
import pandas as pd
from django.http import HttpResponse
import operator
from django.http import JsonResponse


from thesis.services.get_yahoo_table import get_yahoo_table
# saving the user's input and using that to download data about that ticket from Yahoo Finanace
def crypto_choice(request):

    df_cryptolist, json_three = get_yahoo_table(request)

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
        print(cryptolist)
    # getting the user's input
    crypto = request.GET.get('insert_crypto')

    if request.method == 'GET':
        if not crypto in cryptolist:
            print('Sorry. You did not select an available symbol or you misspelled the symbol')
            return render(request, 'thesis/thesis_home.html', {'error':'Sorry. You did not select an available symbol or you misspelled the symbol'})

        else:
            print('You have selected: ', crypto)
            return JsonResponse({'item': crypto}, safe=False)
