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

# creating graph for Close Percentage Change
def hist_box_pct_change(request, y, crypto_name):
    fig = make_subplots(rows=2, cols=1,
                        subplot_titles=['Histogram of {} 1-Day Close Percentage Change'.format(crypto_name),
                                        'Box plot of {} 1-Day Close Percentage Change'.format(crypto_name)],
                        x_title = '1-Day Close Percentage Change')
    # 1.Histogram
    fig.add_trace(go.Histogram(x = y['Close Percentage Change'], name = 'Histogram', nbinsx = round(len(y) / 20),
                               ), row=1, col=1)

    #2. Boxplot
    fig.add_trace(go.Box(x = y['Close Percentage Change'], name = 'Boxplot',
                         customdata = y['Name'],
                         hovertemplate="<b>%{customdata}</b><br><br>" +
                                            "1-Day Percentage Change: %{x:.0%}<br>"+
                                    "<extra></extra>"
                    ), row=2, col=1)

    fig.update_layout(title = 'Plots of 1-Day Close Percentage Change for {}'.format(crypto_name))
    fig['layout']['yaxis1']['title'] = '# of Observations'
    fig.update_xaxes(tickformat = '.0%', row = 1, col = 1)
    fig.update_xaxes(tickformat = '.0%', row = 2, col = 1)

    hist_box_pct_change = fig.to_html(full_html=False, default_height=1000, default_width=1500)

    return hist_box_pct_change
