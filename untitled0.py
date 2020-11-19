print("Task_1")
import pandas as pd 
data=pd.read_csv("file_example_XLS_10.xls") 
data.sort_values(["ID"], axis=1, 
				ascending=True, inplace=True) 
data 


import numpy as np
import math

csv= np.genfromtxt
csv = np.genfromtxt('file_example_XLS_10.xls',delimiter=",")
N=len(csv[:])

X = np.mean(csv,axis=0)
sum = 0

for j in range(len (X[:])):
    for i in range(N):
        val= csv[i,j]-X[j]
        squre = val**2
        sum= sum+squre
    final = math.sqrt(sum/(N-1))
    print (final)