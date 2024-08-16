import feedparser
from urllib.parse import urlparse, parse_qs
from database import insert_advisory

RSS_URL = 'https://wid.cert-bund.de/content/public/securityAdvisory/rss'

def extract_wid_from_link(link):
    parsed_url = urlparse(link)
    wid_number = parse_qs(parsed_url.query).get('name', [None])[0]
    return wid_number

def update_database():
    feed = feedparser.parse(RSS_URL)
    for entry in feed.entries:
        title = entry.title
        link = entry.link
        description = entry.description
        category = entry.category
        pubDate = entry.published
        
        # extract WID-Nummer
        wid_number = extract_wid_from_link(link)
        
        insert_advisory(title, link, description, category, pubDate, wid_number)
