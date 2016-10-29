'''
Created on Oct 19, 2010

@author: joeykblack
'''


from action.SGRequestHandler import SGRequestHandler

class Directions(SGRequestHandler):
        
        
    def post(self):
        super(Directions, self).render("directions")

    def get(self):
        self.post()
        