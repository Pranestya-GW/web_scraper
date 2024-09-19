import pandas as pd
import json
import os

def convert_to_excel(input_file, output_file):
    # Read the input file containing JSON data
    with open(input_file, 'r') as file:
        content = file.read()
    
    # Parse the JSON content
    try:
        json_data = json.loads(content)
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}")
        return
    
    # Convert the JSON data into a pandas DataFrame
    df = pd.DataFrame(json_data)
    
    # Save the DataFrame to an Excel file
    df.to_excel(output_file, index=False)
    print(f"Conversion complete. Data saved to {output_file}")

if __name__ == "__main__":
    # Define the input and output file paths
    input_file = 'logs.txt'  # The file where logs are downloaded
    output_file = 'logs_output.xlsx'  # Desired Excel output file name
    
    # Run the conversion
    if os.path.exists(input_file):
        convert_to_excel(input_file, output_file)
    else:
        print(f"File {input_file} does not exist.")
