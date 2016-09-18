'''
Created on Oct 21, 2010

@author: joeykblack
'''
from google.appengine.api import mail


def sendResults(resultset):
    giftsuser = resultset.giftsuser
    
    if mail.is_email_valid(giftsuser.email):
        message = mail.EmailMessage()
        message.sender = 'Chuck Coker <chuck.coker@meclabs.com>'
        message.to = giftsuser.firstname + ' ' + giftsuser.lastname + ' <' + giftsuser.email + '>'
        message.subject = 'Your Spiritual Gifts Results'
        message.body = 'You can access your results at ' + resultset.url
        
        message.send()