
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  6 00:07:34 2020

@author: gauravbansal1600
"""

import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import numpy.fft
import os

#importing test data set 1
basedir = "/Users/gauravbansal1600/Desktop/StatsLearningUdemy/IMS/1st_test/"
file_path =  "2003.11.25.23.39.56"
data = pd.read_csv(basedir+file_path, sep='\t', header=None)
data.head(5)

#giving name to column
data.columns = ['b1_x', 'b1_y', 'b2_x', 'b2_y', 'b3_x', 'b3_y', 'b4_x', 'b4_y']
data.head()

#ploting the vibration signal for bearring one across accelerometer b1_X
data['b1_x'].plot.line()

#Each plot represents a one second snapshot in the life of that bearing. 
#To perform an analysis of the data, I need to consider all of the snapshots together. 
#Obviously, looking at every plot isn’t going to work

#Feature Extraction
#On the plus side, feature extraction aims to reduce the amount of data you have to process, 
#by drawing signal out of noise

import plotly.graph_objs as go
import chart_studio.plotly as py
from plotly.offline import plot
b1_x_fft  = np.fft.fft(data['b1_x'])
#DISCARDING THE COMPLEX CONJUGATE 
amplitude = np.absolute(b1_x_fft[0:len((b1_x_fft)/2)+1])
frequency = numpy.linspace(0,10000, len(amplitude))

#plotting in frequency Domain
layout = go.Layout(title="Frequency vs Amplitude after FFT",
                  xaxis=dict(title='Frequency', range=[0,11000]),
                  yaxis=dict(title='Amplitude', range=[0,700]))

fig = go.Figure(layout=layout)
fig.add_trace(go.Scatter(x=frequency, y=amplitude,
                    mode='lines',
                    name='lines'))
fig.show()

# analyzing with top 5 vibration 
top_Vibration = sorted(zip(amplitude, frequency), reverse=True)[:5]
df = pd.DataFrame.from_records(top_Vibration)
df.columns = ['Amplitude', 'Frequency']

df = df.transpose()
df.columns = [i+1 for i in range(5)]
df
