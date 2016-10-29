'''
Created on Oct 19, 2010

@author: joeykblack
'''

from action.SGRequestHandler import SGRequestHandler
from util.utils import getUserByEmail, buildQuestionKey
from util import constants
from random import shuffle

class Test(SGRequestHandler):
        
        
    def post(self):
        
        if getUserByEmail(self.request.get("email")):
            msg="You have already taken the Spiritual Gifts test.<br />You may only take the test once per email.<br /><a href='/'>Home</a>"
            super(Test, self).render('error', {'msg':msg})
        else:
            userinfo="<input type='hidden' name='firstname' value='"+self.request.get("firstname")+"' />"
            userinfo+="<input type='hidden' name='lastname' value='"+self.request.get("lastname")+"' />"
            userinfo+="<input type='hidden' name='email' value='"+self.request.get("email")+"' />"   
            userinfo+="<input type='hidden' name='gender' value='"+self.request.get("gender")+"' />"
            userinfo+="<input type='hidden' name='age' value='"+self.request.get("age")+"' />"
            userinfo+="<input type='hidden' name='interest' value='"+self.request.get("interest")+"' />"
            userinfo+="<input type='hidden' name='state' value='"+self.request.get("state")+"' />"
            userinfo+="<input type='hidden' name='country' value='"+self.request.get("country")+"' />"
               
            questions = [buildQuestionKey(category, gift, i) for category in constants.categories for gift in constants.gifting[category] for i in range(1,6)]
            shuffle(questions)
               
            super(Test, self).render('test', {'userinfo':userinfo, 'questions':questions})
        