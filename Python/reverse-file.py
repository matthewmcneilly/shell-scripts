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

try:
    f = open(args.filename)
# More than one expect can be used
except IOError as err:
    print("Error: file not found")
else:
    # Read in each line from bottom to top
    with f:
        limit = args.limit
        lines = f.readlines()
        lines.reverse()

        # If limit specified use it
        if limit:
            lines = lines[:args.limit]

        # Strip lines of whitepsace, reverse and print them
        for line in lines:
            print(line.strip()[::-1])

# Not really needed as else statement closes itself
finally:
    print("\nWe're finished\n")

