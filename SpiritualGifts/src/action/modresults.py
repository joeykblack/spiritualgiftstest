'''
Created on Feb 13, 2010

@author: joeykblack
'''

from model.results import Resultset
from action.SGRequestHandler import SGRequestHandler

class ModResults(SGRequestHandler):
    def get(self):
        super(ModResults, self).render('modresults')
        
    def post(self):
#        table=self.request.get('command')
        
#        if table=='downone':
#            self.downone()
            
        self.response.out.write('disabled')
        
    def downone(self):
        # for each set of results in the database
        allresultsets=Resultset().all()
        for resultset in allresultsets:
            d = resultset.getResultsDict()
            resultset.results = [] #clear
            for res in d.items():
                resultset.results.append(res[0]+','+str(int(res[1])-1))
            resultset.save()
