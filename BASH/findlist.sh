#!/bin/bash
# List the contents of a directory and output to a file


# Variable which is captured from arguments passed in when script is ran 
location=$1

# Uses variables as the location to list 
ls $location >> dir_list.txt
echo "Script is complete and has indexed the $location"   
