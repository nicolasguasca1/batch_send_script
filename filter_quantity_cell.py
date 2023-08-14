import os
import csv

import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--folder_to_filter', type=str,
                    help='Folder name of the attachments to filter')
args = parser.parse_args()

parent_directory = args.folder_to_filter

directories_above_threshold = []

for dir_b in os.listdir(parent_directory):
    dir_b_path = os.path.join(parent_directory, dir_b)

    if os.path.isdir(dir_b_path):
        mantra = []
        for filename in os.listdir(dir_b_path):
            if filename.endswith('.csv'):
                csv_path = os.path.join(dir_b_path, filename)

                with open(csv_path, 'r') as csv_file:
                    csv_reader = csv.DictReader(csv_file)

                    # Check if the file is empty before trying to read the first row
                    try:
                        first_row = next(csv_reader)
                    except StopIteration:
                        continue  # Move to the next file

                    if 'Quantity' in first_row and int(first_row['Quantity']) > 1000:
                        directories_above_threshold.append(dir_b)
                        break  # No need to check other files in this directory

print("Directories with CSV files where 'Quantity' is above 1000:",
      directories_above_threshold)
