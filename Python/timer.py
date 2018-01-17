#!/usr/bin/python

# Import time package that comes with Python
# import time
from time import localtime, strftime, mktime

# Grab and print the current time in X format
start_time = localtime()
print("Timer start at %s" % strftime("%X", start_time))

# Wait for user input
raw_input("Please press Enter to continue...")

# Grab current time
stop_time = localtime()
# Compare the difference between times
difference = mktime(stop_time) - mktime(start_time)

# Display stop time and difference
print("Timer stopped at %s" % strftime("%X", stop_time))
print("Total time: %s seconds" % difference)
