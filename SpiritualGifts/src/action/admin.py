'''
Created on Oct 21, 2010

@author: joeykblack
'''

from model.user import GiftsUser
from action.SGRequestHandler import SGRequestHandler

class Admin(SGRequestHandler):
    def get(self):
        giftsusers=GiftsUser().all()
        super(Admin, self).render('admin', {'giftsusers':giftsusers})
        
    def post(self):
        firstname=self.request.get('firstname')
        lastname=self.request.get('lastname')
        email=self.request.get('email')
        
        q=GiftsUser().all()
        if firstname:
            q.filter('firstname =', firstname)
        if lastname:
            q.filter('lastname =', lastname)
        if email:
            q.filter('email =', email)
        giftsusers=q.fetch(100)
        
        super(Admin, self).render('admin', {'giftsusers':giftsusers})
        
        
class Retake(SGRequestHandler):
    def get(self):
        userkey=self.request.get('userkey')
        user=GiftsUser.get(userkey)
        if user:
            for test in user.resultsets:
                test.delete()
            user.delete()
        
        giftsusers=GiftsUser().all()
        super(Retake, self).render('admin', {'giftsusers':giftsusers})
        