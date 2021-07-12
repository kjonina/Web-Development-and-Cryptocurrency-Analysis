from django.shortcuts import render
import re
import json
import html
import requests
import codecs
from bs4 import BeautifulSoup
import pandas as pd

from thesis.services.get_df_cryptolist import get_df_cryptolist

def get_crypto_name(request, crypto):
    # getting a df of cryptolist downloaded from the yahoo finance
    df_cryptolist = get_df_cryptolist(request)
    # checking whether it works
    #print(df_cryptolist)

    # trying to get the name now
    crypto_name = str(df_cryptolist[df_cryptolist['Symbol'].str.contains(crypto)].iloc[:,1]).split(' ')[4]
    #print(crypto_name)
    return crypto_name
