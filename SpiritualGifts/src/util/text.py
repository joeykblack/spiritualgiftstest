'''
Created on Sep 18, 2016

@author: joey
'''

from ConfigParser import ConfigParser
import io

langCache = {}

class CaseInsensitiveDict(dict):
    def __setitem__(self, key, value):
        super(CaseInsensitiveDict, self).__setitem__(key.lower(), value)

    def __getitem__(self, key):
        return super(CaseInsensitiveDict, self).__getitem__(key.lower())

def loadLanguage(language):
    if language not in langCache:
        config = ConfigParser()
        # config.optionxform = str # do not convert keys to lower case
        
        with open("text/%s.txt" % language) as f:
            config.readfp(io.BytesIO( '[text]\n' + f.read() ))
        
        text = CaseInsensitiveDict()
        
        for k, v in config.items('text'):
            text[k] = v
            
        langCache[language] = text
            
    return langCache[language]

        