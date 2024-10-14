import os
import csv
import glob

# Get the current directory
current_directory = os.getcwd()

# Find all .txt files in the current directory
txt_files = glob.glob(os.path.join(current_directory, '*.txt'))

# Prepare the output CSV file
output_csv = 'output.csv'

# Open the CSV file for writing
with open(output_csv, mode='w', newline='', encoding='utf-8') as csv_file:
    writer = csv.writer(csv_file)
    
    # Write the header row
    writer.writerow(['text'])
    
    # Process each text file
    for file_path in txt_files:
        with open(file_path, 'r', encoding='utf-8') as txt_file:
            # Process each line in the text file
            for line in txt_file:
                # Strip whitespace and save to CSV
                line = line.strip()
                if line:  # Only write non-empty lines
                    writer.writerow([line])

print(f"Processed {len(txt_files)} files and saved to '{output_csv}'.")
