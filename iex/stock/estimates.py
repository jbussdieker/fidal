from iex.client import Client

def fetch(symbols):
    return Client().request("stock/market/estimates", {"symbols": symbols})
