# -*- coding: utf-8 -*-
"""
Created on Tue May 16 13:00:22 2017

@author: fly
"""


import numpy as np
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_absolute_error
from model.
import sys


def mean_abs_error(self,y_true, y_pred) :
    return mean_absolute_error(y_true, y_pred)

def computeTolerance(actual,predicted) :
    return actual- predicted
    
def process(model,dataLoader,dump,startIndex) :
    toleranceList ={}
    for n in range(startIndex,dataLoader.size()-1):
        
        trainX,trainY = dataLoader.skipLastNXY(n ,[2,3,4,6])
        model.trainModel(trainX,trainY)
        x,y = dataLoader.getDataAtIndex(n-1)
        predictedY = model.predict(X)
        tolerance = ModelUtil.computeTolerance(y,predictedY)
        toleranceList.append((y,predictedY,tolerance))
    
    with open ('/'.join(dump,dataLoader.gteUri().split('/')[-1]),'w') as fr :
        fr.write(toleranceList)
