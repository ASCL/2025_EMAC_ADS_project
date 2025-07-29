#! /usr/bin/env python
#

#    "2507-004": {"bibcode": "2024JOSS....9.6972C", "ascl_id": "2412.025", "link": "https://emac.gsfc.nasa.gov?cid=2507-004", "name": "squishyplanet"},
#    ...
#    "2207-147": {"bibcode": null, "ascl_id": "2207.014", "link": "https://emac.gsfc.nasa.gov?cid=2207-147", "name": "petitRADTRANS"}
 
import json

jname = "emac.json"

try:
    with open(jname, 'r') as f:
        data = json.load(f)    # get dict
    keys = list(data.keys())
    keys.sort()
    
    for k in keys:
        d = data[k]
        print(k,d["name"])

except FileNotFoundError:
    print(f"Error: {jname} not found. Please ensure the file exists in the correct directory.")
except json.JSONDecodeError:
    print(f"Error: Could not decode JSON from {jname}. The file may be malformed.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
