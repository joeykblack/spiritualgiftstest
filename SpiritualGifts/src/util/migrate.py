'''
Created on Dec 3, 2016

@author: joey
'''

def addOne(resultset):
    d = resultset.getResultsDict()
    resultset.results = [] #clear
    for res in d.items():
        resultset.results.append(res[0]+','+str(int(res[1])+1))
    return resultset

def updateKeys(resultset):
    d = resultset.getResultsDict()
    resultset.results = [] #clear
    for res in d.items():
        key = res[0].replace("-", "_")
        resultset.results.append(key+','+str(int(res[1])))
    return resultset