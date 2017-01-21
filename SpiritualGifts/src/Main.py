'''
Created on Oct 19, 2010

@author: joey black (joeykblack@gmail.com)
'''


from google.appengine.ext import webapp
from action.directions import Directions
from action.help import Help
from action.test import Test
from action.results import Results
from action.restest import Restest
from action.admin import Admin, Retake
from action.userdetails import Userdetails
from action.norms import Norms
from action.export import Export
from action.modresults import ModResults



app = webapp.WSGIApplication(
                                     [
                                      ('/', Directions),
                                      ('/test', Test),
                                      ('/results', Results),
                                      ('/test/results', Restest),
                                      ('/admin', Admin),
                                      ('/userdetails', Userdetails),
                                      ('/retake', Retake),
                                      ('/norms', Norms),
                                      ('/export', Export),
                                      ('/modresults', ModResults),
                                      ('/help', Help)
                                     ],
                                     debug=True)

