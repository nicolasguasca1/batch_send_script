import os
import csv
import pandas as pd

import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--folder_to_filter', type=str,
                    help='Folder name of the attachments to filter')
args = parser.parse_args()

parent_directory = args.folder_to_filter

directories_above_threshold = []

threshold = 1000
output_file = 'filtered_data.csv'
# List to store filtered DataFrames from different directories


for dir_b in os.listdir(parent_directory):
    dir_b_path = os.path.join(parent_directory, dir_b)
    filtered_dfs = []
    if os.path.isdir(dir_b_path):
        cells = {}
        for filename in os.listdir(dir_b_path):
            filtered_df = None
            if filename.endswith('.csv'):
                csv_path = os.path.join(dir_b_path, filename)
                with open(csv_path, 'r') as csv_file:
                    # EXPERIMENTATION
                    df = pd.read_csv(csv_file)
                    # Find the index of the 'Score' column
                    quantity_column = df.columns[df.columns == 'Quantity'][0]
                    ISRC_column = df.columns[df.columns == 'ISRC'][0]

                    # Filter rows where the 'Score' column is above the threshold
                    filtered_df = df[df[quantity_column] >= threshold]
                    # Append the filtered DataFrame to the list
                    filtered_dfs.append(filtered_df)
                    if filtered_df is not None:
                        directories_above_threshold.append([dir_b, csv_path])

                    # Print the filtered DataFrame
                    # print(filtered_df)

            #         csv_reader = csv.reader(csv_file)
            #         # Check if the file is empty before trying to read the first row
            #         try:
            #             first_row = next(csv_reader)
            #         except StopIteration:
            #             continue  # Move to the next file
            #         quantity_index = None
            #         ISRC_index = None
            #         for index, column in enumerate(first_row):
            #             if column == 'Quantity':
            #                 quantity_index = index
            #             if column == 'ISRC':
            #                 ISRC_index = index
            #                 break  # Exit the loop once the columns are found

            #         if quantity_index is None and ISRC_index is None:
            #             print("Indexes not found in the CSV.")
            #         else:

            #             for line in csv_reader:
            #                 # values = line.strip().split(',')  # Split the line into a list of values
            #                 # if quantity_index < len(line):
            #                 # Assuming the quantity is at index 2
            #                 quantity = int(line[quantity_index])

            #                 if quantity >= threshold:
            #                     print(
            #                         f"File: {csv_path}, with ISRC: {line[ISRC_index]}, has a Quantity: {quantity} which is above the threshold.")

            # # if 'Quantity' in first_row and int(first_row[quantity_index]) >= 1000:
            #                 directories_above_threshold.append(
            #                     [dir_b, csv_path])
                # break  # No need to check other files in this directory
        # Concatenate all filtered DataFrames into a single DataFrame
        result_df = pd.concat(filtered_dfs, ignore_index=True)
        # Write the concatenated DataFrame to a CSV file
        result_df.to_csv(output_file, index=False)
        # Step 6: Create 'directories_above.txt'
    with open('directories_above_Quantity.txt', 'w') as dir_file:
        for dir_name in directories_above_threshold:
            dir_file.write(f"{dir_name}\n")
print(f"Filtered data from all directories saved to '{output_file}'")

print("Directories with CSV files where 'Quantity' is above 1000:",
      directories_above_threshold)
