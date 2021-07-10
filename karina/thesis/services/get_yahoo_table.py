import re
import json
import requests
import codecs
from bs4 import BeautifulSoup
import pandas as pd
from pandas.io.json import json_normalize

# getting the live page
def get_yahoo_table(request):
    global df_cryptolist

    headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36'}
    url = 'https://finance.yahoo.com/cryptocurrencies/'
    # url = 'https://coinmarketcap.com/'
    response = requests.get(url , headers = headers)
    content = response.content
    soup = BeautifulSoup(content, features="html.parser")
    pattern = re.compile(r'\s--\sData\s--\s')
    script_data = soup.find('script', text = pattern).contents[0]
    start = script_data.find("context")-2
    json_data = json.loads(script_data[start:-12])
    # this is where the data is
    crypto_json = json_data['context']['dispatcher']['stores']['ScreenerResultsStore']['results']['rows']
    # normalising the list
    df_cryptolist = pd.io.json.json_normalize(crypto_json)
    # creating a dataset with the right columns and correct column names
    df_cryptolist = pd.DataFrame({'Symbol': df_cryptolist['symbol'],
                   'Name': df_cryptolist['shortName'],
                   'Price (Intraday)': df_cryptolist['regularMarketPrice.fmt'],
                   'Change': df_cryptolist['regularMarketChange.fmt'],
                   '% Change': df_cryptolist['regularMarketChangePercent.fmt'],
                   'Market Cap': df_cryptolist['marketCap.fmt'],
                   'Volume in Currency (Since 0:00 UTC)': df_cryptolist['regularMarketVolume.fmt'],
                   'Volume in Currency (24Hr)': df_cryptolist['volume24Hr.fmt'],
                   'Total Volume All Currencies (24Hr)': df_cryptolist['volumeAllCurrencies.fmt'],
                   'Circulating Supply': df_cryptolist['circulatingSupply.fmt']})

    present_cryptos = df_cryptolist[['Symbol','Name','Market Cap']].head(10)
    return present_cryptos.to_json(orient='records')
