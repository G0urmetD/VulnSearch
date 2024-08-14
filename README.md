# VulnSearch
Fetch vulnerability database from cert-bund and able to search for keywords, instead of scrolling through the website.

```bash
         _   _       _       _____                     _     
        | | | |     | |     /  ___|                   | |    
        | | | |_   _| |_ __ \ `--.  ___  __ _ _ __ ___| |__  
        | | | | | | | | '_ \ `--. \/ _ \/ _` | '__/ __| '_ \ 
        \ \_/ / |_| | | | | /\__/ /  __/ (_| | | | (__| | | |
         \___/ \__,_|_|_| |_\____/ \___|\__,_|_|  \___|_| |_|

        Author: G0urmetD
        Version: 1.0
    
usage: main.py [-h] [-update] [-keywords KEYWORDS] [-keywords-file KEYWORDS_FILE] [-days DAYS]

Security Advisories Tool

options:
  -h, --help            show this help message and exit
  -update               Update the database with the latest advisories
  -keywords KEYWORDS    Comma separated list of keywords to search for
  -keywords-file KEYWORDS_FILE
                        Path to a file containing keywords to search for
  -days DAYS            Search for advisories in the last N days
```
