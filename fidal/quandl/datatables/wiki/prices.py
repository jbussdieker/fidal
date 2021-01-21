import requests
import csv
from io import StringIO, BytesIO
from fidal.quandl.client import client

def fetch():
    url = fetch_url()
    return requests.get(url)

def fetch_url():
    resp = client.request("datatables/WIKI/PRICES.csv", {"qopts.export": "true"})
    reader = csv.DictReader(StringIO(resp.text))
    rows = [dict(item) for item in reader]
    url = rows[0]['file.link']
    return url
