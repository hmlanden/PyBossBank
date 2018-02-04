# Import modules that we're going to need
import os
import pandas as pd
import locale

# ----------------------------------------------------------------------
# Step 0: Give instructions to the user
# ----------------------------------------------------------------------
print()

# ----------------------------------------------------------------------
# Step 1: Get all my data into a clean data frame that I can manipulate
# ----------------------------------------------------------------------

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

# ----------------------------------------------------------------------
# Step 2: Perform analyses
# ----------------------------------------------------------------------

# Total number of months
count_months = len(revenue_df['Date'].unique())

# Total amount of revenue gained over the entire period
total_revenue = revenue_df['Revenue'].sum()

# average change in revenue between months over the entire period
average_revenue_change = round(revenue_df['Revenue'].sum() / revenue_df['Revenue'].count(),2)


# greatest increase in revenue over the entire period
greatest_increase_amount = float(revenue_df['Revenue'].max())

# find the date for that amount
revenue_reindex_df = revenue_df.set_index(['Revenue'])
greatest_increase_date = revenue_reindex_df.loc[greatest_increase_amount,'Date']

# greatest decrease in revenue over the entire period
greatest_decrease_amount = revenue_df['Revenue'].min()
revenue_reindex_df = revenue_df.set_index(['Revenue'])
greatest_decrease_date = revenue_reindex_df.loc[greatest_decrease_amount,'Date']

# set currency 
locale.setlocale( locale.LC_ALL, 'en_US' )

# ----------------------------------------------------------------------
# Step 3: Format and print results in terminal
# ----------------------------------------------------------------------

# print header
print("Financial Analysis")
print('-' * 60)

# print results
print("Time Period: {} months".format(count_months))
print("Total Revenue: "+ str(locale.currency(total_revenue,grouping=True)))
print("Average Revenue Change: " + str(locale.currency(average_revenue_change,grouping=True)))
print("Greatest Increase in Revenue: "+ str(locale.currency(greatest_increase_amount,grouping=True)) + \
      " (" + greatest_increase_date + ")")
print("Greatest Decrease in Revenue: "+ str(locale.currency(greatest_decrease_amount,grouping=True)) + \
      " (" + greatest_decrease_date + ")")
print('-' * 60)

# print close
print("The results of this analysis can be found in the text file named analysis_{}.txt.".format(revenue_file))


# ----------------------------------------------------------------------
# Step 4: Create and write results file
# ----------------------------------------------------------------------

# open the output file
revenue_file_split = revenue_file.split("/")
revenue_file_remove_csv = str(revenue_file_split[1]).split(".")
output_filename = str("analysis_" + str(revenue_file_remove_csv[0]) + ".txt")
results_file = open(output_filename,'w+')

# write to file
results_file.write("Financial Analysis \n")
results_file.write('-' * 60 + "\n")
results_file.write("Time Period: {} months  \n".format(count_months))
results_file.write("Total Revenue: "+ str(locale.currency(total_revenue,grouping=True)) +  "\n")
results_file.write("Average Revenue Change: " + str(locale.currency(average_revenue_change,grouping=True)) +  "\n")
results_file.write("Greatest Increase in Revenue: "+ str(locale.currency(greatest_increase_amount,grouping=True)) + \
                  " (" + greatest_increase_date + ")" +  "\n")
results_file.write("Greatest Decrease in Revenue: "+ str(locale.currency(greatest_decrease_amount,grouping=True)) + \
                  " (" + greatest_decrease_date + ")" +  "\n")
results_file.write('-' * 60)
results_file.close()