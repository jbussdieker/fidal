from fidal.iex.client import client

def fetch(symbols):
    return client.request("stock/market/splits/5y", {"symbols": symbols})
