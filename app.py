from flask import Flask, render_template
import datetime
from google_api import get_sheet_data, get_shared_album_photos, authenticate_google_photos, list_albums, get_media_items_in_album, get_album_photos
from weather import get_weather
from news import get_news_feed

GOOGLE_ALBUM_ID = 'ABtMPp1Yjne0Jf6STId2gWrA_lpqotcRTBAvn6gdEqLqEVcHT2VmfkDOFe02FI4sPfNNcO48CNK8'
YNET_RSS_LINK = 'https://www.ynet.co.il/Integration/StoryRss1854.xml'
WALLA_RSS_LINK = 'https://rss.walla.co.il/feed/22'
RSS_LINK = YNET_RSS_LINK

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
    ## photos = get_shared_album_photos(GOOGLE_ALBUM_ID)
    photos = get_album_photos(GOOGLE_ALBUM_ID)
    print(f'photos:{photos}')

    weather = get_weather(city_id=294801, api_key='94fa85a6340b977f219b230f30fdf4b5')
    print(f'weather: {weather}')

    # News breaks
    news_feed = get_news_feed(RSS_LINK)
    #print(f'news_feed:{news_feed}')

    return render_template('index.html', 
                           time=time, 
                           date=date, 
                           messages=messages, 
                           todos=todos, 
                           photos=photos, 
                           weather=weather, 
                           news_feed=news_feed
                           )

if __name__ == '__main__':
    app.run(debug=True)


