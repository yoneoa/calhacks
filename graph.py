import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import plotly
import plotly.plotly as py
from plotly import tools
import plotly.graph_objs as go
import json

plotly.tools.set_credentials_file(username='trevorwise16', api_key='EhhKIRbvdFkt3pfcIBP4')

def graph(arrived, left, total):
    fig = tools.make_subplots(rows=1, cols=2)

    g1 = graph1(total)
    g2 = graph2(total)
    g3 = graph3(total)

    fig.append_trace(g1, 1, 1)
    # fig.append_trace(g2, 1, 2)
    fig.append_trace(g3, 1, 2)

    py.plot(fig, filename='basic-line', auto_open=True)
    fig.append_trace(g1, 1, 1)
    #fig.append_trace(g2, 1, 2)
    py.plot(fig, filename="basic-line", auto_open=True)
    plt.show()

'''  
    sentimentDifference = []

    for faceLeft in left:
        first = arrived[faceLeft['faceId']]['emotion']
        for i in range(len(faceLeft['emotion'].keys())):
            dif = faceLeft['emotion'].values()[i] - first[i]

'''
def graph1(total):
    age = [j['faceAttributes']['age'] for j in total.values()]
    # age histogram
    return go.Histogram(x=age)

def graph2(total):
    labels = ['Male', 'Female']
    colors = ['#5064ff', '#E1396C']

    men = 0
    women = 0
    # TODO: MAybe change just to people in the room
    for face in total.values():
        if face['faceAttributes']['gender'] == 'male':
            men += 1
        else:
            women += 1
    values = [men, women]
    return go.Pie(labels=labels, values=values,
                hoverinfo='label+percent', textinfo='value',
                textfont=dict(size=20),
                marker=dict(colors=colors,
                            line=dict(color='#000000', width=2)),
                domain={'x': [0.0, 0.5], 'y': [0.0, 0.5]})

def graph3(total, left):
    timeInClub = [(faceLeft["time"] - total[faceLeft['faceId']]['time']).seconds // 60 for faceLeft in left.values()]
    return go.Histogram(x=timeInClub)

