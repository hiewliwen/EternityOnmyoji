import csv
import re

import requests
from bs4 import BeautifulSoup

BOUNTY_LOCATION_SITE = 'https://onmyojiguide.com/guide/bounty-list/'
BOUNTY_LOCATION_CSV = 'bounty_locations_scrape.csv'
SECRETS_KEYWORDS = ['wraith', 'umbrella', 'summer', 'shshio', 'aoandon', 'secret', 'maple', 'river', 'storm']


def web_to_csv():
    """
    Scrape the bounty locations from Onmyoji Guide.
    This CSV **NEEDS TO BE EDITED**. Replace names and spelling mistakes etc.
    https://onmyojiguide.com/guide/bounty-list/
    :return: None
    """
    with open(BOUNTY_LOCATION_CSV, 'w', newline='', encoding='utf-8', errors='ignore') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(
            ['Shikigami', 'Image Link', 'Mystery Clues', 'Chapters', 'Secrets', 'Souls', 'Encounters', 'Others'])

        source = requests.get(BOUNTY_LOCATION_SITE, headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'}).text
        soup = BeautifulSoup(source, 'lxml').find(class_='row-hover')
        # print(soup.prettify())

        for bounty_location in soup.find_all('tr'):
            # print(bounty_locations.prettify())

            shikigami_name = bounty_location.find(class_='column-1').text
            shikigami_name = re.sub(r' *- *', '', shikigami_name)
            # print(shikigami_name)

            shikigami_image = bounty_location.find('img')['src']
            # print(shikigami_image)

            try:
                mystery_clues = bounty_location.find(class_='column-2').text
                mystery_clues = re.sub(r' *- *', '', mystery_clues)
            except Exception as e:
                mystery_clues = 'None'
                print(e)
            # print(mystery_clues)

            locations = bounty_location.find(class_='column-3').text
            locations = locations.replace(';', '')

            chapters = ''
            secrets = ''
            souls = ''
            encounters = ''
            others = ''

            splitlocations = locations.splitlines(keepends=True)

            for location in splitlocations:
                if 'chapter' in location.lower():
                    chapters += location
                elif 'soul' in location.lower():
                    souls += location
                elif 'encounter' in location.lower():
                    encounters += location
                elif any(word in location.lower() for word in SECRETS_KEYWORDS):
                    secrets += location
                else:
                    others += location

            csv_writer.writerow(
                [shikigami_name, shikigami_image, mystery_clues, chapters, secrets, souls, encounters, others])

# web_to_csv()
