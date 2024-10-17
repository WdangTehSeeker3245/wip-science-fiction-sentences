import os
import pandas as pd

def append_csv_files(directory, output_file):
  """Appends all CSV files in a given directory into a single output CSV file.

  Args:
    directory: The directory containing the CSV files.
    output_file: The name of the output CSV file.
  """

  # Get a list of all CSV files in the directory
  csv_files = [f for f in os.listdir(directory) if f.endswith('.csv')]

  # Create an empty DataFrame to store the concatenated data
  df = pd.DataFrame()

  # Iterate over each CSV file and append its data to the DataFrame
  for file in csv_files:
    file_path = os.path.join(directory, file)
    temp_df = pd.read_csv(file_path)
    df = pd.concat([df, temp_df], ignore_index=True)

  # Save the concatenated DataFrame to the output CSV file
  df.to_csv(output_file, index=False)

# Get the current working directory
current_directory = os.getcwd()

# Call the function to append the CSV files
append_csv_files(current_directory, "science_fiction_sentences.csv")