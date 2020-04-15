import datetime
import csv

def export(data):
  with open("datascraper/results/{}".format(str(datetime.datetime.now())), 'w') as csvfile:
      writer = csv.DictWriter(
          csvfile,
          fieldnames=[
              'source_type',
              'region', 'scraped_datetime', 'last_updated', 'odp', 'odp_done',
              'total_odp', 'pdp', 'pdp_death', 'pdp_done', 'total_pdp',
              'positive', 'positive_recovered', 'positive_death',
              'total_positive', 
          ])
      writer.writeheader()
      for d in data:
          writer.writerow(data)
