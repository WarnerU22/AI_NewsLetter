from newsfetcher import fetch_rss_articles
from summarizer import summarize_text
from utils.formatter import format_newsletter
from email_sender import send_email

def run_newsletter():
    rss_url = "https://rss.cnn.com/rss/cnn_topstories.rss"
    raw_articles = fetch_rss_articles(rss_url)

    summarized_articles = []
    for article in raw_articles:
        summary = summarize_text(article['summary'])  # Or article['title'] + article['summary']
        summarized_articles.append({
            'title': article['title'],
            'summary': summary,
            'link': article['link']
        })

    html = format_newsletter(summarized_articles)
    send_email("your@email.com", "📰 AI-Powered News Update", html)

if __name__ == "__main__":
    run_newsletter()
