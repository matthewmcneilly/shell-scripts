import glob
import os
import shutil
import json
import re
import math

# To run script
# python process_receipts.py

# Ensure processed directory exists
try:
    os.mkdir("./processed")
except OSError:
    print("'processed' directory already exists")

# Get a list of receipts
# Returns a list which match a specified pattern
#receipts = glob.glob('./new/receipt-[0-9]*.json')

# Returns all receipts that are evenly numbered, uses a regular expression
# iglob is same as glob but doesnt store all the values simultaneously, more performant
receipts = [f for f in glob.iglob('./new/receipt-[0-9]*.json')
        if re.match('./new/receipt-[0-9]*[02468].json', f)]


subtotal = 0.0

# Open each receipt
for path in receipts:
    with open(path) as f:
        content = json.load(f)
        # Total all of the receipt values
        subtotal += float(content['value'])
    # More succinct way
    destination = path.replace('new', 'processed')
    # name = path.split('/')[-1]
    # destination = "./processed/%s" % name


    # Move receipt to the processed directory
    shutil.move(path, destination)
    # Print a message to confirm the file being moved
    print("moved '%s' to '%s'" % (path, destination))

# Display final subtotal to 2 decimal places
#print("Receipt subtotal: $%.2f" % subtotal)
print("Receipt subtotal: $%s" % round(subtotal, 2))





