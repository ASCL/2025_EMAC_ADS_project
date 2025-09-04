#! /usr/bin/env python

import sys
import json
import requests


# Replace with the actual DOI or record ID of the code you're interested in
# For example, using a concept DOI to get the latest version

# https://doi.org/<RID>

record_identifier = "10.5281/zenodo.11551599"   # NEMO (ocea)
record_identifier = "10.5281/zenodo.3466444"    # Pencil  -> 3947506  (concept: 3466444)
record_identifier = "10.5281/zenodo.3947506"    # ok
record_identifier = "10.5281/zenodo.16304"      # (later: 3637961)    https://zenodo.org/records/16304
record_identifier = "10.5281/zenodo.3637961"    # ok

# MESA (13353788) is another example where only the most recent DOI can be programmaitclaly asked for the concept DOI
# same for other way around:  concept DOI link goes to most recent
#      a={"doi": {"client": "datacite", "identifier": "10.5281/zenodo.592696", "provider": "datacite"}}
#      grep data-record-parent-pids zenodo.16304
#          a['doi']['identifier']
# Out[2]: '10.5281/zenodo.592696'

if len(sys.argv) > 1:
    record_identifier = "10.5281/zenodo.%s" % sys.argv[1]

print(f"# Trying https://doi.org/{record_identifier}")

# Construct the API URL for the record
# For a specific record ID, use: f"https://zenodo.org/api/records/{record_identifier}"
# For a concept DOI (to get the latest version), use: f"https://zenodo.org/api/records?q=doi:{record_identifier}"
api_url = f"https://zenodo.org/api/records?q=doi:{record_identifier}"
print("URL:",api_url)


try:
    response = requests.get(api_url)
    response.raise_for_status()  # Raise an exception for HTTP errors (4xx or 5xx)

    data = response.json()

    print("ALL",data)

    # If searching by concept DOI, the result will be a list of records,
    # and we usually want the first one (latest version).
    if data and 'hits' in data and data['hits']['hits']:
        code_info = data['hits']['hits'][0] # Get the latest version

        print("Information about the code:")
        print(f"Title: {code_info.get('metadata', {}).get('title')}")
        print(f"DOI: {code_info.get('doi')}")
        print(f"CONCEPT_DOI: {code_info.get('conceptdoi')}")
        print(f"Description: {code_info.get('metadata', {}).get('description')[:200]}...") # Truncate for brevity
        print(f"Creators: {', '.join([c.get('name') for c in code_info.get('metadata', {}).get('creators', [])])}")
        print(f"Publication Date: {code_info.get('metadata', {}).get('publication_date')}")
        print(f"Files:")
        for file in code_info.get('files', []):
            print(f"  - {file.get('key')} (Size: {file.get('size')} bytes)")
    else:
        print(f"No record found for identifier: {record_identifier}")

except requests.exceptions.RequestException as e:
    print(f"Error fetching data: {e}")
