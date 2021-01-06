from fin.iex.client import Client

def fetch(symbols):
    return Client().request("stock/market/advanced-stats", {"symbols": symbols})
