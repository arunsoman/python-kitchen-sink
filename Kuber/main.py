# -*- coding: utf-8 -*-
from  source.NSE import  downloadHistory
from talib.Enrich import enrich
from model.Svm import SvmModel
from model.DataLoader import DataLoader
from model.ModelUtil import process
import ConfigReader


config = ConfigReader.readConfigFile('config.ini')

inputUri = downloadHistory(config['NSE_DATA']['dumpPath'])

enrichUri=enrich(inputUri)

for uri in enrichUri :
    
    svmModel = SvmModel()
    dataLoader = DataLoader(uri)
    process(svmModel,dataLoader,100)
   
   
   
