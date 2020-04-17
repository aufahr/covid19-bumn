import re

def get_date(value):
    val = re.findall(r'\d{4}-\d{2}-\d{2}|\d{2} .+ \d{4}', value)
    return val[0] if len(val) > 0 else None

def get_number_only(value):
    val = re.findall(r'[\d|\.]+', value)
    return val[0].replace(".", "") if len(val) > 0 else None


def get_number_only2(value):
    val = re.findall(r'[\d|\.]+', value)
    return val[1].replace(".", "") if len(val) > 0 else None


def get_number_only3(value):
    val = re.findall(r'[\d|\.]+', value)
    return val[2].replace(".", "") if len(val) > 0 else None

def get_number_only4(value):
    val = re.findall(r'[\d|\.]+', value)
    return val[3].replace(".", "") if len(val) > 0 else None

def get_number_only5(value):
    val = re.findall(r'[\d|\.]+', value)
    return val[4].replace(".", "") if len(val) > 0 else None