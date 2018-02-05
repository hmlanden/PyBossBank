# import modules
import csv
import os

# thank you @afhaque for this dictionary!
# can be found here: https://gist.github.com/afhaque/29f0f4f37463c447770517a6c17d08f5
us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}

# get filename
file_name = input("Please insert the file name here: ")
file_output = input("Please insert the name you want on the ouput file: ")

# open file
with open(file_name, 'r') as original, open(file_output, 'w') as new:
    #create file readers and writers
    employee_data_reader = csv.DictReader(original)
    header_names = ['Emp ID', 'First Name', 'Last Name', 'SSN', 'DOB', 'State']
    employee_data_writer = csv.DictWriter(new, fieldnames=header_names)

    # write header row
    employee_data_writer.writeheader()
    
    # iterate over file
    for row in employee_data_reader:
        
        # split name, remove it, and add first and last name to the dictionary
        first_name, last_name = row['Name'].split()
        row['First Name'], row['Last Name'] = first_name, last_name
        del row['Name']
        
        # reformat birthdate
        birth_year, birth_month, birth_day = row['DOB'].split('-')
        row['DOB'] = "{}/{}/{}".format(birth_month, birth_day, birth_year)
        
        # remove all but last four of the SSN
        split_SSN = row['SSN'].split('-')
        row['SSN'] = "{}-{}-{}".format('***', '**', split_SSN[2])
        
        # change the states to the abbreviations
        row['State'] = us_state_abbrev[row['State']]
      
        # rearrange "columns" 
        row.move_to_end('SSN')
        row.move_to_end('DOB')
        row.move_to_end('State')
        
        # write row to the new file
        employee_data_writer.writerow(row)

print("Check out the file! We're done reformatting the file.")