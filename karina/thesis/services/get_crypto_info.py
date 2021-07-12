from django.shortcuts import render
import re
import json
import html
import requests
import codecs
from bs4 import BeautifulSoup
import pandas as pd

from thesis.services.get_df_cryptolist import get_df_cryptolist

def get_crypto_info(request, crypto):
    # getting a df of cryptolist downloaded from the yahoo finance
    df_cryptolist = get_df_cryptolist(request)
    # checking whether it works
    #print(df_cryptolist)

    #trying to present the information
    df_new = df_cryptolist.copy()
    df_new.set_index("Symbol", inplace=True)
    info_on_crypto = df_new.loc[crypto]
    info_on_crypto = info_on_crypto.reset_index(drop=False)
    print(info_on_crypto.reset_index(drop=True))
    return info_on_crypto.to_json(orient='records')
