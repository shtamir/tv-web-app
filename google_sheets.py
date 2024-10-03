import os.path
from google.oauth2 import service_account
from googleapiclient.discovery import build

# Open the file in read mode
with open('token.txt', 'r') as file:
    # Read the token from the file
    token = file.read().strip()

# Print the token
print(f'Token: {token}')

# Replace with your spreadsheet ID
SPREADSHEET_ID = token
SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']

def get_sheet_data(range_name):
    creds = None
    if os.path.exists('token.json'):
        creds = service_account.Credentials.from_service_account_file('credentials.json', scopes=SCOPES)
    else:
        # Implement authentication flow
        pass  # For brevity, assuming service account is used

    service = build('sheets', 'v4', credentials=creds)
    sheet = service.spreadsheets()

    result = sheet.values().get(spreadsheetId=SPREADSHEET_ID, range=range_name).execute()
    values = result.get('values', [])

    return values
