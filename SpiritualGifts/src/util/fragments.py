

def langSelector(handler, lang, template_dict={}):
    path = handler.request.path
    form = """
            <form action="%s" method="post" style='float:right; margin-right:5px; clear:both;'>
                <select name='lang' onchange='this.form.submit()'> 
                    <option %s value="en">English</option>
                    <option %s value="lg">Oluganda</option>
                </select>
            """ % (path,
                   "selected='selected'" if lang=='en' else '',
                   "selected='selected'" if lang=='lg' else '') 
            
    form+="<input type='hidden' name='firstname' value='"+handler.request.get("firstname")+"' />"
    form+="<input type='hidden' name='lastname' value='"+handler.request.get("lastname")+"' />"
    form+="<input type='hidden' name='email' value='"+handler.request.get("email")+"' />"   
    form+="<input type='hidden' name='gender' value='"+handler.request.get("gender")+"' />"
    form+="<input type='hidden' name='age' value='"+handler.request.get("age")+"' />"
    form+="<input type='hidden' name='interest' value='"+handler.request.get("interest")+"' />"
    form+="<input type='hidden' name='state' value='"+handler.request.get("state")+"' />"
    form+="<input type='hidden' name='country' value='"+handler.request.get("country")+"' />"
    if 'reskey' in template_dict:
        form+="<input type='hidden' name='reskey' value='"+template_dict['reskey']+"' />"
    form+="</form>"
    
    return form
    
    
def langHidden(lang):
    return "<input type='hidden' name='lang' value='%s' />" % lang

def banner():
    return """
        <div style="clear:both"></div>
        <div align='center'>
                <img src="img/lifethrive191x48.jpg" name="LifeThrive" width="191" height="48" align="center" />
        </div>
        <h5 align='center' style='margin-top: 0'>
            <a href='http://www.lifethrive.com'>www.lifethrive.com</a> - 904-474-3600
        </h5>
        """
