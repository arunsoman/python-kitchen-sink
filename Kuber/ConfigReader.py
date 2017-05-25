# -*- coding: utf-8 -*-
"""
Created on Tue May 16 12:13:40 2017

@author: fly
"""

import configparser

def readConfigFile(fileName):
    config = configparser.ConfigParser()
    config.sections()
    config.read(fileName)
    return config
    
