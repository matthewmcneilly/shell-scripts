import glob
import os
import shutil
import json

# To run script
# python process_receipts.py

# Ensure processed directory exists
try:
    os.mkdir("./processed")
except OSError:
    print("'processed' directory already exists")

# Get a list of receipts
# Returns a list which match a specified pattern
receipts = glob.glob('./new/receipt-[0-9]*.json')

subtotal = 0.0

# Open each receipt
for path in receipts:
    with open(path) as f:
        content = json.load(f)
        # Total all of the receipt values
        subtotal += float(content['value'])
    # Take the last part of the path as use it as the name
    name = path.split('/')[-1]
    destination = "./processed/%s" % name
    # Move receipt to the processed directory
    shutil.move(path, destination)
    # Print a message to confirm the file being moved
    print("moved '%s' to '%s'" % (path, destination))

# Display final subtotal to 2 decimal places
print("Receipt subtotal: $%.2f" % subtotal)


