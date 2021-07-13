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
