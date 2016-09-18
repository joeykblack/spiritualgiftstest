'''
Created on Oct 20, 2010

@author: joeykblack
'''

from action.SGRequestHandler import SGRequestHandler

from util import constants

class Restest(SGRequestHandler):
    def get(self):
        
        score=str(3)
        inputs = '<p>'
        for cat in constants.categories:
        #cat = constants.categories[2]
            for gift in constants.gifting[cat]:
                for index in range(1,6):
                    inputs+=cat+"_"+gift+"_"+str(index)+"<input type='text' name='"+cat+"_"+gift+"_"+str(index)+"' value='"+score+"' /><br />"
        
        inputs+="<input type='text' name='firstname' value='Auto' /><br />"
        inputs+="<input type='text' name='lastname' value='Test' /><br />"
        inputs+="<input type='text' name='email' value='autotest"+score+"' /><br />"   
        inputs+='</p>'          
          
        
        super(Restest, self).render('restest', {'inputs':inputs})
