'''
Created on Sep 24, 2016

@author: joey
'''

import csv

import sys  

reload(sys)  
sys.setdefaultencoding('utf8')


if __name__ == '__main__':
    with open('csv/narratives-en.csv') as f:
        reader = csv.reader(f)
        for row in reader:
            key = '$' + '_'.join(row[0:5]).replace(' ', '_').replace('-', '_')
            print ','.join(row[0:5]) + ',' + key
            