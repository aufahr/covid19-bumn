import datetime

import bs4
import requests
import re
import json

def call():
    site = requests.get('https://covid19.sukabumikota.go.id/new/index.php/welcome/grafik/2')

    page = bs4.BeautifulSoup(site.text,features="lxml")

    raw_js = page.select_one('body > script:nth-child(20)')

    data = json.loads("{" + "\"data\" : {}".format(re.findall('data\: (\[\ \{[\s\S]+\}\,\]),', str(raw_js))[0]).replace("\'", "\"")[0:-2] + "]}")['data']




    result = {
        'scraped_datetime': str(datetime.datetime.now()),
        'last_updated': data[-1]['period'],
        'odp': data[-1]['ODP_Dalam_Pantauan'],
        'odp_done': data[-1]['ODP_Selesai'],
        'pdp': data[-1]['PDP_Dalam_Pengawasan'],
        'pdp_done': data[-1]['PDP_Selesai'],
        'positive': data[-1]['Positif_Perawatan'],
        'positive_death': data[-1]['Positif_Meninggal'],
        'positive_recovered': data[-1]['Positif_Sembuh']
    }

    return result
