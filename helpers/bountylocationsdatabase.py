import csv

import sqlite3

BOUNTY_LOCATION_CSV = 'bounty_locations.csv'
BOUNTY_LOCATION_DB = '../databases/eternity.db'
SECRETS_KEYWORDS = ['wraith', 'umbrella', 'summer', 'shshio', 'aoandon', 'secret', 'maple', 'river', 'storm']

conn = sqlite3.connect(BOUNTY_LOCATION_DB)
cur = conn.cursor()


def csv_to_db(csv_file):
    """
    Save CSV to SQLite DB.
    **REMEMBER TO USE THE EDITED CSV.**
    :param csv_file: (str) File name (with extension) of the CSV file to be saved.
    :return: None
    """
    with conn:
        cur.execute("DROP TABLE IF EXISTS bounty_locations")
        cur.execute("""CREATE TABLE bounty_locations (
                        "shikigami_name" TEXT NOT NULL COLLATE NOCASE,
                        "shikigami_image" TEXT NOT NULL,
                        "mystery_clues" TEXT COLLATE NOCASE,
                        "chapters" TEXT,
                        "secrets" TEXT,
                        "souls" TEXT,
                        "encounters" TEXT,
                        "others" TEXT,
                        "challenge_tickets" TEXT);""")

    with open(csv_file, 'r', newline='\n', encoding='utf-8') as csv_file:
        reader = csv.reader(csv_file)
        next(reader, None)  # Skip header
        for field in reader:
            with conn:
                cur.execute("INSERT INTO bounty_locations VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)", field, )


csv_to_db(BOUNTY_LOCATION_CSV)
