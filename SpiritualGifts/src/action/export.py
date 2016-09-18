'''
Created on Feb 13, 2010

@author: joeykblack
'''

from model.results import Resultset
from model.user import GiftsUser
from action.SGRequestHandler import SGRequestHandler

class Export(SGRequestHandler):
    def get(self):
        super(Export, self).render('exportform')
        
    def post(self):
        table=self.request.get('table')
        csv=''
        
        if table=='Resultset':
            csv='Date,Email,url,Results'+'<br/>'
            resultSet=Resultset().all().fetch(1000)
            for res in resultSet:
                csv += str(res.date)+','+res.giftsuser.email+','+res.url+',"'
                for ans in res.results:
                    csv += ans+':'
                csv += '"<br />'
        elif table=='GiftsUser':
            csv='Email,First Name,Last Name,Gender,Age,Interest,State,Country'+'<br />'
            giftsUsers=GiftsUser().all().fetch(1000)
            for user in giftsUsers:
                csv += user.email+','+user.firstname+','+user.lastname+','+user.gender+','+user.age+','+user.interest+','+user.state+','+user.country+'<br />'
        
        self.response.out.write(csv)
