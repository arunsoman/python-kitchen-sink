# -*- coding: utf-8 -*-
"""
Created on Tue May 16 12:58:13 2017

@author: fly
"""

from sklearn.multioutput import MultiOutputRegressor
from sklearn.ensemble import GradientBoostingRegressor


class SvmModel (object): 

    def __init__(self) :
        # Build Model
        self.model = MultiOutputRegressor(GradientBoostingRegressor(random_state=0))
        
    #Train model
    def trainModel(self,trainX,trainY):        
        self.model = self.model.fit(trainX, trainY)
   
    #Predict 
    def predict(self,testX):        
        result = self.model.predict(testX)
        return result
    
 