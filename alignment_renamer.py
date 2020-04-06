#!/usr/bin/python3

import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument("-i", help='Input file', required=True)
parser.add_argument("-s", help='Strict rename', action='store_true')
args = parser.parse_args()

file = args.i

input = open(file).readlines()
output = open(f'{"/".join(file.split("/")[:-1])}/r_{file.split("/")[-1]}', 'w')
old = ''

for i in range(len(input)):
    if '>' in input[i]:
        if args.s:
            output.write('>' + input[i][3:8] + '\n')
        else:
            tekst = input[i][:8]
            if old:
                if tekst == old:
                    index_t += 1
                else:
                    old = tekst
                    index_t = 1
            else:
                old = tekst
                index_t = 1
            output.write(tekst + '_' + str(index_t) + '\n')
    else:
        output.write(input[i])
