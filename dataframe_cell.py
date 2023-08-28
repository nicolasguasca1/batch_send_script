import os
import pandas as pd
import json

import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--folder_to_filter', type=str,
                    help='Folder name of the attachments to filter')
args = parser.parse_args()

content_folder = args.folder_to_filter

# List to store records
data_dict = {}
directories_above_threshold = []
quantity_threshold = 1000
directory_name = os.path.basename(content_folder)
# directory_name = os.path.abspath(content_folder) 
output_compiled_directory = f"{directory_name}_Compiled"
# os.makedirs(output_compiled_directory, exist_ok=True)
# EXPERIMENT________________________________________________
# Iterate over all files in the 'Content' folder
for root, _, files in os.walk(content_folder):
    dir_b_path = os.path.join(content_folder, root)
    directory_data = {}
    filtered_dfs = []
    for file in files:
        filtered_rows = None
        if file.endswith('.csv'):
            csv_file_path = os.path.join(dir_b_path, file)
            with open(csv_file_path, 'r') as csv_file:
                df = pd.read_csv(csv_file)
                # Check for lines where 'Quantity' column is 1000 or more

                filtered_rows = df[df['Quantity'] >= quantity_threshold]
                if filtered_rows is not None:
                    filtered_dfs.append(filtered_rows)
                    
                file_data = []

                for index, row in filtered_rows.iterrows():
                    record = {
                        # Assuming 'ISRC' is the column name
                        'ISRC': row['ISRC'],
                        'Quantity': row['Quantity']
                    }
                    file_data.append(record)
                if file_data:
                    directory_data[file] = file_data
            output_file_compiled = "Rows_Above_1000.csv"
            # output_file_compiled = os.path.join(
            #     root, "_Rows_Above_1000.csv")
            # Create the complete path for the output CSV file
            output_csv_path = os.path.join(root, output_file_compiled)
            # Concatenate all filtered DataFrames into a single DataFrame
            result_df = pd.concat(filtered_dfs, ignore_index=True)
            # Write the concatenated DataFrame to a CSV file
            result_df.to_csv(output_csv_path, index=False)
    if directory_data:
        data_dict[root] = directory_data


# Save the records to a JSON file in valid JSON format
output_file = 'filtered_cell_records.json'
with open(output_file, 'w') as json_file:
    json.dump(data_dict, json_file, indent=4)

print(f"Filtered records saved to '{output_file}'")
print(
    f"Enterprise folder filtered records saved to '{output_compiled_directory}'")


# EXPERIMENT________________________________________________

# # Get a list of subdirectories inside the 'Content' folder
# subdirectories = [subdir for subdir in os.listdir(
#     content_folder) if os.path.isdir(os.path.join(content_folder, subdir))]

# # Iterate over subdirectories
# for subdir in subdirectories:
#     subfolder_path = os.path.join(content_folder, subdir)

#     # Get a list of CSV files in the subdirectory
#     csv_files = [file for file in os.listdir(
#         subfolder_path) if file.endswith('.csv')]

#     if csv_files:
#         csv_file_path = os.path.join(
#             subfolder_path, csv_files[0])  # Get the first CSV file

#         # Read the CSV file into a DataFrame
#         df = pd.read_csv(csv_file_path)

#         # Print the values of the first and second lines
#         if len(df) >= 2:
#             first_line = df.iloc[0]
#             second_line = df.iloc[1]
#             print(f"Subdirectory: {subdir}, CSV File: {csv_files[0]}")
#             print("Values in the first line:")
#             print(first_line)
#             print("Values in the second line:")
#             print(second_line)
#             print("-" * 40)
#         break
