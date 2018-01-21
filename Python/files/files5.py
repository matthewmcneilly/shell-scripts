#!/usr/bin/python

# Shorter version of the code block below
with open('xmen.txt', 'a') as xmen_file:
    xmen_file.write("Professor Xavier\n")

'''
xmen_file = open('xmen.txt', 'a')

xmen_file.writelines(['Morph\n', 'Rouge\n'])

xmen_file.close()
'''
