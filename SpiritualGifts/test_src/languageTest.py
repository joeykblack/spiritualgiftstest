'''
Created on Sep 18, 2016

@author: joey
'''
import unittest

from util.text import loadLanguage
from string import Template


class Test(unittest.TestCase):


    def testLanguageSub(self):
        en = loadLanguage("English")
        print en['directions_page_title']
        print en['Romans_12']
        print en['romans_12']
        print en['Displaying_Gods_love_Serving_Helps_1']
        pass
    
    def testTemplating(self):
        en = loadLanguage("English")
        s = Template('Title: $directions_page_title')
        s = Template('Question: $Displaying_Gods_love_Serving_Helps_1')
        print s.substitute(en)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testLanguageSub']
    unittest.main()