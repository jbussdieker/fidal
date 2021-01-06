from iex.client import Client

def fetch():
    return Client().request("ref-data/iex/symbols")
