import pandas as pd
import json
import re
import os

def convert_to_excel(input_file, output_file):
    # Read the input file
    with open(input_file, 'r') as file:
        content = file.read()
    
    # Extract the relevant lines that contain JSON data
    lines_with_data = re.findall(r'\{.*?\}', content)
    
    # Convert the extracted JSON data into a list of dictionaries
    data = []
    for line in lines_with_data:
        try:
            data.append(json.loads(line))
        except json.JSONDecodeError:
            continue  # Skip any lines that don't contain valid JSON
    
    # Convert the list of dictionaries into a DataFrame
    df = pd.DataFrame(data)
    
    # Save the DataFrame to an Excel file
    df.to_excel(output_file, index=False)

if __name__ == "__main__":
    # Input and output paths within your GitHub repo
    input_file = os.path.join(os.getenv('GITHUB_WORKSPACE'), 'logs.txt')  # Assuming logs.txt is downloaded to the repo
    output_file = os.path.join(os.getenv('GITHUB_WORKSPACE'), 'logs_output.xlsx')  # Excel output in the same repo directory
    
    # Check if the input file exists
    if not os.path.exists(input_file):
        print(f"File {input_file} does not exist.")
        exit(1)
    
    # Run the conversion
    convert_to_excel(input_file, output_file)
    print(f"Conversion complete. Data has been saved to {output_file}.")
