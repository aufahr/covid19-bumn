import datetime

import requests


def call():
    url = "https://covid19.bandung.go.id/api/covid19bdg/v1/covid/list?date="

    payload = {}
    headers = {
      'Connection': 'keep-alive',
      'Pragma': 'no-cache',
      'Cache-Control': 'no-cache',
      'authorization': 'RkplDPdGFxTSjARZkZUYi3FgRdakJy',
      'Sec-Fetch-Dest': 'empty',
      'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36',
      'content-type': 'application/json',
      'Accept': '*/*',
      'Sec-Fetch-Site': 'same-origin',
      'Sec-Fetch-Mode': 'cors',
      'Referer': 'https://covid19.bandung.go.id/',
      'Accept-Language': 'en-US,en;q=0.9',
      'Cookie': '_ga=GA1.3.1636756225.1586935747; _gid=GA1.3.864194120.1586935747'
    }

    response = requests.request("GET", url, headers=headers, data = payload)


    data = response.json()['data']

    result = {
        'scraped_datetime': datetime.datetime.now(),
        'last_updated': data['date'],
        'odp': data['total_odp'],
        'odp_done': data['total_odp_selesai'],
        'pdp': data['total_pdp'],
        'pdp_done': data['total_pdp_selesai'],
        'positive': data['total_positif'] -
                    (data['total_sembuh'] + data['total_meninggal']),
        'positive_recovered': data['total_sembuh'],
        'positive_death': data['total_meninggal']
    }

    return result