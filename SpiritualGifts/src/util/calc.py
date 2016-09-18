'''
Created on Oct 19, 2010

@author: joey
'''
from util import constants




categoryTotals = {}
giftingTotals = {}

def totals(re):
    
    # Add up totals
    # For each category
    for categorie in constants.categories:
        categoryTotals[categorie] = 0
        giftingTotals[categorie] = {}
        
        # For each gifting in category
        for gift in constants.gifting[categorie]:
            key = categorie+"_"+gift+"_"
            giftingTotals[categorie][gift] = 0
            
            # For each question in category_gifting
            for index in range(1, 6):
                # Sum up gifting totals
                if (re.get(key+str(index))):
                    giftingTotals[categorie][gift] += int(re.get(key+str(index)))
                else:
                    giftingTotals[categorie][gift] += 0
            
            # Sum up category totals from gifting totals
            categoryTotals[categorie] += giftingTotals[categorie][gift]
    



