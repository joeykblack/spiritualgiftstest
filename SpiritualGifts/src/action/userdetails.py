'''
Created on Oct 21, 2010

@author: joey
'''

from model.user import GiftsUser

from action.SGRequestHandler import SGRequestHandler

class Userdetails(SGRequestHandler):
    def get(self):
        userkey=self.request.get('userkey')
        giftsuser=GiftsUser().get(userkey)
        super(Userdetails, self).render('userdetails', {'giftsuser':giftsuser})
