from fidal.iex.client import client

def fetch(symbols):
    return client.request("stock/market/company", {"symbols": symbols})
