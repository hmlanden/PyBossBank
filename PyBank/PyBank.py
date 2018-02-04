# Import modules that we're going to need
import os
import pandas as pd

# Step One: Get all my data into a clean data frame that I can manipulate

# Get paths for the file that we're going to be using
revenue_file = input("Input the path name of the file that you want to analyze! FYI, you're currently at Documents/Github/UCBerkeley_HomeworkAssignment3/ ")

# create a data frame
revenue_df = pd.read_csv(revenue_file)


# I need to get the following data from analyzing the dataframe I just made: 
# - The total number of months included in the dataset
# - The total amount of revenue gained over the entire period
# - The average change in revenue between months over the entire period
# - The greatest increase in revenue (date and amount) over the entire period
# - The greatest decrease in revenue (date and amount) over the entire period


# Step 2: Perform analyses

# Total number of months
count_months = len(revenue_df['Date'].unique())

# Total amount of revenue gained over the entire period
total_revenue = revenue_df['Revenue'].sum()

# average change in revenue between months over the entire period
average_revenue_change = round(revenue_df['Revenue'].sum() / revenue_df['Revenue'].count(),2)


# greatest increase in revenue over the entire period
greatest_increase_amount = revenue_df['Revenue'].max()

# find the date for that amount
revenue_reindex_df = revenue_df.set_index(['Revenue'])
greatest_increase_date = revenue_reindex_df.loc[greatest_increase_amount]
print(type(greatest_increase_date))

# greatest decrease in revenue over the entire period
greatest_decrease_amount = revenue_df['Revenue'].min()



# Step 3: Return results

