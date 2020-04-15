import datetime

import requests

def add(a, b):
    return (a or 0) + (b or 0)

def call():
    url = "https://covid19-public.digitalservice.id/api/v1/rekapitulasi/jabar?level=kab"

    payload = {}
    headers = {
        'authority': 'covid19-public.digitalservice.id',
        'pragma': 'no-cache',
        'cache-control': 'no-cache',
        'accept': 'text/html, */*; q=0.01',
        'sec-fetch-dest': 'empty',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36',
        'origin': 'https://covid19.garutkab.go.id',
        'sec-fetch-site': 'cross-site',
        'sec-fetch-mode': 'cors',
        'referer': 'https://covid19.garutkab.go.id/',
        'accept-language': 'en-US,en;q=0.9',
        'Cookie': '__cfduid=d4ee9b30a4df5d75f6c01955caec327e41586922838'
    }

    response = requests.request("GET", url, headers=headers, data=payload)


    data = list(filter(lambda x: x['kode_kab'] == '3205', response.json()['data']['content']))[0]


    result = {
            'scraped_datetime' : datetime.datetime.now(),
            'last_updated' : None,
            'odp': data['odp_proses'],
            'odp_done' : data['odp_selesai'],
            'pdp': data['pdp_proses'],
            'pdp_done': data['pdp_selesai'],
            'positive': data['positif'],
            'positive_death': data['meninggal'],
            'positive_recovered': data['sembuh']
    }

    return result