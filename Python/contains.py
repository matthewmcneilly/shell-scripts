#!/usr/bin/python

import argparse

# User must provide a search term 'snippet'
parser = argparse.ArgumentParser(description='Search for words including partial words')
parser.add_argument('snippet', help='partial or (complete) string to search for in the words file')

args = parser.parse_args()
snippet = args.snippet.lower()

# Read dict words file line by line
words = open('/usr/share/dict/words').readlines()
matches = []

# If snippet matches the current word add it as a match
for word in words:
    if snippet in word.lower():
        matches.append(word)

# Display all the matches
print(matches)


