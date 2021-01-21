from fidal.iex.client import client

def fetch():
    return client.request("ref-data/symbols")
