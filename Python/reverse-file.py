#!/usr/bin/python

import argparse

# Program description
parser = argparse.ArgumentParser(description='Read a file in reverse')
# Positional argument - file to be reversed
parser.add_argument('filename', help='the file to read')
# Optional argument the finite number of lines you want reversed
parser.add_argument('--limit', '-l', type=int, help='the number of the lines to read')
# Program version number e.g. reverse-file.py 1.0
parser.add_argument('--version', '-v', action='version', version='%(prog)s 1.0')

args = parser.parse_args()

'''
print(args)
Would print something like this
Namespace(filename='somefilename', limit=None)
filename and limit are atributes
Namespace is an object
'''

# Read in each line from bottom to top
with open(args.filename) as f:
    lines = f.readlines()
    lines.reverse()

# If limit specified use it
    if args.limit:
        lines = lines[:args.limit]
# Strip lines of whitepsace, reverse and print them
    for line in lines:
        print(line.strip()[::-1])


