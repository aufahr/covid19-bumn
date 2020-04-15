import csv
import inspect
import os
import sys
import datetime
from template import all_website
from exporter import spreadexporter

kab_web_data = []

for web in all_website:
    kab_web_data.append(web.execute())


# update to csv

# update to google drive 
print("update to google drive : ")
spreadexporter.export(kab_web_data)

