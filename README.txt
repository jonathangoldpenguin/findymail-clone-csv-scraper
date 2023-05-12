Email Finder Script
This Python script uses a Flask API to find email addresses based on the input data from a CSV file. The input CSV file should contain three columns: full_name, domain, and company_size. The script calls the API for each row in the input CSV and writes the API results to an output CSV file.

Dependencies
Python 3.6 or higher
requests library
tqdm library
You can install the required libraries with the following command:

bash
Copy code
pip install requests tqdm
Usage
Set the api_url variable to the URL of your Flask API.
Set the input_csv variable to the filename of your input CSV file.
Set the output_csv variable to the desired filename for the output CSV file.
Run the script using Python:
bash
Copy code
python email_finder.py
The script reads the input CSV file and makes API calls for each row. It writes the results to the output CSV file, along with the number of API calls made for each row.

Code Explanation
The script contains the following functions:

count_rows(csv_file): Counts the number of rows in the input CSV file, excluding the header row.
api_call_function(api_url, full_name, domain, company_size): Calls the Flask API with the given parameters and returns the API result and the number of API calls made.
The script processes the input CSV file using the csv.DictReader class, which reads the file row by row and returns a dictionary for each row. The keys of the dictionary correspond to the column names in the header row.

The script appends two new columns to the output CSV file: API Result and API Calls. These columns store the API result for each row and the number of API calls made, respectively.

The tqdm library is used to display a progress bar during the processing of the input CSV file.

Error Handling
The script handles errors from the API by checking the HTTP status code of the response. If the status code is 200, the script processes the JSON data returned by the API. If the status code is 503 (Service Unavailable), the script returns an error message and zero API calls. For other status codes, the script returns a generic error message and zero API calls.

Output
After processing the input CSV file, the script prints a message indicating that the processing is complete and the results have been written to the output CSV file.