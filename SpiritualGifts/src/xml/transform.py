'''
Created on Feb 25, 2016

@author: joey
'''
from __future__ import print_function

def doReplace(targetFileName, findFileName, replaceFileName):
    data=''
    with open(targetFileName, 'r') as targetFile, open(findFileName) as findFile, open(replaceFileName) as replaceFile:
        data=targetFile.read()
        for f,r in zip(findFile, replaceFile):
            data = data.replace(f.strip(), r.strip())
            
    with open(targetFileName, 'w') as targetFile:
        print(data, file=targetFile)
        
        


if __name__ == '__main__':
    doReplace('test-lg.xml', 'en.txt', 'lg.txt')