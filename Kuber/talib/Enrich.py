# -*- coding: utf-8 -*-
"""
Created on Tue May 16 12:22:23 2017

@author: fly
"""

def enrich(listUri,config) :
    listUri ={}
    for uri in listUri :
        listUri.append(processFile(uri,config))
    return listUri

def enrichTalibValues(inputDict, features, result) :
    headers=''
    for aType in features:
        for func in talib.get_function_groups()[aType]:
            pf = abstract.Function(func)
            try:
                pf.input_arrays = inputDict
                pf.run()
                outputs = pf.outputs
                if isinstance(outputs, list):
                    for anItem , name in zip(outputs, pf.output_names):
                        result = numpy.hstack((result, anItem.reshape(anItem.size,1)))
                        headers = ','.join([headers, name])
                else:
                    result = numpy.hstack((result, outputs.reshape(outputs.size,1)))
                    headers = ','.join([headers,func])
            except:
                sys.exc_info()[0]                
               
    return result, headers

def stripData(df,config):
     
    if bool(config['TA LIB CONFIG']['REMOVE_ALL_NaN_COLUMNS']) :
        df = df.dropna(axis=1,how="all")
    
    if bool(config['TA LIB CONFIG']['REMOVE_ANY_NaN_ROWS']) :
        df = df.dropna(axis=0)
        
    if bool(config['TA LIB CONFIG']['REMOVE_SAME_VALUE']):
        df = df.drop(df.std()[(df.std() == 0)].index, axis=1)
        
    return df  
 

def parseDate(df):
    dates_list = [parse(dateValue) for dateValue in df['Date']]   
    datesvale = [time.mktime(dateValue.timetuple()) for dateValue in dates_list]
    df['Date'] = datesvale
    return df;    

def writeResult(inFilePath,outFileName ,headers,data,config):
    df = pandas.read_csv(inFilePath)
    count =0 
    for key in headers.split(',') :
        if key != '' :
            new_column = pandas.DataFrame({key: data[count]})
            df = df.merge(new_column, left_index = True, right_index = True)
        count = count +1 
    #df = df.fillna('nan')
    
    df =stripData(df,config)    
    df = parseDate(df)    
    df = df.to_csv(outFileName,index=False, sep=',', encoding='utf-8')
    #writeNormalizeFile(outFileName)
    return outFileName


def processFile(fileName,config ):    
    try :
        if os.path.isfile(fileName) :
           
            sample_data = numpy.genfromtxt(fileName, delimiter=",", skip_header=True)
            sample_data = numpy.column_stack(sample_data)
            openValue = sample_data[int( config['TA LIB CONFIG']['open'])].astype(float)
            high = sample_data[int( config['TA LIB CONFIG']['high'])].astype(float)
            low = sample_data[int( config['TA LIB CONFIG']['low'])].astype(float)
            close = sample_data[int( config['TA LIB CONFIG']['close'])].astype(float)
            volume = sample_data[ int( config['TA LIB CONFIG']['volume'])].astype(float)
            result = numpy.empty(shape=(openValue.shape[0],1),dtype=float)            
            inputDict = {'high':high,'close':close,'open':openValue,
                         'low':low,'volume':volume,'timeperiod':3}
            features = config['TA LIB CONFIG']['features'].split(',')
            result, headers = enrichTalibValues(inputDict, features, result)     
            result = numpy.column_stack(result)
            
            talibOutPath = config['TA LIB CONFIG']['OUT_PATH']
            outpath = "/".join(talibOutPath,talibOutPathfileName.split('/')[-1])            
            return writeResult(fileName,outpath,headers,result,config)
                
        else :
            #raise ValueError('File Not Found {0}'.format(fileName))
            print ('File Not Found {0}'.format(fileName))
    except :
            errorPath = '{0}/{1}.csv'.format(config.getErrorPath(),fileName)
            rename(dataFilePath,errorPath)
            print ("Error while TA LIB Process ,File Name ", fileName)
            #raise ValueError('Invalid File {0}'.format(fileName))


    