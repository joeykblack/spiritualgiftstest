'''
Created on Sep 18, 2016

@author: joey
'''

from ConfigParser import ConfigParser
import io

def loadLanguage(language):
    config = ConfigParser()
    
    with open("text/%s.txt" % language) as f:
        config.readfp(io.BytesIO( '[text]\n' + f.read() ))
    
    text = dict()
    
    for k, v in config.items('text'):
        text[k] = v 
        
    return text