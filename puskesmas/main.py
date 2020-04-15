import googlemaps
from datetime import datetime
import csv

all_puskesmas = []
with open('puskesmas_jabar.csv', mode='r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=';')
    line_count = 0
    for row in csv_reader:
        line_count = line_count + 1
        if line_count is 1:
            continue
        else:
            all_puskesmas.append(row)


def find_phone_num(name):
    gmaps = googlemaps.Client(key='AIzaSyB-mZjUVb3Pl5LxmyXIS4SpK-J1_LL0Z3s')

    # Geocoding an address
    result = gmaps.places(query=name, type='health')

    print(result)

    id = result['results'][0]['place_id']
    place = gmaps.place(id)

    print()

    if 'formatted_phone_number' in place['result']:
        return place['result']['formatted_phone_number'], place

    else:
        return 'None', place


with open('puskesmas_result.csv', mode='w') as puskesmas_file:
    with open('puskesmas_result2.csv', mode='w') as puskesmas_file2:

        puskesmas_writer = csv.writer(puskesmas_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        puskesmas_writer2 = csv.writer(puskesmas_file2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)


        count = 0

        for puskesmas in all_puskesmas:
            count = count + 1
            if count > 673:
                try:
                    row = puskesmas
                    phone_num, place = find_phone_num('Puskesmas {}'.format(puskesmas[2]))
                    row.append(phone_num)
                    puskesmas_writer.writerow(row)
                    row.append(place)
                    puskesmas_writer2.writerow(row)
                except Exception as e :
                    print(e)
                    error_row = puskesmas
                    error_row.append('ERROR')
                    error_row.append('ERROR')
                    puskesmas_writer.writerow(error_row)
                    puskesmas_writer2.writerow(error_row)


