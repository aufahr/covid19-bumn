import csv
import inspect
import os
import sys

from csv import DictReader
from template import all_website

# append project path
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

kab_web_data = []

for web in all_website:
    kab_web_data.append(web.execute())

with open('names.csv', 'w', newline='') as csvfile:
    writer = csv.DictWriter(csvfile,
                            fieldnames=['region', 'scraped_datetime', 'last_updated', 'odp', 'odp_done', 'total_odp',
                                        'pdp', 'pdp_death', 'pdp_done', 'total_pdp',
                                        'positive', 'positive_recovered', 'positive_death', 'total_positive'])
    writer.writeheader()
    for data in kab_web_data:
        writer.writerow(data)
