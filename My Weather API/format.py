import json

def format_data(data):
    keys = ["queryCost", "latitude", "longitude", "resolvedAddress", "address", "timezone", "tzoffset"]
    new_data = {}
    for k in keys:
        if isinstance(data[k], float):
            new_data[k] = str(data[k])
        else:
            new_data[k] = data[k]
    return new_data