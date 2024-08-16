# VulnSearch
Fetch vulnerability database from cert-bund and able to search for keywords, instead of scrolling through the website.

# Example
```bash
python3 main.py -keywords docker,zabbix,windows            


         _   _       _       _____                     _     
        | | | |     | |     /  ___|                   | |    
        | | | |_   _| |_ __ \ `--.  ___  __ _ _ __ ___| |__  
        | | | | | | | | '_ \ `--. \/ _ \/ _` | '__/ __| '_ \ 
        \ \_/ / |_| | | | | /\__/ /  __/ (_| | | | (__| | | |
         \___/ \__,_|_|_| |_\____/ \___|\__,_|_|  \___|_| |_|

        Author: G0urmetD
        Version: 1.2.1
    
+------------+----------+------------------------------+----------------------------------------------------+------------------------------------------+---------------------+-------------------+
| Severity   | Status   | Name                         | Description                                        | Link                                     | Initial Date        | WID Nummer        |
+============+==========+==============================+====================================================+==========================================+=====================+===================+
| kritisch   | Neu      | [NEU] [kritisch] Microsoft   | Ein Angreifer kann mehrere Schwachstellen in       | https://wid.cert-bund.de/portal/wid/secu | 2024-08-14 09:38:39 | WID-SEC-2024-1835 |
|            |          | Windows: Mehrere             | Microsoft Windows, Microsoft Windows 10, Microsoft | rityadvisory?name=WID-SEC-2024-1835      |                     |                   |
|            |          | Schwachstellen               | Windows 11, Microsoft Windows Server, Microsoft    |                                          |                     |                   |
|            |          |                              | Windows Server 2012, Microsoft Windows Server 2012 |                                          |                     |                   |
|            |          |                              | R2, Microsoft Windows Server 2016, Microsoft       |                                          |                     |                   |
|            |          |                              | Windows Server 2019 und Microsoft Windows Server   |                                          |                     |                   |
|            |          |                              | 2022 ausnutzen, um beliebigen Programmcode         |                                          |                     |                   |
|            |          |                              | auszuführen, beliebigen Programmcode mit           |                                          |                     |                   |
|            |          |                              | Administratorrechten auszuführen, seine            |                                          |                     |                   |
|            |          |                              | Privilegien zu erweitern, Informationen            |                                          |                     |                   |
|            |          |                              | offenzulegen, einen Denial of Service Zustand      |                                          |                     |                   |
|            |          |                              | herbeizuführen oder Sicherheitsvorkehrungen zu     |                                          |                     |                   |
|            |          |                              | umgehen.                                           |                                          |                     |                   |
+------------+----------+------------------------------+----------------------------------------------------+------------------------------------------+---------------------+-------------------+
| mittel     | Neu      | [NEU] [UNGEPATCHT] [mittel]  | Ein lokaler Angreifer kann eine Schwachstelle in   | https://wid.cert-bund.de/portal/wid/secu | 2024-08-13 09:33:35 | WID-SEC-2024-1813 |
|            |          | Microsoft Windows:           | Microsoft Windows 10, Microsoft Windows 11,        | rityadvisory?name=WID-SEC-2024-1813      |                     |                   |
|            |          | Schwachstelle ermöglicht     | Microsoft Windows Server 2016 und Microsoft        |                                          |                     |                   |
|            |          | Denial of Service            | Windows Server 2019 ausnutzen, um einen Denial of  |                                          |                     |                   |
|            |          |                              | Service Angriff durchzuführen.                     |                                          |                     |                   |
+------------+----------+------------------------------+----------------------------------------------------+------------------------------------------+---------------------+-------------------+
| hoch       | Neu      | [NEU] [hoch] Zabbix: Mehrere | Ein Angreifer kann mehrere Schwachstellen in       | https://wid.cert-bund.de/portal/wid/secu | 2024-08-12 10:35:28 | WID-SEC-2024-1811 |
|            |          | Schwachstellen               | Zabbix ausnutzen, um Informationen offenzulegen,   | rityadvisory?name=WID-SEC-2024-1811      |                     |                   |
|            |          |                              | Dateien zu manipulieren, Sicherheitsmaßnahmen zu   |                                          |                     |                   |
|            |          |                              | umgehen, einen Denial-of-Service-Zustand zu        |                                          |                     |                   |
|            |          |                              | verursachen oder beliebigen Code auszuführen.      |                                          |                     |                   |
+------------+----------+------------------------------+----------------------------------------------------+------------------------------------------+---------------------+-------------------+
| mittel     | Update   | [UPDATE] [mittel] docker:    | Ein Angreifer kann mehrere Schwachstellen in       | https://wid.cert-bund.de/portal/wid/secu | 2024-08-12 10:11:30 | WID-SEC-2023-1183 |
|            |          | Mehrere Schwachstellen       | docker ausnutzen, um Sicherheitsmaßnahmen zu       | rityadvisory?name=WID-SEC-2023-1183      |                     |                   |
|            |          |                              | umgehen, vertrauliche Informationen offenzulegen,  |                                          |                     |                   |
|            |          |                              | einen Denial-of-Service-Zustand auszulösen, seine  |                                          |                     |                   |
|            |          |                              | Privilegien zu erweitern und Daten zu              |                                          |                     |                   |
|            |          |                              | manipulieren.                                      |                                          |                     |                   |
+------------+----------+------------------------------+----------------------------------------------------+------------------------------------------+---------------------+-------------------+
| hoch       | Update   | [UPDATE] [hoch] docker:      | Ein entfernter Angreifer kann mehrere              | https://wid.cert-bund.de/portal/wid/secu | 2024-08-12 10:11:26 | WID-SEC-2024-0272 |
|            |          | Mehrere Schwachstellen       | Schwachstellen in Docker ausnutzen, um seine       | rityadvisory?name=WID-SEC-2024-0272      |                     |                   |
|            |          |                              | Privilegien zu erhöhen, einen Denial-of-Service-   |                                          |                     |                   |
|            |          |                              | Zustand zu verursachen, vertrauliche Informationen |                                          |                     |                   |
|            |          |                              | offenzulegen, Sicherheitsmaßnahmen zu umgehen oder |                                          |                     |                   |
|            |          |                              | Dateien zu manipulieren.                           |                                          |                     |                   |
+------------+----------+------------------------------+----------------------------------------------------+------------------------------------------+---------------------+-------------------+
| hoch       | Update   | [UPDATE] [hoch] Zabbix:      | Ein Angreifer kann mehrere Schwachstellen in       | https://wid.cert-bund.de/portal/wid/secu | 2024-08-16 08:03:23 | WID-SEC-2024-1811 |
|            |          | Mehrere Schwachstellen       | Zabbix ausnutzen, um Informationen offenzulegen,   | rityadvisory?name=WID-SEC-2024-1811      |                     |                   |
|            |          |                              | Dateien zu manipulieren, Sicherheitsmaßnahmen zu   |                                          |                     |                   |
|            |          |                              | umgehen, einen Denial-of-Service-Zustand zu        |                                          |                     |                   |
|            |          |                              | verursachen oder beliebigen Code auszuführen.      |                                          |                     |                   |
+------------+----------+------------------------------+----------------------------------------------------+------------------------------------------+---------------------+-------------------+

```

# Usage
```bash
python3 main.py -update/-init # updates the datase and/or initialize the database columns
python3 main.py -keywords docker,zabbix # searches for entries with the keywords 'docker' and 'zabbix'
python3 main.py -keywords docker,zabbix -days 5 # searches for entries with the keywords 'docker' and 'zabbix' in the last 5 days

python3 main.py -keywords-file words.txt # searches for keywords out of the txt file
python3 main.py -keywords-file words.txt -days 5 # searches for keywords out of the txt file in the last 5 days
```

```bash
         _   _       _       _____                     _     
        | | | |     | |     /  ___|                   | |    
        | | | |_   _| |_ __ \ `--.  ___  __ _ _ __ ___| |__  
        | | | | | | | | '_ \ `--. \/ _ \/ _` | '__/ __| '_ \ 
        \ \_/ / |_| | | | | /\__/ /  __/ (_| | | | (__| | | |
         \___/ \__,_|_|_| |_\____/ \___|\__,_|_|  \___|_| |_|

        Author: G0urmetD
        Version: 1.2.1
    
usage: main.py [-h] [-update] [-keywords KEYWORDS] [-keywords-file KEYWORDS_FILE] [-days DAYS] [-init]

Vulnerability Search Tool

options:
  -h, --help            show this help message and exit
  -update               Update the database with the latest advisories
  -keywords KEYWORDS    Comma separated list of keywords to search for
  -keywords-file KEYWORDS_FILE
                        Path to a file containing keywords to search for
  -days DAYS            Search for advisories in the last N days
  -init                 Switch parameter to initialiaze the database columns.
```

# Automation
To automate the database update process, just use a cronjob and a small shell script. And do not forget to make the script executable.

```shell
#!/bin/bash
python3 main.py -update
```

Then create a cronjob to run every 2 hours:
```bash
crontab -e
# choose the one you want

# then enter the cronjob to run every 2 hours and create a log file
0 */2 * * * /bin/bash /home/kali/VulnSearch/update_automation.sh >> /home/kali/VulnSearch/update_cron.log 2>&1

# check your edit with
crontab -l
```
