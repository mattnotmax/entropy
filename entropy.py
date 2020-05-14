#!/usr/bin/env python
'''
Calculate Shannon Entropy (min bits per byte-character)
original source: https://www.kennethghartman.com/calculate-file-entropy/
'''

__version__ = '0.1'
__description__ = 'Calculate Shannon Entropy for given file'

import sys
import math
from collections import Counter

def main():
    entropy()

def entropy():
    print('Opening file {}...'.format(sys.argv[1]))
    with open(sys.argv[1], 'rb') as f:
        byteArr = f.read()

    fileSize = len(byteArr)
    print("")
    print('File size in bytes: {:,d}'.format(fileSize))

    # calculate the frequency of each byte value in the file
    print('Calculating Shannon entropy of file. Please wait...')
    counts = Counter(byteArr)
    freqList =  [byteCount / fileSize for byteCount in dict(counts).values()]

    # Shannon entropy
    ent = 0.0
    for freq in freqList:
        ent = ent + freq * math.log(freq, 2)
    ent = -ent
    
    print('Shannon entropy: {}'.format(ent))
    print("")


if __name__== "__main__":
    main()
