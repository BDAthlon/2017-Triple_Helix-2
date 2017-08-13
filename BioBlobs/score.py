import random
import os
import matplotlib.pyplot as plt
import numpy as np
import csv
from numpy import genfromtxt
import pandas as pd

def scoretest():
    hit_blobs, nothit_blobs = ([(5),(10)], [(10,15,20,25,30,35,40,45,50),(2,20,30,40,56,4,87,31,52)])
    return hit_blobs, nothit_blobs

def playgametest(param1, param2):
    x = [(1,10,20,30,40,50),(2,3,4,20,40,43),(2,6,8,0,7,0)]
    return x

def score():
    df_blobs=pd.read_csv('blobvalues.csv', sep=',',header=None)
    #print df_blobs.values

    df_sim =pd.read_csv('simvalues.csv', sep=',',header=None)
    #print df_sim.values

    right_timings_1 = [sublist[0] for sublist in df_blobs.values - 1]
    #right_timings  - 1 so indexes

    diff_simblob = []
    count = 0
    for timing in right_timings_1:
        diff_simblob.append(100.0*abs(df_sim.values[timing][2] - df_blobs.values[count][1])/(df_blobs.values[count][1]))
        count = count + 1
        #print diff_simblob

    scoring = []#1*[None]
    for difference in diff_simblob:
        scoring.append(difference < 5)
    #print scoring

    #get coordinates of blob that was hit
    count = 0
    hit_blobs = []
    nothit_blobs = []
    for correct in scoring:
        if correct:
            hit_blobs.append([df_blobs[0][count],df_blobs[1][count]])
        else:
            nothit_blobs.append([df_blobs[0][count],df_blobs[1][count]])
        count = count + 1
    #print hit_blobs
    hit_blobs = zip(*hit_blobs)
    nothit_blobs = zip(*nothit_blobs)
    return hit_blobs,nothit_blobs

#run the function
#score()
#print score()




