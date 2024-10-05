from flask import Flask, render_template
import datetime
from google_api import get_sheet_data, get_shared_album_photos, authenticate_google_photos, list_albums, get_media_items_in_album


app = Flask(__name__)

@app.route('/')
def index():
    now = datetime.datetime.now()
    time = now.strftime("%H:%M")
    date = now.strftime("%A, %d %B %Y")

    # Fetch team messages
    messages = get_sheet_data('Messages','A:A')  # Assuming messages are in 'Messages' sheet, column A
    messages = [msg[0] for msg in messages if msg]

    # Fetch to-do list
    todos = get_sheet_data('ToDo','A:A')  # Assuming to-dos are in 'ToDo' sheet, column A
    todos = [todo[0] for todo in todos if todo]

    # Inside index() function
    ## photos = get_shared_album_photos('AF1QipPX6rR7jKeOSwnoMXmHxfdkfVFBAejFvMFpQdug')

    # ===========================
    # test start
    # ===========================
     # Authenticate and build the service
    service = authenticate_google_photos()

    # Step 1: List all albums
    print("Fetching your albums...")
    albums = list_albums(service)
    if not albums:
        print("No albums available.")
        return

    print("\nYour Albums:")
    for idx, album in enumerate(albums, start=1):
        print(f"{idx}. {album['title']} (ID: {album['id']})")

    # Step 2: Specify the album you want to access
    #target_album_title = input("\nEnter the exact name of the album you want to access: ").strip()
    #album_id = find_album_id(albums, target_album_title)

    album_id = 'ABtMPp1Yjne0Jf6STId2gWrA_lpqotcRTBAvn6gdEqLqEVcHT2VmfkDOFe02FI4sPfNNcO48CNK8'

    #if not album_id:
    #    print(f"Album titled '{target_album_title}' not found.")
    #    return

    #print(f"\nAccessing Album: {target_album_title} (ID: {album_id})")

    # Step 3: Retrieve media items from the specified album
    media_items = get_media_items_in_album(service, album_id)
    photos = []
    if media_items:
        #print(f"\nMedia Items in '{target_album_title}':")
        for item in media_items:
            filename = item.get('filename')
            base_url = item.get('baseUrl')
            media_type = item.get('mimeType')
            #print(f"Filename: {filename}, Type: {media_type}, URL: {base_url}=w2048-h1024")
            photos.append(base_url)
    else:
        print("No media items found in the specified album.")

    # ===========================
    # test end
    # ===========================

    return render_template('index.html', time=time, date=date, messages=messages, todos=todos, photos=photos)

if __name__ == '__main__':
    app.run(debug=True)


