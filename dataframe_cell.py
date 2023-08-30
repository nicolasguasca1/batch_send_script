import os
import pandas as pd
import json
import csv


import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--folder_to_filter', type=str,
                    help='Folder name of the attachments to filter')
args = parser.parse_args()

content_folder = args.folder_to_filter

# List to store records
data_dict = {}
directories_above_threshold = []
directories_below_threshold = []
directories_above_threshold_count = 0
directories_below_threshold_count = 0
quantity_threshold = 1000
quantities_concerning = {}
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
    quantity_per_concerning_company = 0
    for file in files:
        filtered_rows = None
        if file.endswith('.csv'):
            csv_file_path = os.path.join(dir_b_path, file)
            with open(csv_file_path, 'r') as csv_file:
                quantity_above_per_file = 0
                df = pd.read_csv(csv_file)
                # Check for lines where 'Quantity' column is 1000 or more

                filtered_rows = df[df['Quantity'] >= quantity_threshold]
                if filtered_rows is not None:
                    quantity_above_per_file = filtered_rows['Quantity'].sum()
                    
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
                    quantity_per_concerning_company += quantity_above_per_file
                # json_concerning = {
                #     'Total amount': 
                # } 
              
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
        # data_dict[root]['Total amount']=quantity_per_concerning_company
        # if os.path.basename(root) not in directories_above_threshold:
        directories_above_threshold_count += 1
        directories_above_threshold.append(os.path.basename(root))
        quantities_concerning[os.path.basename(root)] = quantity_per_concerning_company
    else:
        if os.path.basename(root) != directory_name:
            directories_below_threshold_count += 1
            directories_below_threshold.append(os.path.basename(root))
    with open('directories_above_1000.txt', 'w') as dir_file:
        for dir_name in directories_above_threshold:
            dir_file.write(f"{dir_name}\n")
    with open('directories_below_1000.txt', 'w') as dir_file:
        for dir_name in directories_below_threshold:
            dir_file.write(f"{dir_name}\n")

sorted_concerning = sorted(quantities_concerning.items(), key=lambda x: x[1], reverse=True)
top_5_arrays = sorted_concerning[:5]
# Save the records to a JSON file in valid JSON format
output_file = 'filtered_cell_records.json'
output_file_sum = 'concerning_records_sum.csv'
with open(output_file, 'w') as json_file:
    json.dump(data_dict, json_file, indent=4)

# Convert the dictionary to a DataFrame
df3 = pd.DataFrame(list(quantities_concerning.items()), columns=['EntId','Total sum'])

# Save the DataFrame to a CSV file
df3.to_csv(output_file_sum, index=False)
# with open(output_file_sum, 'w', newline='') as json_file2:
#     writer = csv.DictWriter(json_file2, fieldnames=quantities_concerning.keys())
#     writer.writeheader()
#     json.dump(quantities_concerning, json_file2, indent=4)

print(f"Filtered records saved to '{output_file}'")
print("Directories with CSV files where 'Quantity' is above 1000:",
     directories_above_threshold_count)
print("Directories with CSV files where 'Quantity' is below 1000:",
     directories_below_threshold_count)
print("The top five directories with the most AS with the scheme ['company',total_sum] are the following:",
     top_5_arrays)




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
