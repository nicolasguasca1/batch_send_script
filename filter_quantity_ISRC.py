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

                    # EXPERIMENTATION
                    # Step 1: Check if 'ISRC' is in the first row
                    header = next(csv_reader, None)
                    if header and 'ISRC' not in header:
                        print(
                            f"The following .csv file {csv_path} doesn't have ISRC references")
                        continue

                    # Get the index of 'ISRC' and 'Quantity' columns
                    isrc_index = header.index('ISRC')
                    quantity_index = header.index('Quantity')

                    z_value = 0
                    current_isrc = None

                    # Step 2: Iterate through the rows
                    for row in csv_reader:
                        isrc = row[isrc_index]
                        quantity = int(row[quantity_index])

                        if current_isrc is None:
                            current_isrc = isrc

                        if isrc != current_isrc:
                            mantra.append((current_isrc, z_value, dir_b))
                            if z_value > 1000:
                                print(f"{current_isrc}:{z_value}")
                            z_value = 0
                            current_isrc = isrc

                        z_value += quantity

                    # Append the last values
                    if current_isrc is not None:
                        mantra.append((current_isrc, z_value, dir_b))
                        if z_value > 1000:
                            print(f"{current_isrc}:{z_value}")

                    # Step 3: Create 'Mantra_above' and 'ISRCs_above.txt'
                    mantra_above = [(x, z, dir_name)
                                    for x, z, dir_name in mantra if z > 1000]
                    with open('ISRCs_above.txt', 'w') as isrc_file:
                        for x, z, dir_name in mantra_above:
                            isrc_file.write(f"{x}:{z}:{dir_name}\n")

                    # Step 5: Modify 'directories_above_threshold'
                    if len(mantra_above) > 0:
                        directories_above_threshold.append(dir_b)

                    # EXPERIMENTATION END
                    # Assuming 'Quantity' is in the first row
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
