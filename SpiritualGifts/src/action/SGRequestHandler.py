'''
Created on Oct 7, 2015

@author: joey
'''
from google.appengine.ext import webapp
from google.appengine.ext.webapp import template
from util.utils import getPage, getStdDict, getLang
from string import Template
from util.text import loadLanguage

class SGRequestHandler(webapp.RequestHandler):
    
    def render(self, page, template_dict = {}):
        # Render with Google's template engine
        rawText = getPage(self, page)
        dataDict = getStdDict(self, template_dict)
        googleTemplateRendered = template.render(rawText, dataDict)
        
        # Render with actual language text
        pyTemplate = Template(googleTemplateRendered)
        lang = getLang(self)
        languageDict = loadLanguage(lang)
        stringReplaced = pyTemplate.safe_substitute( languageDict ) 
        
        self.response.out.write(stringReplaced)