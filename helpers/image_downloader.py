import sqlite3

import requests

BOUNTY_LOCATION_DB = '../eternity.db'
conn = sqlite3.connect(BOUNTY_LOCATION_DB)
cur = conn.cursor()


def fetch_image_links():
    cur.execute("SELECT shikigami_image FROM bounty_locations")
    return cur.fetchall()


image_links = [link[0] for link in fetch_image_links()]

if not image_links:
    print('No links fetched.')
else:
    for link in image_links:
        filename = link.split('/')[-1]
        r = requests.get(link, allow_redirects=True)
        with open(filename, 'wb') as f:
            f.write(r.content)
        print(f'Downloaded {filename}')

cur.close()
conn.close()