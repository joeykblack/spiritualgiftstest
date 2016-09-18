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
        print en['dirrections_page_title']
        pass
    
    def testTemplating(self):
        en = loadLanguage("English")
        s = Template('Title: $dirrections_page_title')
        print s.substitute(en)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testLanguageSub']
    unittest.main()