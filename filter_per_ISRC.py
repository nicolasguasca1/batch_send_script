import json
import os
import csv

import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--folder_to_filter', type=str,
                    help='Folder name of the attachments to filter')
args = parser.parse_args()

parent_directory = args.folder_to_filter
result = {}  # Nested dictionary to store the result


directories_above_threshold = []
files_with_one_row = []  # To store files with only one row

for dir_b in os.listdir(parent_directory):
    dir_b_path = os.path.join(parent_directory, dir_b)

    if os.path.isdir(dir_b_path):
        mantra = {}
        for filename in os.listdir(dir_b_path):
            if filename.endswith('.csv'):
                csv_path = os.path.join(dir_b_path, filename)

                with open(csv_path, 'r') as csv_file:
                    csv_reader = csv.reader(csv_file)

                    # Step 1: Check if 'ISRC' is in the first row
                    header = next(csv_reader, None)
                    if header and 'ISRC' not in header:
                        print(
                            f"The following .csv file {csv_path} doesn't have ISRC references")
                        continue

                    # Get the index of 'ISRC' and 'Quantity' columns
                    isrc_index = header.index('ISRC')
                    quantity_index = header.index('Quantity')

                    current_isrc = None
                    rows_processed = False  # To keep track if any rows were processed
                    num_rows = 0

                    # # Read and discard the first row (header row)
                    # next(csv_reader, None)
                    # Read the second row (if it exists)
                    second_row = next(csv_reader, None)
                    if second_row is not None:
                        # Step 2: Iterate through the rows
                        for row in csv_reader:
                            num_rows += 1
                            isrc = row[isrc_index]
                            quantity = int(row[quantity_index])

                            if current_isrc is None:
                                current_isrc = isrc

                            if isrc != current_isrc:
                                if current_isrc in mantra:  # Check if ISRC is already in mantra
                                    if rows_processed:  # Only reset count if rows were processed
                                        mantra[current_isrc][0] += quantity
                                    else:
                                        mantra[current_isrc] = [
                                            quantity, dir_b]
                                else:
                                    mantra[current_isrc] = [quantity, dir_b]

                                current_isrc = isrc

                            # # Add the quantity to the existing entry
                            # mantra[current_isrc][0] += quantity

                            rows_processed = True  # Mark that rows were processed
                    # if num_rows == 1:
                    #     files_with_one_row.append((dir_b, filename))
                        # if isrc != current_isrc:
                        #     # Update the dictionary value or create a new entry
                        #     if current_isrc in mantra:
                        #         mantra[current_isrc][0] += quantity
                        #     else:
                        #         mantra[current_isrc] = [quantity, dir_b]

                        #     current_isrc = isrc

                        # Update the dictionary for the last ISRC
                        if current_isrc is not None:
                            if current_isrc in mantra:  # Check if ISRC is already in mantra
                                if rows_processed:  # Only reset count if rows were processed
                                    mantra[current_isrc][0] += quantity
                                else:
                                    mantra[current_isrc] = [quantity, dir_b]
                            else:
                                mantra[current_isrc] = [quantity, dir_b]
                    else:
                        files_with_one_row.append((dir_b, filename))
                    # if current_isrc in mantra:
                    #     mantra[current_isrc][0] += quantity
                    # else:
                    #     mantra[current_isrc] = [quantity, dir_b]

                    # Step 3: Create 'Mantra_above' and 'ISRCs_above.txt'
                    mantra_above = [(x, quantity, dir_name)
                                    for x, (quantity, dir_name) in mantra.items() if quantity > 1000]
                    # print(mantra_above)
                    with open('ISRCs_above.txt', 'a') as isrc_file:  # Open in append mode
                        for x, quantity, dir_name in mantra_above:
                            isrc_file.write(f"{x}:{quantity}:{dir_name}\n")

                    # Step 5: Modify 'directories_above_threshold'
                    if len(mantra_above) > 0:
                        if dir_b not in result:
                            # Initialize inner dictionary if needed
                            result[dir_b] = {}
                        # Store the result for this folder and file
                        result[dir_b][filename] = mantra_above

                    # if len(mantra_above) > 0:
                    #     directories_above_threshold.append(dir_b)
                    #     # Store the result for this folder and file
                    #     result[dir_b] = {filename: mantra_above}
                    # if len(mantra_above) > 0:
                    #     directories_above_threshold.append(dir_b)

        # Step 6: Create 'directories_above.txt'
        with open('directories_above_ISRC.txt', 'w') as dir_file:
            for dir_name in directories_above_threshold:
                dir_file.write(f"{dir_name}\n")

        # Step 7: Create 'files_with_one_row.txt'
        with open('files_with_one_row.txt', 'w') as one_row_file:
            for dir_name, file_name in files_with_one_row:
                one_row_file.write(f"{dir_name}:{file_name}\n")

# Step 8: Create 'result.json'
with open('analysis_result.json', 'w') as result_file:
    json.dump(result, result_file, indent=4)

print("Directories with no rows:",
      files_with_one_row)
print("Directories with CSV files where the sum of quantity per 'ISRC' is above 1000:",
      mantra_above)
