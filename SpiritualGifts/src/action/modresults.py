'''
Created on Feb 13, 2010

@author: joeykblack
'''

from model.results import Resultset
from action.SGRequestHandler import SGRequestHandler
from util import migrate

class ModResults(SGRequestHandler):
    def get(self):
        super(ModResults, self).render('modresults')
        
    def post(self):
        table=self.request.get('command')
        
        if table=='migrate':
            allresultsets=Resultset().all()
            for resultset in allresultsets:
                resultset = migrate.addOne(resultset)
                resultset = migrate.updateKeys(resultset)
                resultset.save()
            self.response.out.write('done')
        else:
            self.response.out.write('not supported')

