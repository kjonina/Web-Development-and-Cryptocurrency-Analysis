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

# saving the user's input and using that to download data about that ticket from Yahoo Finanace
def crypto_choice(request):
    # getting the user's input
    crypto = request.GET['insert_crypto']
    print(crypto)

    # NEEDS TO GIVE A USER AN ERROR MESSAGE IF THE INPUT IS NOT IN THE FIRST ROW-
    # if input on the first row of the table: pass
    # else: give error

    # returning the crypto choice
    return JsonResponse({'item': crypto}, safe=False)
