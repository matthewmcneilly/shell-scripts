#!/usr/bin/python

import subprocess

# Runs commands and saves output in a variable
# Handy to capture errors spit out
output = subprocess.check_output(['ls', '-l'])
print(output)
