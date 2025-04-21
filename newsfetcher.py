import feedparser

def fetch_rss_articles(feed_url, limit=5):
    feed = feedparser.parse(feed_url)
    articles = []

    for entry in feed.entries[:limit]:
        article = {
            'title': entry.title,
            'link': entry.link,
            'summary': entry.summary
        }
        articles.append(article)
    
    return articles
