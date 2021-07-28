# Downloading necessary files
import numpy as np
import pandas as pd
import yfinance as yf
from matplotlib import pyplot
import matplotlib.pyplot as plt
from datetime import datetime
import datetime as dt
import plotly.graph_objects as go
import plotly.graph_objs as go
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.io as pio
import plotly.offline as py
from plotly.offline import download_plotlyjs, plot

def training_and_test_plot(request,df_train, df_test, crypto_name):
    # creating a plotly graph for training and test set
    trace1 = go.Scatter(
        x = df_train.index,
        y = df_train['Close'],
        customdata = df_train['Name'],
        hovertemplate="<b>%{customdata}</b><br><br>" +
        "Date: %{x|%d %b %Y} <br>" +
        "Closing Price: %{y:$,.2f}<br>"+
        "<extra></extra>",
        name = 'Training Set')

    trace2 = go.Scatter(
        x = df_test.index,
        y = df_test['Close'],
        name = 'Test Set',
        customdata = df_test['Name'],
        hovertemplate="<b>%{customdata}</b><br><br>" +
        "Date: %{x|%d %b %Y} <br>" +
        "Closing Price: %{y:$,.2f}<br>"+
        "<extra></extra>",
        yaxis="y1")

    data = [trace1, trace2]
    fig = go.Figure(data = data)

    fig.update_layout({'title': {'text':'Training and Test Set Plot of {}'.format(str(crypto_name))}},
                      yaxis_tickprefix = '$', yaxis_tickformat = ',.')
    training_and_test_plot = fig.to_html(full_html=False, default_height=1000, default_width=1500)

    return training_and_test_plot
