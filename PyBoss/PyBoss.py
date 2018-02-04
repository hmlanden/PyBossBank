# import modules
import csv
import os


# get filename
file_name = 'raw_data/employee_data1.csv'
file_output = 'cleaned_data.csv'

# open file
with open(file_name) as original:
    employee_data_reader = csv.DictReader(original)
    
    # iterate over file and pull in data
    for row in employee_data_reader:
        print(row)


# clean data


# export file

