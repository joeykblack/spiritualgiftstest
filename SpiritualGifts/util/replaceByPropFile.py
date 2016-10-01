'''
Created on Oct 1, 2016

@author: joey
'''

if __name__ == '__main__':
    replacements = dict(line.strip().split('=') for line in open('util/replace.prop'))
    with open('src/text/Oluganda.txt') as f:
        for line in f:
            for key in replacements:
                line = line.replace(key, replacements[key])
            print line.rstrip()