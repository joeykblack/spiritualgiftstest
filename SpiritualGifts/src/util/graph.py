'''
Created on Oct 19, 2010

@author: joeykblack
'''


#include 'phplib/http.php'

from util import constants

#site = 'http://chart.apis.google.com/chart?'
site = 'http://chart.googleapis.com/chart?'

def graphGiftings(giftingTotals):
    
    sorttotals = []
    totals=""
    sortlabel = []
    label=""
    
    for categorie in constants.categories: 
        for gift in constants.gifting[categorie]:
            sortlabel.append('$'+gift+'_gifting')
            sorttotals.append(giftingTotals[categorie][gift])
        
    totals_labels = zip(sorttotals, sortlabel)
    totals_labels.sort(reverse=True)
    
    for total_label in totals_labels:
            label = '|' + total_label[1] + label
            totals += str(total_label[0]) + ','
    
    totals = totals[0:-1]
    
    data = 'cht=bhs'
    data += '&chs=500x600'
    data += '&chds=0,25' #25
    data += '&chxr=0,0,25' #25
    data += '&chxt=x,y'
    data += '&chco=0000FF'
    data += '&chg=20,0'
    data += '&chxl=0:|0|5|10|15|20|25|1:'+label # |25
    data += '&chd=t:'+totals
    
    return url(data)



def graphCategories(categoryTotals):
    
    label=""
    totals=""
    #categoryTotals = categoryTotals.reverse()
    for category in constants.categories: 
        totals += str(categoryTotals[category])+","
        label = "|$"+category+"_category"+label
    
    totals = totals[0:-1]
        
    data = 'cht=bhs'
    data += '&chs=500x200'
    data += '&chds=0,125'
    data += '&chxr=0,0,125'
    data += '&chxt=x,y'
    data += '&chco=0000FF'
    data += '&chg=20,0'
    data += '&chxl=0:|0|25|50|75|100|125|1:'+label
    data += '&chd=t:'+totals

    return url(data)


def giftGraph(score):

    data = 'cht=bhs&'
    data += 'chs=500x50&'
    data += 'chds=0,25&'
    data += 'chxr=0,0,25&'
    data += 'chxt=x&'
    data += 'chco=0000FF&'
    data += 'chg=20,0&'
    data += 'chm=N*f1y*,000000,0,-1,11,,:10:&'
    data += 'chxl=0:|0|5|10|15|20|25&'
    data += 'chd=t:'+str(score)
    
    return url(data)


def normGraph(norm):

    data = 'chxt=x,y&'
    data += 'chbh=a&'
    data += 'chs=300x60&'
    data += 'cht=bhg&'
    data += 'chco=0000FF&'
    data += '&chxl=&'
    
    if norm.type=='cat':
        data += 'chxr=0,0,125&' #125
        data += 'chds=0,125&' #125
        data += 'chxl=0:|0|25|50|75|100|125|1:|%2B1%CF%83|Average|-1%CF%83&' # |125 
    else:
        data += 'chxr=0,0,25&' #25
        data += 'chds=0,25&' #25
        data += 'chxl=0:|0|5|10|15|20|25|1:|%2B1%CF%83|Average|-1%CF%83&' # |25
    
    data += 'chd=t:'+str(norm.low)+','+str(norm.average)+','+str(norm.high)
    
    print data
    
    return url(data)


def url(data):
    return site+(data.replace(' ', '%20'))
