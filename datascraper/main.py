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

# kab_sukabumi datanya malah kota_sukabumi berarti harusnya kota_sukabumi gak usah manual DONE
# kab_cianjur ada tanggal tapi gak keambil
# kab_garut ada tanggal tapi gak keambil

# kab_tasikmalaya harusnya datanya triase tapi malah ngambil data kab_garut DONE

# kab_ciamis pdp_death dihitung di dalam pdp_done jadi harusnya total_pdp cuma pdp + pdp_done DONE

# kab_ciamis positive_recovered dan positive_death gak keambil DONE


# kab_sumedang odp dibedain pemantauan dan pengawasan jadi harusnya odp = odp_pemantauan + odp_pengawasan

# kab_karawang
# kota_tasikmalaya ada tanggal tapi gak keambil