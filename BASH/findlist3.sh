#!/bin/bash
# List the contents of a directory and output to a file


# Variables which are captured from arguments passed in when the script is ran 
location=$1
filename=$2

# If no location or filename given display an message
# Only if first if statement is passed will the second execute
if [ -z "$location" ]
then
	echo "please provide a location argument"
  	exit 0	
fi

if [ -z "$filename" ]
then
	echo "please provide a filename"
	exit 0 
fi
 
List the location given to the filename given
# >> is for append and > create a new
ls $location > $filename 
echo "Script is complete and has indexed the $location"
echo "###################"
echo "Displaying contents of our $filename"
echo "###################"
cat $filename   
