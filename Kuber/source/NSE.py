# -*- coding: utf-8 -*-import 
"""
Created on Tue May 16 11:30:26 2017

@author: fly
"""
import FileLoader
from datetime import date,  timedelta
from nsepy import get_history
from os.path import dirname, abspath, exists
from os import makedirs

def getFileName(stock):
    return '_'.join([stock[0],stock[4]])   
    
def writeToFile(fileName,dataFrame,mode):

    if not exists(fileName):
        makedirs(dirname(abspath(fileName)))
    if mode =='a' :
        with open(fileName, mode) as f:
            dataFrame.to_csv(f, sep=',',encoding='utf-8',header=False)    
    else :
        dataFrame.to_csv(fileName,sep=',', encoding='utf-8')
   


def download(stockName,dumpPath,fromDate,toDate,mode) :
    print("Start Fetching data from NSE...")
    try:      
      
        dataframe = get_history(symbol=stockName,start=fromDate,end=toDate)
        dataframe.drop('Symbol', axis=1, inplace=True)
        dataframe.drop('Series', axis=1, inplace=True)
        writeToFile(dumpPath,dataframe,mode)
    except :
        print ("Error while downloading data")



def downloadHistory(dump):
    listUri =[]
    endDate = date.today() - timedelta(days=1) 
    for stock in FileLoader.loadNSEData() :
        uri =  "/".join([dump,getFileName(stock)])
        listUri.append(uri)
        stockName =  stock[1]
        startDate =  endDate - timedelta(days=int(stock[3]))
        download(stockName,uri,startDate,endDate,'w')
    return listUri
    
  

def downloadWindow(dump,window):
    listUri ={}
    endDate = window.end
    for stock in FileLoader.loadNSEData() : 
        uri =  "/".join(dump,getFileName(stock))
        listUri.append(uri)
        stockName =  stock[1]
        startDate =  window.start
        download(stockName,uri,startDate,endDate,'a')
    return listUri
        
