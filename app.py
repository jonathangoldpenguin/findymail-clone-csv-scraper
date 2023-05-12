import csv
import requests
import time
from tqdm import tqdm  # Import tqdm for the loading bar

def count_rows(csv_file):
    with open(csv_file, 'r') as f:
        return sum(1 for row in f) - 1  # Subtract 1 to account for the header row

def api_call_function(api_url, full_name, domain, company_size):
    payload = {
        'full_name': full_name,
        'domain': domain,
        'company_size': company_size,
    }

    response = requests.post(api_url, json=payload)
    if response.status_code == 200:
        data = response.json()
        return data['message'], data['api_calls']
    elif response.status_code == 503:
        return 'API error (503 Service Unavailable)', 0
    else:
        return 'API error', 0

api_url = 'https://arcane-coast-03298.herokuapp.com/api/search/email'  # Replace with your Flask API URL

input_csv = 'input.csv'  # Replace with your input CSV filename
output_csv = 'output.csv'  # Replace with your desired output CSV filename

with open(input_csv, 'r') as infile, open(output_csv, 'w', newline='') as outfile:
    reader = csv.DictReader(infile)
    header = reader.fieldnames
    header.append('API Result')
    header.append('API Calls')  # Add a new column for the API call count

    writer = csv.DictWriter(outfile, fieldnames=header)
    writer.writeheader()

    total_rows = count_rows(input_csv)  # Call the function to count the rows in the input CSV

    for row in tqdm(reader, total=total_rows):  # Wrap the reader iterator with tqdm
        full_name = row['full_name']
        domain = row['domain']
        company_size = row['company_size']

        api_result, api_calls = api_call_function(api_url, full_name, domain, company_size)
        row['API Result'] = api_result
        row['API Calls'] = api_calls  # Add the API call count to the output row
        writer.writerow(row)

print("Processing complete. Results written to:", output_csv)