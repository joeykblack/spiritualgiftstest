'''
Created on Nov 2, 2010

@author: joeykblack
'''

from google.appengine.ext import db
from util import constants, graph
import math


class Norm(db.Model):
    title=db.StringProperty()
    average=db.FloatProperty()
    sdev=db.FloatProperty()
    low=db.FloatProperty()
    high=db.FloatProperty()
    sum=db.FloatProperty()
    sumsq=db.FloatProperty()
    numscores=db.IntegerProperty()
    scorelist=db.ListProperty(int)
    graphurl=db.StringProperty()
    type=db.StringProperty()
    
    def init(self, name):
        self.title=name
        self.sum=0.0
        self.sumsq=0.0
        self.numscores=0
        self.scorelist=[]
        self.settype()
    
    def settype(self):
        if self.title in constants.categories:
            self.type='cat'
        else:
            self.type='gift'
    
    def sums(self):
        self.numscores=len(self.scorelist)
        self.sum=0.0
        for score in self.scorelist:
            self.sum += score
        self.ave() #must take ave for for sumsq
        self.sumsq=0.0
        for score in self.scorelist:
            self.sumsq += math.pow(score-self.average, 2)
            
    def ave(self):
        if self.numscores>0:
            self.average = self.sum / self.numscores
        else:
            self.average=0.0
        

    def dev(self):
        #std dev
        if self.numscores>1:
            self.sdev = math.sqrt( self.sumsq / (self.numscores-1) )
        else:
            self.sdev = 0.0
        self.low = self.average - self.sdev
        self.high = self.average + self.sdev
            
    
    def graph(self):
        self.graphurl=graph.normGraph(self)
    
            
        
    def recalc(self, scores):
        self.scorelist=scores
        self.sums()
        self.dev()
        self.graph()
        
    def update(self, newscore):
        self.scorelist.append(newscore)
        self.sums()
        self.dev()
        self.graph()
        