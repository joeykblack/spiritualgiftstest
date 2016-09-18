'''
Created on Oct 21, 2010

@author: joeykblack
'''
from google.appengine.api import users


def loadloginout(handler):
    user = users.get_current_user()
    loginout='<div class="loginout">'
    if user:
        loginout+=user.nickname()+' - '
        loginout+='<a href="'+users.create_logout_url(handler.request.uri)+'">Logout</a>'
    else:
        loginout+='<a href="'+users.create_login_url(handler.request.uri)+'">Login</a>'
    loginout+='</div>'

    return loginout
