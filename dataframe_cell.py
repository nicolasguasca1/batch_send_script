import argparse
import os
import pandas as pd
import json

# Path to your credentials JSON file downloaded from the Google Cloud Console
credentials_path = '/Users/nicolasguascasantamaria/Desktop/RevAPIS/extRepo/gmailAPI/credenciales_drive.json'

parser = argparse.ArgumentParser()
parser.add_argument('--folder_to_filter', type=str,
                    help='Folder name of the attachments to filter')
args = parser.parse_args()

content_folder = args.folder_to_filter

# List to store records
data_dict = {}
directories_above_threshold = []
entIds_analized = []
directories_below_threshold = []
directories_above_threshold_count = 0
directories_below_threshold_count = 0
quantity_threshold = 1000
quantity_threshold_tiktok = 10000
quantities_concerning = {}
directory_name = os.path.basename(content_folder)
output_compiled_directory = f"{directory_name}_Compiled"
entIds_analized.append(pd.Timestamp.now())
# Iterate over all files in the 'Content' folder
for root, _, files in os.walk(content_folder):
    dir_b_path = os.path.join(content_folder, root)
    directory_data = {}
    quantity_per_concerning_company = 0
    entIds_analized.append(os.path.basename(root))
    
    # Append to entIds_analized the timestamp and date of the analysis based on the system timestamp 

    

    for file in files:
        filtered_dfs = []
        filtered_rows = None
        filtered_rows2 = None
        filtered_rows3 = None
        filtered_rows4 = None
        if file.endswith('.csv'):
            
            csv_file_path = os.path.join(dir_b_path, file)
            with open(csv_file_path, 'r') as csv_file:
                quantity_above_per_file = 0
                df = pd.read_csv(csv_file)
                # Check for lines where 'Quantity' column is 1000 or more
            if 'Quantity' in df.columns:
                filtered_rows = df[df['Quantity'] >= quantity_threshold]
                if filtered_rows is not None:
                    output_file_compiled = "Spotify_Rows_Above_1000.csv"
                    quantity_above_per_file = filtered_rows['Quantity'].sum()

                    filtered_dfs.append(filtered_rows)
                    file_data = []
                    for index, row in filtered_rows.iterrows():
                        record = {
                            # Assuming 'ISRC' is the column name
                            'ISRC': row['ISRC'],
                            'SpoQuantity': row['Quantity']
                        }
                        file_data.append(record)
                    if file_data:
                        directory_data[file] = file_data
                        quantity_per_concerning_company += quantity_above_per_file
                
            elif 'tkt_quantity' in df.columns:
                # ################### Case for Tikt

                filtered_rows2 = df[(df['tkt_quantity'] >= quantity_threshold_tiktok) & (df['removal_reason'] == 'Bot Creation')]
                # USED TO BE:
                # filtered_rows2 = df[df['tkt_quantity'] >= quantity_threshold_tiktok]
                if filtered_rows2 is not None:
                    output_file_compiled = "Tiktok_Rows_Above_10000.csv"
                    quantity_above_per_file = filtered_rows2['tkt_quantity'].sum()

                    filtered_dfs.append(filtered_rows2)
                    file_data2 = []
                    for index, row in filtered_rows2.iterrows():
                        record = {
                            # Assuming 'ISRC' is the column name
                            'ISRC': row['ISRC'],
                            'tkt_quantity': row['tkt_quantity']
                        }
                        file_data2.append(record)
                    if file_data2:
                        directory_data[file] = file_data2
                        quantity_per_concerning_company += quantity_above_per_file

            elif 'pndra_quantity' in df.columns:
                # ################### Case for Tikt

                filtered_rows3 = df[df['pndra_quantity'] >= quantity_threshold]
                if filtered_rows3 is not None:
                    output_file_compiled = "Pandora_Rows_Above_1000.csv"
                    quantity_above_per_file = filtered_rows3['pndra_quantity'].sum()

                    filtered_dfs.append(filtered_rows3)
                    file_data3 = []
                    for index, row in filtered_rows3.iterrows():
                        record = {
                            # Assuming 'ISRC' is the column name
                            'ISRC': row['ISRC'],
                            'pndra_quantity': row['pndra_quantity']
                        }
                        file_data3.append(record)
                    if file_data3:
                        directory_data[file] = file_data3
                        quantity_per_concerning_company += quantity_above_per_file
            
            elif 'deezer_quantity' in df.columns:
                # ################### Case for Tikt

                filtered_rows4 = df[df['deezer_quantity'] >= quantity_threshold]
                if filtered_rows4 is not None:
                    output_file_compiled = "Deezer_Rows_Above_1000.csv"
                    quantity_above_per_file = filtered_rows4['deezer_quantity'].sum()

                    filtered_dfs.append(filtered_rows4)
                    file_data4 = []
                    for index, row in filtered_rows4.iterrows():
                        record = {
                            # Assuming 'ISRC' is the column name
                            'ISRC': row['ISRC'],
                            'deezer_quantity': row['deezer_quantity']
                        }
                        file_data4.append(record)
                    if file_data4:
                        directory_data[file] = file_data4
                        quantity_per_concerning_company += quantity_above_per_file
            
            else:
                print(f"Neither Quantity, tkt_quantity, pndra_quantity or deezer_quantity found in {csv_file_path}. Moving on to the next file.")

                continue

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
    with open('directories_above_1000_spo.txt', 'w') as dir_file:
        for dir_name in directories_above_threshold:
            dir_file.write(f"{dir_name}\n")
    with open('directories_below_1000_spo.txt', 'w') as dir_file:
        for dir_name in directories_below_threshold:
            dir_file.write(f"{dir_name}\n")
    with open('enterprises_analized_from_dataframe_cell.txt', 'w') as dir_file:
        for dir_name in entIds_analized:
            dir_file.write(f"{dir_name}\n")

sorted_concerning = sorted(
    quantities_concerning.items(), key=lambda x: x[1], reverse=True)
# THE FOLLOWING NEED TO BE ADJUSTED TO THE NUMBER OF COMPANIES WITH ALARMING NUMBERS
top_arrays = sorted_concerning[:directories_above_threshold_count]
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
print("The top directories with the most AS with the scheme ['EntID',total_sum] are the following:",
      top_arrays)

# print('File ID on Drive:', uploaded_file['id'])
