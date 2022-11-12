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
    print(f'Start process to import {BOUNTY_LOCATION_CSV} into {BOUNTY_LOCATION_DB.split("/")[-1]}')
    with conn:
        cur.execute("DROP TABLE IF EXISTS bounty_locations")
        print('Existing table found. Table will be recreated.')
        cur.execute("""CREATE TABLE bounty_locations (
                        "shikigami_name" TEXT NOT NULL COLLATE NOCASE,
                        "shikigami_image" TEXT NOT NULL,
                        "mystery_clues" TEXT COLLATE NOCASE,
                        "explorations" TEXT,
                        "secrets" TEXT,
                        "souls" TEXT,
                        "encounters" TEXT,
                        "others" TEXT,
                        "challenge_tickets" TEXT);""")
        print('Table created.')

    # with open(csv_file, 'r', newline='\n', encoding='utf-8') as csv_file:
    with open(csv_file, 'r', encoding='utf-8') as csv_file:
        print(f'Reading {csv_file.name}.')
        reader = csv.reader(csv_file)
        next(reader, None)  # Skip header
        for field in reader:
            with conn:
                cur.execute("INSERT INTO bounty_locations VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)", field, )
        print(f'Completed importing of {csv_file.name} into table.')
    
    cur.close()
    conn.close()

csv_to_db(BOUNTY_LOCATION_CSV)
