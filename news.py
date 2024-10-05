import feedparser

def get_news_feed(rss_url):
    feed = feedparser.parse(rss_url)
    
    #for f in feed:
    for e in feed.entries:
        print(f'feed:{e}')

    #, 'time': entry.pubDate
    news_items = [{'time': entry.published, 'title': entry.title, 'link': entry.link} for entry in feed.entries[:10]]
    return news_items
