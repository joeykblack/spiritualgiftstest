'''
Created on Oct 19, 2010

@author: joeykblack
'''


from action.SGRequestHandler import SGRequestHandler

class Help(SGRequestHandler):
        
        
    def post(self):
        super(Help, self).render("help")

    def get(self):
        self.post()
        