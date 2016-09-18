'''
Created on Oct 20, 2010

@author: joeykblack
'''

from util import constants
import csv

narratives = {}

# load narratives from csv file into array
# NOTE: "Gift 5-14" or "Gift 15-25" used as keys
# Keys must be in order
def loadNarratives(lang):
    #reader = csv.reader(template.render('csv/narratives.csv',{}))
    reader = csv.reader(open("csv/narratives-%s.csv" % lang, 'rb'))
    for row in reader:
        line = row
        narratives[(line[0], line[1], line[2], line[3], line[4])] = line[5]



# NOTE: Prefixes for keys must be in order of how they are in csv file
def getPrefix(category, categories):
    if category== categories[0]:
        prefix = ["Serv ","Show ","Hosp ","Enc ","Giv "]
    elif category== categories[1]:
        prefix = ["Wis ","Know ","Prop ","Tea ","Evan "]
    elif category== categories[2]:
        prefix = ["Adm ","Lead ","Pas ","Apos ","Faith "]
    else:
        prefix = ["Heal ","Mir ","Dist ","Tong ","Inter "]
        
    return prefix


# select range with given score (for key)
# ranges changed from 5-15 and 15-25
# to 1-9 and 10-20
# HOWEVER, naratives.csv was NOT changed because this is easier
def srange(score):
    if score<10:
        r = "5-14"
    else:
        r = "15-25"
    
    return r


# get narrative for given category and scores
# NOTE: scores must be in order matching csv file
def getNarrative(category, scores):
    prefix = getPrefix(category, constants.categories)
    gifts = constants.gifting[category]
    key = [prefix[0]+srange(scores[gifts[0]]), prefix[1]+srange(scores[gifts[1]]),  prefix[2]+srange(scores[gifts[2]]), prefix[3]+srange(scores[gifts[3]]), prefix[4]+srange(scores[gifts[4]])]
        
    return narratives[(key[0], key[1], key[2], key[3], key[4])]


