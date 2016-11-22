'''
Created on Oct 20, 2010

@author: joeykblack
'''

from util import constants

# select range with given score (for key)
def srange(score):
    if score<15:
        r = "05_14"
    else:
        r = "15_25"
    
    return r


# get narrative for given category and scores
def getNarrative(category, scores):
    key = '$'
    for gift in constants.gifting[category]:
        key += gift + '_' + srange(scores[gift]) + '_'
        
    return key[:-1]


