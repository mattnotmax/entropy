#!/usr/bin/env python
'''
Calculate Shannon Entropy (min bits per byte-character)
original source: https://www.kennethghartman.com/calculate-file-entropy/
'''

__version__ = '0.1'
__description__ = 'Calculate Shannon Entropy for given file'

import sys
import math

def main():
    entropy()

def entropy():
    print('Opening file {}...'.format(sys.argv[1]))
    with open(sys.argv[1], 'rb') as f:
        byteArr = list(f.read())
    fileSize = len(byteArr)
    print
    print('File size in bytes: {:,d}'.format(fileSize))
    # calculate the frequency of each byte value in the file
    print('Calculating Shannon entropy of file. Please wait...')
    freqList = []
    for b in range(256):
        ctr = 0
        for byte in byteArr:
            if byte == b:
                ctr += 1
        freqList.append(float(ctr) / fileSize)
    # Shannon entropy
    ent = 0.0
    for freq in freqList:
        if freq > 0:
            ent = ent + freq * math.log(freq, 2)
    ent = -ent
    print('Shannon entropy: {}'.format(ent))
    print


if __name__== "__main__":
    main()
