import argparse
import textwrap
from colorama import Fore, Style
from database import initialize_database, search_advisories, cleanup_database, add_wid_column, display_all_entries
from rss_feed import update_database
from tabulate import tabulate

def load_keywords_from_file(file_path):
    with open(file_path, 'r') as f:
        keywords = [line.strip() for line in f.readlines()]
    return keywords

def wrap_text(text, width=160):
    return "\n".join(textwrap.wrap(text, width=width))

def filter_results_by_status(results, status_filter):
    return [result for result in results if ("NEU" in result[0] and status_filter == "Neu") or ("UPDATE" in result[0] and status_filter == "Update") or status_filter is None]

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
        Version: 1.4
    """)
    
    parser = argparse.ArgumentParser(description="Vulnerability Search Tool")
    
    parser.add_argument("-update", action="store_true", help="Update the database with the latest advisories")
    parser.add_argument("-keywords", help="Comma separated list of keywords to search for")
    parser.add_argument("-keywords-file", help="Path to a file containing keywords to search for")
    parser.add_argument("-days", type=int, help="Search for advisories in the last N days")
    parser.add_argument("-init", action='store_true', help="Switch parameter to initialiaze the database columns.")
    parser.add_argument("-status", choices=["Neu", "Update"], help="Search parameter to only output for New or Updated vulnerabilities. Not required.")
    parser.add_argument("-checkdb", action='store_true', help="Displays database entries.")
    
    args = parser.parse_args()
    
    # Initialize database on first run
    initialize_database()

    if args.checkdb:
        display_all_entries()
    
    if args.init:
        add_wid_column()
    
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

        # Filter results based on the -status parameter
        filtered_results = filter_results_by_status(results, args.status)
        
        table = []
        for result in filtered_results:
            status = "Neu" if "NEU" in result[0] else "Update"
            wrapped_description = wrap_text(result[2], width=50)
            wrapped_title = wrap_text(result[0], width=30)
            wrapped_link = wrap_text(result[1], width=60)
            wrapped_link = result[1]
            table.append([result[3], status, wrapped_title, wrapped_description, wrapped_link, result[4], result[5]])
        
        headers = ["Severity", "Status", "Name", "Description", "Link", "Initial Date", "WID Nummer"]
        print(tabulate(table, headers, tablefmt="grid"))
    
    # Clean up old records
    cleanup_database()
