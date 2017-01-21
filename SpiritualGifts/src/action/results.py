'''
Created on Oct 19, 2010

@author: joeykblack
'''

from google.appengine.ext import db

from util import calc, graph, constants, narratives
from model.category import Category
from model.gift import Gift

from model.results import Resultset
from util.utils import getUser
from model.norms import Norm

from action.SGRequestHandler import SGRequestHandler



class Results(SGRequestHandler):
    
    def get(self):
        if self.request.get('reskey'):
            reskey = self.request.get('reskey')
            resultset=db.get(reskey)
            
            if not resultset:
                self.error(404)
            else:
                giftsuser=resultset.giftsuser
                giftingTotals = calc.totals(resultset.getResultsDict())
                categoryTotals = calc.categoryTotals(giftingTotals)
                respond(self, giftsuser, resultset, categoryTotals, giftingTotals)
        else:
            self.error(400)
        
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
            
            giftingTotals = calc.totals(self.request)
            categoryTotals = calc.categoryTotals(giftingTotals)
            addnorms(categoryTotals, giftingTotals) 
            
            respond(self, giftsuser, resultset, categoryTotals, giftingTotals)
        elif self.request.get('reskey'):
            self.get()
        else:
            self.error(403)
        
        
        
def respond(handler, giftsuser, resultset, categoryTotals, giftingTotals):
    
    pdf = handler.request.get('pdf')
    
    date = resultset.date.strftime('%B %d, %Y at %I:%M %p')
    
    pdfurl=handler.request.host_url+'/results?reskey='+str(resultset.key())
    
    name = giftsuser.firstname + ' ' + giftsuser.lastname
    giftsChartUrl = graph.graphGiftings(giftingTotals)
    categoriesChartUrl = graph.graphCategories(categoryTotals)
    categories = buildCat(categoryTotals, giftingTotals)
    fname=giftsuser.firstname + '_' + giftsuser.lastname + '_SpiritualGifts.pdf'
    
    params = {'fname':fname, 'pdf':pdf, 'pdfurl':pdfurl, 'name':name, 
              'date':date, 'giftsChartUrl':giftsChartUrl, 'categoriesChartUrl':categoriesChartUrl, 
              'categories':categories, 'reskey':str(resultset.key())} 
    super(Results, handler).render('results', params)
    
    
        
def buildCat(categoryTotals, giftingTotals):
    catTotals = []
    for cat in constants.categories:
        catTotals.append(categoryTotals[cat])
    catScores = zip(catTotals, constants.categories)
    catScores.sort(reverse=True)
    
    i = 1
    
    categories = []
    for cats in catScores:
        newcat = None
        newcat = Category()
        newcat.title = '$'+cats[1]+'_category'
        newcat.titlepre = '$gifting_title_' + str(i)
        i += 1
        newcat.text = narratives.getNarrative(cats[1], giftingTotals[cats[1]])
        newcat.gifts = []
        
        for gift in constants.gifting[cats[1]]:
            newgift = None
            newgift = Gift()
            newgift.title = '$' + gift + '_gifting'
            newgift.definition = '$' + gift + '_definition'
            newgift.url = graph.giftGraph(giftingTotals[cats[1]][gift])
            newcat.gifts.append(newgift)
        
        categories.append(newcat)
        
    return categories



def addnorms(categoryTotals, giftingTotals):
    for cat in constants.categories:
        norm=db.GqlQuery('SELECT * FROM Norm where  title=:1', cat).get()
        if not norm:
            norm=Norm()
            norm.init(cat)
        norm.update(categoryTotals[cat])
        norm.save()
        for gift in constants.gifting[cat]:
            norm=db.GqlQuery('SELECT * FROM Norm where  title=:1', gift).get()
            if not norm:
                norm=Norm()
                norm.init(gift)
            norm.update(giftingTotals[cat][gift])
            norm.save()
        
        
        

