import sqlite3
from datetime import datetime, timedelta
from colorama import Fore, Style

DB_NAME = 'security_advisories.db'

def create_connection():
    return sqlite3.connect(DB_NAME)

def initialize_database():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS advisories
                      (id INTEGER PRIMARY KEY,
                       title TEXT,
                       link TEXT,
                       description TEXT,
                       category TEXT,
                       pubDate TEXT,
                       wid TEXT)''')
    conn.commit()
    conn.close()

def insert_advisory(title, link, description, category, pubDate, wid):
    conn = create_connection()
    cursor = conn.cursor()
    
    # Convert pubDate to a datetime object and then to ISO format
    pubDate_obj = datetime.strptime(pubDate, '%a, %d %b %Y %H:%M:%S %Z')
    pubDate_iso = pubDate_obj.strftime('%Y-%m-%d %H:%M:%S')
    
    cursor.execute("SELECT * FROM advisories WHERE title=? AND pubDate=?", (title, pubDate_iso))
    if cursor.fetchone() is None:
        print(f"Inserting: {title}, WID: {wid}")  # Debug-Print
        cursor.execute('''INSERT INTO advisories (title, link, description, category, pubDate, wid)
                          VALUES (?, ?, ?, ?, ?, ?)''', (title, link, description, category, pubDate_iso, wid))
    conn.commit()
    conn.close()

def search_advisories(keywords, days=None):
    conn = create_connection()
    cursor = conn.cursor()
    
    date_limit = None
    if days:
        date_limit = datetime.utcnow() - timedelta(days=days)
    
    keyword_conditions = " OR ".join(["title LIKE ? OR description LIKE ?" for _ in keywords])
    sql_query = f"SELECT DISTINCT title, link, description, category, pubDate, wid FROM advisories WHERE ({keyword_conditions})"
    
    if date_limit:
        sql_query += " AND pubDate >= ?"
        params = [f"%{keyword}%" for keyword in keywords for _ in range(2)] + [date_limit.strftime('%Y-%m-%d %H:%M:%S')]
    else:
        params = [f"%{keyword}%" for keyword in keywords for _ in range(2)]
    
    cursor.execute(sql_query, params)
    results = cursor.fetchall()
    conn.close()
    
    return results

def cleanup_database():
    conn = create_connection()
    cursor = conn.cursor()
    
    date_limit = datetime.utcnow() - timedelta(days=180)
    cursor.execute("DELETE FROM advisories WHERE pubDate < ?", (date_limit.strftime('%Y-%m-%d %H:%M:%S'),))
    
    conn.commit()
    conn.close()

def add_wid_column():
    conn = create_connection()
    cursor = conn.cursor()
    
    try:
        cursor.execute("ALTER TABLE advisories ADD COLUMN wid TEXT")
        conn.commit()
    except sqlite3.OperationalError:
        print(f"{Fore.GREEN}[+]{Style.RESET_ALL} Column wid already exists.")
    
    conn.close()
