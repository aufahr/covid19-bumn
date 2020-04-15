
from datascraper.util import get_number_only2, get_number_only

def custom_cianjur_pdp_processor(value):
    all = get_number_only(value)
    dead = get_number_only2(value)
    return int(all) - int(dead)