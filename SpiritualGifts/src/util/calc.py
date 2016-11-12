'''
Created on Oct 19, 2010

@author: joey
'''
from util import constants
from util.utils import buildQuestionKey




def totals(request):
    giftingTotals = {}
    
    # Add up totals
    # For each category
    for categorie in constants.categories:
        giftingTotals[categorie] = {}
        
        # For each gifting in category
        for gift in constants.gifting[categorie]:
            giftingTotals[categorie][gift] = 0
            
            # For each question in category_gifting
            for index in range(1, 6):
                # Sum up gifting totals
                key = buildQuestionKey(categorie, gift, index)
                if (request.get(key)):
                    giftingTotals[categorie][gift] += int(request.get(key))
                else:
                    giftingTotals[categorie][gift] += 1
                    
    return giftingTotals 

def categoryTotals(giftingTotals):
    categoryTotals = {}

    # Add up totals
    # For each category
    for categorie in constants.categories:
        categoryTotals[categorie] = 0
        # For each gifting in category
        for gift in constants.gifting[categorie]:
            categoryTotals[categorie] += giftingTotals[categorie][gift]
            
    return categoryTotals