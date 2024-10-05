import os.path
import gspread
from google.oauth2.service_account import Credentials
from gspread.exceptions import SpreadsheetNotFound, WorksheetNotFound
import sys

# Open the file in read mode
with open('google_sheets_id.txt', 'r') as file:
    # Read the token from the file
    google_sheets_id = file.read().strip()

# Replace with your spreadsheet ID
SPREADSHEET_ID = google_sheets_id
# Define the scope
# SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']
SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets.readonly",
    "https://www.googleapis.com/auth/drive.readonly"
]

# Path to your service account key file
SERVICE_ACCOUNT_FILE = 'service_account_credentials.json'

def get_sheet_data(worksheet_name, data_range='!A:A'):
    creds = None
    if os.path.exists(SERVICE_ACCOUNT_FILE):
        print(f'\n=================\n[TAMIR] path ok\n=================\n')

        # Create credentials using the service account file and defined scopes
        creds = Credentials.from_service_account_file(
            SERVICE_ACCOUNT_FILE,
            scopes=SCOPES
        )

        print(f'\n=================\n[TAMIR] creds: {creds}\n=================\n')
    else:
        # Implement authentication flow
        pass  # For brevity, assuming service account is used

    # --------------
    # Authorize the client
    client = gspread.authorize(creds)

    # Open the Google Sheet by name or by URL
    # By name:
    # sheet = client.open("Your Google Sheet Name").sheet1

    # By URL:
    sheet_url = "https://docs.google.com/spreadsheets/d/1n2mTOacP_UV4zBE10xHy5d3LobNDGkNiXsvH33Trejo/edit#gid=0"
    

    print (f'Party time')
    # Open the Google Sheet by name
    spreadsheet_name = "messageList"  # Replace with your spreadsheet name
    try:
        # Open the Google Sheet by name
        spreadsheet = client.open(spreadsheet_name)
    except SpreadsheetNotFound:
        print(f"Error: Spreadsheet named '{spreadsheet_name}' not found.")
        return 'no spread sheet'

    # worksheet_name - Name of the specific sheet/tab
    try:
        worksheet = spreadsheet.worksheet(worksheet_name)
    except WorksheetNotFound:
        print(f"Worksheet '{worksheet_name}' not found in '{spreadsheet_name}'.")
        return 'no worksheet'    

    try:
        # Get values from the specified range
        data = worksheet.get(data_range)
    except Exception as e:
        print(f"An error occurred while fetching data: {e}")
        return 'no data'


    # Print the retrieved data
    print(f"Values from {worksheet_name}!{data_range}:")
    for row in data:
        print(row[0])  # Since it's a single column, access the first element
    
    return data
