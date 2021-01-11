import requests
import csv
from io import StringIO, BytesIO
from fidal.quandl.client import Client

def fetch():
    client = Client()

    resp = client.request("datatables/WIKI/PRICES.csv", {"qopts.export": "true"})
    reader = csv.DictReader(StringIO(resp.text))
    rows = [dict(item) for item in reader]
    url = rows[0]['file.link']

    resp = requests.get(url)
    print(resp)
    return resp
