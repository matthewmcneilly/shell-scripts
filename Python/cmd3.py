#!/usr/bin/python

import subprocess

# run the following command and capture any output
# useful because the same code written in a different way can throw a different error
# e.g. "ls fake.txt" and  ['ls', 'fake.txt']
try:
    output = subprocess.check_output(
            ['ls', '-l'],
            stderr=subprocess.STDOUT
            )
# if no argument is given e.g. command
except OSError as err:
    # print meaningful message and captured output error
    print("Caught OSError")
    output = err
# if non existent command is given
except subprocess.CalledProcessError as err:
    print("Caught CallProccessError")
    output = err

print(output)

