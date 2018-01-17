#!/usr/bin/python

# Run this to change the STAGE
# STAGE=staging ./defualt-env.py

import os

# stage = os.environ["STAGE"].upper()
# Get STAGE value if none, set to developement, then convert to uppercase
stage = (os.getenv("STAGE") or "development").upper()

output = "We're running in %s" % stage

# If in product environment alert the user
if stage.startswith("PROD"):
    output = "DANGER!!! - " + output

print(output)
