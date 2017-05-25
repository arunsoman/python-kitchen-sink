# -*- coding: utf-8 -*-
"""
Created on Tue May 16 13:41:30 2017

@author: fly
"""

class DataLoader(object): 
    '''
    classdocs
    '''


    def __init__(self, uri):
        '''
        Constructor
        '''
        self.uri=uri
        self.scaler = MinMaxScaler(feature_range=(0, 1))
        self.transform = self.scaler.fit_transform
        self.inversetransform =self.scaler.inverse_transform        
        dataSet =  np.genfromtxt(self.uri, delimiter=",", skip_header=True)
        if(dataSet.ndim) :
            self.dataSet = dataSet[:, 0:dataSet.shape[1]] 
       
            
    def transform(self,data):
        return self.transform(data)
    
    def inverseTransform(self,data):
        return self.inversetransform(data)
       
    def skipLastNXY(self,index,YindexArry):        
        datasubset = self.dataSet[:len(self.dataSet)-index]
        yvalue = datasubset[:, YindexArry]     
        return np.delete(self.dataSet.copy(), (-1), axis=0), np.delete(yvalue.copy(), (0), axis=0)
    
    def getDataAtIndex(self,index):
        return dataSet[len(self.dataSet)-index:]
    
    def getLastRecord(self,ndArray) :
        return ndArray[len(ndArray)-1:]
    
    def reshape(self,ndArry):
        return ndArry.reshape(1,-1)
    
    def size(self):
        return len(self.dataSet)
        
    def gteUri(self) :
        return self.uri