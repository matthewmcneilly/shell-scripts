import random
import os
import json

# Useful for creating file to use with other scripts
# Creates receipts with a topic and value pair

# Get environment variable FILE_COUNT value or use 100
count = os.getenv("FILE_COUNT") or 100
words = [word.strip() for word in open('/usr/share/dict/words').readlines()]

'''
Same as using a while loop e.g. while id < count:
1 is the starting number, count is the end number
Best practice to avoid writing infinite loops
'''
for identifier in range(1, count + 1):
    amount = random.uniform(1.0, 1000.0) # generate a random number from 1 to 1000
    content = {
            'topic': random.choice(words), # grab a random word
            'value': "%.2f" % amount # ensure number is to 2 decimal points
    }
    # Create a new receipt for each iteration
    with open('./new/receipt-%s.json' % identifier, 'w') as f:
       # Write the content to the file i.e. a topic and value is json format
        json.dump(content, f)


