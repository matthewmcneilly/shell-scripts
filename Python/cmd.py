#!/usr/bin/python

import subprocess

# Calls the ls command with -l flag
code = subprocess.call(['ls', '-l'])
# If command called runs succesfully
if code == 0:
  print("Command finished successfully")
# If command fails to run e.g. doesnt exist
else:
  print("Failed with code: %i" % code)


