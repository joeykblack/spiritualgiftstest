'''
Created on Oct 7, 2015

@author: joey
'''
from google.appengine.ext import webapp
from google.appengine.ext.webapp import template
from util.utils import getPage, getStdDict

class SGRequestHandler(webapp.RequestHandler):
    
    def render(self, page, template_dict = {}):
        self.response.out.write(template.render(getPage(self, page), 
                                                getStdDict(self, template_dict)))