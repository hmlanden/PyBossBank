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
        
        # split name, remove it, and add first and last name to the dictionary
        first_name,last_name = row['Name'].split()
        del row['Name']
        row['First Name'], row['Last Name'] = first_name, last_name


# clean data


# export file

