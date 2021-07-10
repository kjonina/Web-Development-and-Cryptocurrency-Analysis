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

# the graph needs formatting
def create_first_graph(request):
    fig = make_subplots(rows=2, cols=1, shared_xaxes=True)
    # Lineplots of price and moving averages
    fig.add_trace(go.Scatter(
                            x = df.index,
                            y = df['Close'],
                            mode='lines',
                            line = dict(color="black")), row = 1, col = 1)
    fig.add_trace(go.Scatter(x = df.index,
                             y = df['short_SMA'],
                             name = 'Short SMA',
                             mode = 'lines',
                             line = dict(color="red")), row = 1, col = 1)
    fig.add_trace(go.Scatter(x = df.index,
                             y = df['long_SMA'],
                             name = 'Long SMA',
                             mode = 'lines',
                             line = dict(color="green")), row = 1, col = 1)
    # Barplot of volume
    fig.add_trace(go.Bar(x = df.index,
                    y = df['Volume'],
                    name = 'Volume',
                    marker = dict(color="black", opacity = True)), row = 2, col = 1)
    #fig show
    fig.show()
