# -*- coding: utf-8 -*-
"""
Created on Tue May 16 11:35:36 2017
 
@author: fly
"""

import csv
import configparser

# Read the configuration file and return the configuration data as list data 
def readConfigurations(fileName):    
    rows = []
    with open(fileName, "rb") as f_obj:         
        next(f_obj, None) # SKIP header 
        reader = csv.reader(f_obj)
        for row in reader:
            if(len (row)<5):
                raise ValueError('Wrong Input Configuration')
            else :
                rows.append(row)               
    return  rows

def getConfigPath():
    return 'inputconfig.csv'


def loadNSEData() :
    stocks = readConfigurations(getConfigPath())
    return list(filter(lambda x: x[0] == 'NSE',stocks))
