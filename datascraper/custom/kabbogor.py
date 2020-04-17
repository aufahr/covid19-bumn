import datetime


import requests


def kab_bogor_call():
    url = "https://geoportal.bogorkab.go.id/server/rest/services/Hosted/Covid_19/FeatureServer/0/query?where=1%3D1&outFields=*&f=pjson"

    payload = {}
    headers = {
        'authority': 'geoportal.bogorkab.go.id',
        'pragma': 'no-cache',
        'cache-control': 'no-cache',
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'sec-fetch-dest': 'empty',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36',
        'origin': 'https://covid-19.bogorkab.go.id',
        'sec-fetch-site': 'same-site',
        'sec-fetch-mode': 'cors',
        'referer': 'https://covid-19.bogorkab.go.id/',
        'accept-language': 'en-US,en;q=0.9',
        'Cookie': 'AGS_ROLES="419jqfa+uOZgYod4xPOQ8Q=="'
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    res = response.json()

    odp = 0
    odp_done = 0
    pdp = 0
    pdp_done = 0
    pdp_death = 0
    positive_death = 0
    positive = 0
    positive_recovered = 0

    for item in res['features']:
        odp = add(odp, item['attributes']['odp'])
        odp_done = add(odp_done, item['attributes']['odp_selesai'])
        pdp = add(item['attributes']['pdp'], pdp)
        pdp_done = add(pdp_done, item['attributes']['pdp_selesai'])
        pdp_death = add(pdp_death, item['attributes']['pdp_meninggal'])
        positive = add(positive, item['attributes']['aktif'])
        positive_death = add(positive_death,item['attributes']['meninggal'])
        positive_recovered = add(positive_recovered, item['attributes']['recovered'])

    return {
        'scraped_datetime' : str(datetime.datetime.now()),
        'last_updated' : None,
        'odp': odp,
        'odp_done': odp_done,
        'pdp': pdp,
        'pdp_done': pdp_done,
        'pdp_death': pdp_death,
        'positive': positive,
        'positive_death': positive_death,
        'positive_recovered': positive_recovered
    }

def add(a, b):
    return (a or 0) + (b or 0)
