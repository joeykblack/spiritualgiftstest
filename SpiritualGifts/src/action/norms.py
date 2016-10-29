'''
Created on Nov 2, 2010

@author: joeykblack
'''

import model
from model.results import Resultset
from util import calc, constants
from action.SGRequestHandler import SGRequestHandler

class Norms(SGRequestHandler):
    def get(self):
        norms=model.norms.Norm.all().fetch(500)
        super(Norms, self).render('norms', {'norms':norms})
        #self.response.out.write(template.render('html/norms.html', {}))
        
    # recalculate all
    def post(self):
        norms=model.norms.Norm.all()
        norms=norms.fetch(500)
        for norm in norms:
            norm.delete()
        norms=[]
        scoresets={}
        for cat in constants.categories:
            scoresets[cat]=[]
            for gift in constants.gifting[cat]:
                scoresets[gift]=[]
        
        # for each set of results in the database
        allresultsets=Resultset().all()
        for resultset in allresultsets:
            re = resultset.getResultsDict()
            # calculate the results
            giftingTotals = calc.totals(re)
            # for each category, append the score for this set
            for cat in constants.categories:
                scoresets[cat].append(calc.categoryTotals[cat])
                # for each gifting, append the score for this set
                for gift in constants.gifting[cat]:
                    s=giftingTotals[cat][gift]
                    scoresets[gift].append(s)

                
        # for each category, calculate norm with score set
        for cat in constants.categories:
            name=cat
            norm=model.norms.Norm()
            norm.init(name)
            norm.recalc(scoresets[cat])
            norm.save()
            norms.append(norm)
            # for each gifting, calculate norm with score set
            for gift in constants.gifting[cat]:
                name=gift
                norm=model.norms.Norm()
                norm.init(name)
                norm.recalc(scoresets[gift])
                norm.save()
                norms.append(norm)
            
        super(Norms, self).render('norms', {'norms':norms})
        