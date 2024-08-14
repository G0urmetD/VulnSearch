import feedparser
from database import insert_advisory

RSS_URL = 'https://wid.cert-bund.de/content/public/securityAdvisory/rss'

def update_database():
    feed = feedparser.parse(RSS_URL)
    for entry in feed.entries:
        title = entry.title
        link = entry.link
        description = entry.description
        category = entry.category
        pubDate = entry.published
        insert_advisory(title, link, description, category, pubDate)
