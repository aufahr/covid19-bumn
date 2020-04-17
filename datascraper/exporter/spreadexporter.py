import gspread_db
import datetime
from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build
import time


def export(web_data):
    # You can learn more about how to register your
    # service and get API credentials at:
    # https://gspread.readthedocs.io/en/latest/oauth2.html
    spreadsheet_key = '1MGRDgBecXKN1qtx7dkAx5z183wujFvHXjpN0smr5Tag'

    scope = ['https://spreadsheets.google.com/feeds']

    credentials = Credentials.from_service_account_file("datascraper/exporter/creds.json", scopes=scope)

    client = gspread_db.authorize(credentials)
    db = client.open_by_key(spreadsheet_key)

    if 'data' not in db:
      try:
        db.create_table(
            table_name='data',
            header=[
                'update_id',
                'source_type',
                'region',
                'scraped_datetime',
                'last_updated',
                'odp',
                'odp_done',
                'total_odp',
                'pdp',
                'pdp_death',
                'pdp_done',
                'total_pdp',
                'positive',
                'positive_recovered',
                'positive_death',
                'total_positive',
            ])
      except Exception as e:
        pass

    data_db = db['data']

    for d in web_data:
        update_id = "{}-{}-{}".format(str(d['scraped_datetime']).split(" ")[0],
        d['source_type'], d['region'])
        
        d['update_id'] = update_id

        if len(data_db.select('update_id', update_id)) > 0:
            data_db.update('update_id', update_id, new_values=d)
        else:
            data_db.insert(d)
        
        time.sleep(1)
  

    print("done")
