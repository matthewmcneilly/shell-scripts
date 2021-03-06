#!/usr/bin/python

import argparse

# User must provide a search term 'snippet'
parser = argparse.ArgumentParser(description='Search for words including partial words')
parser.add_argument('snippet', help='partial or (complete) string to search for in the words file')

args = parser.parse_args()
snippet = args.snippet.lower()

# Read dict words file line by line
words = open('/usr/share/dict/words').readlines()

# Shorten version of code block in contains.py using list comprehension
print([word.strip() for word in words if snippet in word.lower()])

