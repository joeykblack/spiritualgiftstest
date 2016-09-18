'''
Created on Oct 21, 2010

@author: joeykblack
'''

from google.appengine.ext import db
from util import constants
from model.user import GiftsUser


class Resultset(db.Model):
    date=db.DateTimeProperty(auto_now_add=1)
    giftsuser=db.ReferenceProperty(GiftsUser, collection_name='resultsets')
    url=db.StringProperty()
    results=db.StringListProperty()
    
    
    def saveResults(self, handler):
        self.results = []
        
        # Add up totals
        # For each category
        for categorie in constants.categories:
            # For each gifting in category
            for gift in constants.gifting[categorie]:
                key = categorie+"_"+gift+"_"
                # For each question in category_gifting
                for index in range(1, 6):
                    # Sum up gifting totals
                    if (handler.request.get(key+str(index))):
                        self.results.append( key+str(index) + ',' + handler.request.get(key+str(index)) )
                    else:
                        self.results.append( key+str(index) + ',' + '0' )
    
    def getResultsDict(self):
        re = {}
        for result in self.results:
            re[result.split(',')[0]] = result.split(',')[1]
        return re
