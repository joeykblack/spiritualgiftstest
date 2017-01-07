'''
Created on Feb 13, 2010

@author: joeykblack
'''

from model.results import Resultset
from action.SGRequestHandler import SGRequestHandler
from util import migrate

class ModResults(SGRequestHandler):
    def get(self):
        allresultsets=Resultset().all()
        for resultset in allresultsets:
            if resultset.version < 2:
                resultset = migrate.addOne(resultset)
                resultset = migrate.updateKeys(resultset)
                resultset.url = ''
                resultset.version = 2
                resultset.save()
        self.response.out.write('done')

