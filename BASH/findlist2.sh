#!/bin/bash
# List the contents of a directory and output to a file


# Variables which are captured from arguments passed in when the script is ran 
location=$1
filename=$2

# List the location given to the filename given
# >> is for append and > create a new
ls $location > $filename 
echo "Script is complete and has indexed the $location"
echo "###################"
echo "Displaying contents of our $filename"
echo "###################"
cat $filename   
