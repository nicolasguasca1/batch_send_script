import argparse
import os
import pandas as pd
import json
import csv

import pickle
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from google_auth_oauthlib.flow import InstalledAppFlow

# Path to your credentials JSON file downloaded from the Google Cloud Console
credentials_path = '/Users/nicolasguascasantamaria/Desktop/RevAPIS/extRepo/gmailAPI/credenciales_drive.json'

parser = argparse.ArgumentParser()
parser.add_argument('--folder_to_filter', type=str,
                    help='Folder name of the attachments to filter')
args = parser.parse_args()

content_folder = args.folder_to_filter

# # Create credentials flow and load existing token if available
# flow = InstalledAppFlow.from_client_secrets_file(
#     credentials_path, ['https://www.googleapis.com/auth/drive'])
# if os.path.exists('token.pickle'):
#     creds = pickle.load(open('token.pickle', 'rb'))
# else:
#     creds = flow.run_local_server(port=0)

# # Save the credentials token
# with open('token.pickle', 'wb') as token:
#     pickle.dump(creds, token)

# # Create a Google Drive API service
# service = build('drive', 'v3', credentials=creds)

# List to store records
data_dict = {}
directories_above_threshold = []
directories_below_threshold = []
directories_above_threshold_count = 0
directories_below_threshold_count = 0
quantity_threshold = 1000
quantities_concerning = {}
directory_name = os.path.basename(content_folder)
output_compiled_directory = f"{directory_name}_Compiled"
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
            # Create the complete path for the output CSV file
            output_csv_path = os.path.join(root, output_file_compiled)
            # Concatenate all filtered DataFrames into a single DataFrame
            result_df = pd.concat(filtered_dfs, ignore_index=True)
            # Write the concatenated DataFrame to a CSV file
            result_df.to_csv(output_csv_path, index=False)
    if directory_data:
        data_dict[root] = directory_data
        directories_above_threshold_count += 1
        directories_above_threshold.append(os.path.basename(root))
        quantities_concerning[os.path.basename(
            root)] = quantity_per_concerning_company
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

sorted_concerning = sorted(
    quantities_concerning.items(), key=lambda x: x[1], reverse=True)
top_5_arrays = sorted_concerning[:5]
# Save the records to a JSON file in valid JSON format
output_file = 'filtered_cell_records.json'
output_file_sum = 'concerning_records_sum.csv'
with open(output_file, 'w') as json_file:
    json.dump(data_dict, json_file, indent=4)

# Convert the dictionary to a DataFrame
df3 = pd.DataFrame(list(quantities_concerning.items()),
                   columns=['EntId', 'Total sum'])

# Save the DataFrame to a CSV file
df3.to_csv(output_file_sum, index=False)

# # Upload the CSV file to Google Drive
# file_metadata = {'name': 'Concerning_records_sum_'+os.path.basename(content_folder)+'.csv'}
# media = MediaFileUpload('Concerning_records_sum_'+os.path.basename(content_folder)+'.csv', mimetype='text/csv')
# uploaded_file = service.files().create(body=file_metadata, media_body=media, fields='id').execute()


print(f"Filtered records saved to '{output_file}'")
print("Directories with CSV files where 'Quantity' is above 1000:",
      directories_above_threshold_count)
print("Directories with CSV files where 'Quantity' is below 1000:",
      directories_below_threshold_count)
print("The top five directories with the most AS with the scheme ['EntID',total_sum] are the following:",
      top_5_arrays)

# print('File ID on Drive:', uploaded_file['id'])
