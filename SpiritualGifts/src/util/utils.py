'''
Created on Oct 27, 2010

@author: joeykblack
'''

from model.user import GiftsUser
from google.appengine.ext import db
from util.fragments import langSelector, langHidden, banner
from util.session import loadloginout


def getUser(first, last, email, handler):
    user=db.GqlQuery('SELECT * FROM GiftsUser where firstname=:1 and lastname=:2 and email=:3', first, last, email).get()
    if not user:
        user = GiftsUser()
        user.firstname = first
        user.lastname = last
        user.email = email
        user.gender=handler.request.get('gender')
        user.age=handler.request.get('age')
        user.interest=handler.request.get('interest')
        user.state=handler.request.get('state')
        user.country=handler.request.get('country')
        user.save()
    return user


def getUserByEmail(email):
    user=db.GqlQuery('SELECT * FROM GiftsUser where  email=:1', email).get()
    return user


def getLang(handler):
    lang = handler.request.get('lang')
    if lang==None or lang=='':
        lang = 'English'
    return lang

def getStdDict(handler, template_dict = {}):
    lang = getLang(handler)
    template_dict.update({'lang':lang,
                          'langselect':langSelector(handler, lang, template_dict), 
                          'langhidden':langHidden(lang), 
                          'loginout':loadloginout(handler),
                          'banner':banner()})
    return template_dict


def getPage(handler, page):
    return "html/%s.html" % page


def buildQuestionKey(category, gift, index):
    return category + "_" + gift + "_" + str(index)
