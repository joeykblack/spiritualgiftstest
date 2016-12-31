'''
Created on Oct 20, 2010

@author: joeykblack
'''

from action.SGRequestHandler import SGRequestHandler

from util import constants
from util.utils import buildQuestionKey

class Restest(SGRequestHandler):
    def get(self):
        
        score=str(3)
        inputs = '<p>'
        for cat in constants.categories:
        #cat = constants.categories[2]
            for gift in constants.gifting[cat]:
                for index in range(1,6):
                    key = buildQuestionKey(cat, gift, index)
                    inputs+=key+"<input type='text' name='"+key+"' value='"+score+"' /><br />"
        
        inputs+="<input type='text' name='firstname' value='Auto' /><br />"
        inputs+="<input type='text' name='lastname' value='Test' /><br />"
        inputs+="<input type='text' name='email' value='autotest"+score+"' /><br />"   
        inputs+='</p>'          
          
        
        super(Restest, self).render('restest', {'inputs':inputs})
