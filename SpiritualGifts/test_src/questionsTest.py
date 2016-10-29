'''
Created on Oct 3, 2016

@author: joey
'''

from util import constants
from util.utils import buildQuestionKey
from random import shuffle

if __name__ == '__main__':
    questions = [buildQuestionKey(category, gift, i) for category in constants.categories for gift in constants.gifting[category] for i in range(1,6)]
    shuffle(questions)
    for question in questions:
        print question
    