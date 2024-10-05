import os.path
import gspread
from google.oauth2.service_account import Credentials
from google.oauth2.credentials import Credentials as Creds2
from gspread.exceptions import SpreadsheetNotFound, WorksheetNotFound
from googleapiclient.discovery import build
from google.auth.transport.requests import Request
import sys

#from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow


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
    "https://www.googleapis.com/auth/drive.readonly",
    "https://www.googleapis.com/auth/photoslibrary.readonly"
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
    #print(f"Values from {worksheet_name}!{data_range}:")
    #for row in data:
    #    print(row[0])  # Since it's a single column, access the first element
    
    return data

def get_shared_album_photos(album_id):
    try:
        creds = Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
        service = build('photoslibrary', 'v1', static_discovery=False, credentials=creds)

        results = service.mediaItems().search(body={'albumId': album_id}).execute()
        items = results.get('mediaItems', [])
        photo_urls = [item['baseUrl'] for item in items]
    except Exception as e:
        print(f"[Yakinton46App] An error occurred while fetching data: {e}")
        return 'no data'
    
    try:
        # Authenticate and get credentials
        flow = InstalledAppFlow.from_client_secrets_file(
            'path/to/your/client_secret.json', SCOPES)
        creds = flow.run_local_server(port=0)

        # Build the service
        service = build('photoslibrary', 'v1', credentials=creds)

        # Example: List albums
        results = service.albums().list(pageSize=10).execute()
        items = results.get('albums', [])

        if not items:
            print('No albums found.')
        else:
            print('Albums:')
            for item in items:
                print('{0} ({1})'.format(item['title'], item['id']))
            return items

    except Exception as e:
        print(f"[Yakinton46App] An error occurred while fetching data: {e}")
        return 'no data for my dear!'
    return photo_urls


# from google_photos_album_test.py
def authenticate_google_photos():
    """
    Authenticate the user and return the Google Photos service.
    """
    creds = None
    # The file token.json stores the user's access and refresh tokens.
    if os.path.exists('token.json'):
        creds = Creds2.from_authorized_user_file('token.json', SCOPES)
    # If there are no valid credentials, perform the OAuth flow.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            try:
                creds.refresh(Request())
            except Exception as e:
                print(f"Error refreshing credentials: {e}")
                creds = None
        if not creds:
            try:
                flow = InstalledAppFlow.from_client_secrets_file(
                    'desktop_app_credentials.json', SCOPES)
                creds = flow.run_local_server(port=0)
            except Exception as e:
                print(f"Error during OAuth flow: {e}")
                sys.exit(1)
        # Save the credentials for future use
        with open('token.json', 'w') as token:
            token.write(creds.to_json())
    
    try:
        service = build('photoslibrary', 'v1', credentials=creds, static_discovery=False)
        return service
    except Exception as error:
        print(f'An error occurred while building the service: {error}')
        sys.exit(1)

def list_albums(service):
    """
    List all albums in the user's Google Photos library.
    Returns a list of albums with their names and IDs.
    """
    albums = []
    next_page_token = None

    while True:
        try:
            results = service.albums().list(
                pageSize=50,
                pageToken=next_page_token
            ).execute()
            items = results.get('albums', [])
            if not items:
                print('No albums found.')
                break
            for item in items:
                albums.append({'title': item.get('title'), 'id': item.get('id')})
            next_page_token = results.get('nextPageToken')
            if not next_page_token:
                break
        except Exception as error:
            print(f'An error occurred while listing albums: {error}')
            break

    return albums

def find_album_id(albums, target_album_title):
    """
    Find and return the album ID for the given album title.
    """
    for album in albums:
        if album['title'].lower() == target_album_title.lower():
            return album['id']
    return None

def get_media_items_in_album(service, album_id, page_size=50):
    """
    Retrieve media items from a specific album using its album ID.
    Returns a list of media items.
    """
    media_items = []
    next_page_token = None

    while True:
        try:
            request_body = {
                "albumId": album_id,
                "pageSize": page_size
            }
            results = service.mediaItems().search(body=request_body).execute()
            items = results.get('mediaItems', [])
            if not items:
                print('No media items found in the album.')
                break
            media_items.extend(items)
            next_page_token = results.get('nextPageToken')
            if not next_page_token:
                break
        except Exception as error:
            print(f'An error occurred while retrieving media items: {error}')
            break

    return media_items
