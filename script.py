import pandas as pd

# Read the Excel file and extract the desired columns
# Adjust the file name and column indices as needed
df = pd.read_excel(
    '/Volumes/NICO_HD_(MyPassport)/nicolasguascasantamaria/Documents/REVELATOR/APIS/customers.xlsx', usecols=[6, 7])

# Convert the columns to a set
column_set = set(zip(df.iloc[:, 0], df.iloc[:, 1]))

# Print the resulting set
print(column_set)
