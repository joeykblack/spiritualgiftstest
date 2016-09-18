'''
Created on Oct 21, 2010

@author: joeykblack
'''

from google.appengine.ext import db


class GiftsUser(db.Model):
    firstname=db.StringProperty()
    lastname=db.StringProperty()
    email=db.StringProperty()
    gender=db.StringProperty()
    age=db.StringProperty()
    interest=db.StringProperty()
    state=db.StringProperty()
    country=db.StringProperty()
    
