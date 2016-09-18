'''
Created on Oct 19, 2010

@author: joeykblack
'''

from google.appengine.ext import db

from util import calc, graph, constants, narratives
from model.category import Category
from model.gift import Gift

from model.results import Resultset
from util.utils import getUser, getLang
from model.norms import Norm
from util.constants import fix

from action.SGRequestHandler import SGRequestHandler



class Results(SGRequestHandler):
    
    def get(self):
        reskey = self.request.get('reskey')
        resultset=db.get(reskey)
        
        if not resultset:
            self.error(404)
        else:
            giftsuser=resultset.giftsuser
            calc.totals(resultset.getResultsDict())
            respond(self, giftsuser, resultset)
        
    def post(self):
        
        if self.request.get('newresults'):
            first = self.request.get('firstname')
            last = self.request.get('lastname')
            email = self.request.get('email')
            
            giftsuser = getUser(first, last, email, self)
            
            resultset=Resultset()
            resultset.giftsuser=giftsuser
            resultset.saveResults(self)
            resultset.save()
            resultset.url=self.request.host_url+'/results?reskey='+str(resultset.key())
            resultset.save()
            
            #sendResults(resultset)
        
            calc.totals(self.request)
            addnorms() 
            
            respond(self, giftsuser, resultset)
        elif self.request.get('reskey'):
            reskey = self.request.get('reskey')
            resultset=db.get(reskey)
            giftsuser=resultset.giftsuser
            
            respond(self, giftsuser, resultset)
        else:
            self.error(404)
        
        
        
def respond(handler, giftsuser, resultset):
    
    pdf = handler.request.get('pdf')
    
    date = resultset.date.strftime('%B %d, %Y at %I:%M %p')
    
    pdfurl=resultset.url
    
    name = giftsuser.firstname + ' ' + giftsuser.lastname
    giftsChartUrl = graph.graphGiftings(calc.giftingTotals)
    categoriesChartUrl = graph.graphCategories(calc.categoryTotals)
    categories = buildCat(getLang(handler))
    fname=giftsuser.firstname + '_' + giftsuser.lastname + '_SpiritualGifts.pdf'
    
    params = {'fname':fname, 'pdf':pdf, 'pdfurl':pdfurl, 'name':name, 
              'date':date, 'giftsChartUrl':giftsChartUrl, 'categoriesChartUrl':categoriesChartUrl, 
              'categories':categories, 'reskey':str(resultset.key())} 
    super(Results, handler).render('results', params)
    
        
def buildCat(lang):
    catTotals = []
    for cat in constants.categories:
        catTotals.append(calc.categoryTotals[cat])
    catScores = zip(catTotals, constants.categories)
    catScores.sort(reverse=True)
    
    narratives.loadNarratives(lang)
    
    i = 0
    
    categories = []
    for cats in catScores:
        newcat = None
        newcat = Category()
        newcat.title = cats[1].replace('-', '/').replace('_', ' ').replace('Gods', "God's")
        newcat.titlepre = constants.heading[i]
        i += 1
        newcat.text = narratives.getNarrative(cats[1], calc.giftingTotals[cats[1]])
        newcat.gifts = []
        
        for gift in constants.gifting[cats[1]]:
            newgift = None
            newgift = Gift()
            newgift.title = gift.replace('-', '/').replace('_', ' ').replace('Gods', "God's")
            newgift.definition = constants.definitions[gift][1]
            newgift.url = graph.giftGraph(calc.giftingTotals[cats[1]][gift])
            newcat.gifts.append(newgift)
        
        categories.append(newcat)
        
    return categories



def addnorms():
    for cat in constants.categories:
        norm=db.GqlQuery('SELECT * FROM Norm where  title=:1', fix(cat)).get()
        if not norm:
            norm=Norm()
            norm.init(fix(cat))
        norm.update(calc.categoryTotals[cat])
        norm.save()
        for gift in constants.gifting[cat]:
            norm=db.GqlQuery('SELECT * FROM Norm where  title=:1', fix(gift)).get()
            if not norm:
                norm=Norm()
                norm.init(fix(gift))
            norm.update(calc.giftingTotals[cat][gift])
            norm.save()
        
        
        

