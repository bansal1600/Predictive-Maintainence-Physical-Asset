#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  6 14:12:03 2020

@author: gauravbansal1600
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from utility import cal_amplitude, top_five_freq, plotlabels

import os

def reshapelist(lst):
    return (list(map(list, zip(*lst))))

try:
    # user input for the path of the dataset
    filedir = "/Users/gauravbansal1600/Desktop/StatsLearningUdemy/IMS/"
    folder_name = input("enter the folder name:- ")
    file_ext = "/"
    filepath = folder_name+file_ext
    basedir = filedir+filepath 
    all_files = os.listdir(basedir)

    freq_max1,freq_max2,freq_max3,freq_max4,freq_max5 = top_five_freq(all_files,basedir)

except IOError:
    print("Warning! Please cheeck the file directory path")

freq = [freq_max1,freq_max2,freq_max3,freq_max4,freq_max5]

#max_type = input("enter the max type in range 1-5:- ")
a = [1,2,3,4,5]
for i in a:
    max_type=int(i)
    if(max_type >= 1 and max_type <= 5):
        freqmax = reshapelist(freq[max_type-1])
    else:
        print("you have enter the max type range except 1-5.")
    
    # plot the figure
    fig  =  plt.figure()
    plotlabels(freqmax)
    fig.suptitle(("freq_max"+str(max_type )+'vs time '), fontsize = 20)
    plt.ylabel('frequency_'+ str(i), fontsize = 15)
    plt.xlabel('time', fontsize = 15)
    fig.savefig((folder_name + "_" + "freq_" +str(max_type)+'.jpg'), dpi = 1024, quality = 95)    