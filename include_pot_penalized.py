import os
import pandas as pd
import sys
import os
import pandas as pd

# Define paths being the first one the directory with the reports per customer and the second one the CSV file with the fines compiled
main_folder = 'path_to_main_folder'
separate_csv_path = 'path_to_separate_csv_file.csv'
subfolders_txt_path = 'clients_analized.txt'


# Check if the required arguments are provided
if len(sys.argv) < 3:
    print("Please provide the main folder path and separate CSV file path as arguments.")
    exit(1)

# Get the main folder path and separate CSV file path from the command line arguments
main_folder = sys.argv[1]
separate_csv_path = sys.argv[2]

# List to store subfolder names
subfolder_names = []

try:
    # Load the separate CSV file
    all_records_df = pd.read_csv(separate_csv_path, header=0)

    # Normalize the column names
    all_records_df.columns = all_records_df.columns.str.strip().str.lower().str.replace(' ', '_')

    # Normalize the values in the dataframe
    all_records_df = all_records_df.apply(lambda x: x.str.strip() if x.dtype == "object" else x)

    # filtered_records_df2 = all_records_df[all_records_df['tenantid'] == 376822]
    # print(f"Filtered records sample2 {filtered_records_df2}")


    # print(f"all_records_df is {separate_csv_path}")
    # print(all_records_df.columns)
    # print(all_records_df)
    
except Exception as e:
    print(f"Error loading separate CSV file: {e}")
    exit(1)

# Iterate through each subfolder in the main folder
for subfolder_name in os.listdir(main_folder):
    subfolder_path = os.path.join(main_folder, subfolder_name)
    
    # Check if it is a directory
    if os.path.isdir(subfolder_path):
        try:
            subfolder_names.append(subfolder_name)  # Add subfolder name to the list

            # Assuming the company name or ID is in a column (e.g., 'company_name' or 'company_id')
            # Here we assume 'company_name' matches subfolder_name
            # Filter records in the separate CSV file for this specific company
            # print(f"OK UNTIL HERE {subfolder_name}")
            filtered_records_df = all_records_df[all_records_df['tenantid'] == int(subfolder_name)]
            # Check if filtered_records_df is empty
            if filtered_records_df.empty:
                print(f"No records found for {subfolder_name}. Skipping file creation.")
                continue  # Skip file creation if no records found
            # print(f"OK UNTIL NOW {subfolder_name}")
            # filtered_records_df = all_records_df[all_records_df.iloc[:, 11] == subfolder_name]
            # print(f"Filtered records sample {filtered_records_df}")
            # Define output path for filtered records inside the subfolder
            output_path = os.path.join(subfolder_path, 'fines_applied.csv')
            
            # Write the filtered records to the new CSV file inside the subfolder
            filtered_records_df.to_csv(output_path, index=False)
            
            print(f"Filtered records for {subfolder_name} written to {output_path}")
        except Exception as e:
            print(f"Error accessing subfolder {subfolder_path}: {e}")

# Write subfolder names to a .txt file
try:
    with open(subfolders_txt_path, 'w') as f:
        for subfolder_name in subfolder_names:
            f.write(subfolder_name + '\n')
    print(f"Subfolder names written to {subfolders_txt_path}")
except Exception as e:
    print(f"Error writing subfolder names to {subfolders_txt_path}: {e}")

print("Processing complete.")
