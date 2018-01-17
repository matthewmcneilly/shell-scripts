#!/usr/bin/python

# Captures input as a string
name = raw_input("What is your name?")
birthdate = raw_input("What is your birthdate? ")

# Captures input as an appropiate data type
age = input("How old are you? ")
# Best practice would be
# age = int(raw_input("How old are you? "))

print("%s was born on %s" % (name, birthdate))
print("Half of your age is %s" %(age /2))
