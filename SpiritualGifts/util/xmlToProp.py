'''
Created on Sep 18, 2016

@author: joey
'''

import re


if __name__ == '__main__':
    pattern = re.compile('question\snum="(\d+)"\scategory="(\w+)"\sgifting="(\w+)"')
    with open('xml/test-lg.xml') as f:
        key=None
        for line in f:
            match = pattern.search(line)
            if match:
                key = match.group(3)+"_"+match.group(2)+"_Question_"+match.group(1)
            elif key:
                print key + " = " + line.strip()
                key = None
