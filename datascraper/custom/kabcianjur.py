import re

def get_number_only(value):
    val = re.findall(r'\d+', value)
    return val[0] if len(val) > 0 else None


def get_number_only2(value):
    val = re.findall(r'\d+', value)
    return val[1] if len(val) > 0 else None


def custom_cianjur_pdp_processor(value):
    all = get_number_only(value)
    dead = get_number_only2(value)
    return int(all) - int(dead)