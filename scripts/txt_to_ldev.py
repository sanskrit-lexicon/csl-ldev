# This Python file uses the following encoding: utf-8
"""
Usage:
python txt_to_ldev.py dictId
python txt_to_ldev.py mw
"""
from __future__ import print_function
import re
import codecs
import sys
import os


if __name__ == "__main__":
    dictId = sys.argv[1]
    inputfile = os.path.join('..', '..', 'csl-devanagari', 'v02', dictId, dictId + '.txt')
    fin = codecs.open(inputfile, 'r', 'utf-8')
    outputfolder = os.path.join('..', 'v02', dictId)
    if not os.path.exists(outputfolder):
        os.makedirs(outputfolder)
    start = False
    end = False
    for lin in fin:
        if lin.startswith('<L>'):
            start = True
            end = False
            result = lin
            lnum = re.match('<L>(.*?)<', lin).group(1)
            if int(lnum.split('.')[0]) % 1000 == 0:
                print(lnum)
        elif start and (not end):
            result += lin
        if lin.startswith('<LEND>'):
            end = True
            outfile = os.path.join(outputfolder, lnum + '.txt')
            fout = codecs.open(outfile, 'w', 'utf-8')
            fout.write(result)
    fin.close()
    fout.close()
