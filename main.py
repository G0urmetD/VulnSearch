import argparse
from colorama import Fore, Style
from database import initialize_database, search_advisories, cleanup_database
from rss_feed import update_database

def load_keywords_from_file(file_path):
    with open(file_path, 'r') as f:
        keywords = [line.strip() for line in f.readlines()]
    return keywords

if __name__ == "__main__":
    
    # ASCII banner
    print(r"""

         _   _       _       _____                     _     
        | | | |     | |     /  ___|                   | |    
        | | | |_   _| |_ __ \ `--.  ___  __ _ _ __ ___| |__  
        | | | | | | | | '_ \ `--. \/ _ \/ _` | '__/ __| '_ \ 
        \ \_/ / |_| | | | | /\__/ /  __/ (_| | | | (__| | | |
         \___/ \__,_|_|_| |_\____/ \___|\__,_|_|  \___|_| |_|

        Author: G0urmetD
        Version: 1.0
    """)
    
    parser = argparse.ArgumentParser(description="Vulnerability Search Tool")
    
    parser.add_argument("-update", action="store_true", help="Update the database with the latest advisories")
    parser.add_argument("-keywords", help="Comma separated list of keywords to search for")
    parser.add_argument("-keywords-file", help="Path to a file containing keywords to search for")
    parser.add_argument("-days", type=int, help="Search for advisories in the last N days")
    
    args = parser.parse_args()
    
    # Initialize database on first run
    initialize_database()
    
    if args.update:
        print(f"{Fore.YELLOW}[~]{Style.RESET_ALL} Updating Database...")
        update_database()
        print(f"{Fore.GREEN}[+]{Style.RESET_ALL} Database updated.")
    
    if args.keywords or args.keywords_file:
        if args.keywords:
            keywords = args.keywords.split(",")
        elif args.keywords_file:
            keywords = load_keywords_from_file(args.keywords_file)
        
        results = search_advisories(keywords, days=args.days)
        for result in results:
            print(f"[{result[3]}] {result[0]}")
            print(f"Link: {result[1]}")
            print(f"Description: {result[2]}")
            print(f"initial Date: {result[4]}")
            print("\n")
    
    # Clean up old records
    cleanup_database()
