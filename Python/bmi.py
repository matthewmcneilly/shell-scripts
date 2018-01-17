#!/usr/bin/python

height = float(raw_input("What is your height? (inches or meters) "))
weight = float(raw_input("What is your weight? (pounds or kilograms) "))
unit = raw_input("Are your measurements in metric or imperial units? ").lower().strip()

if unit.startswith('i'):
    bmi = 703 * (weight / (height ** 2))
elif unit.startswith('m'):
    bmi = (weight / (height ** 2))

print("Your BMI is %s" % bmi)
