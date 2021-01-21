from fidal.iex.client import client

def fetch(symbols):
    return client.request("stock/market/cash-flow", {"symbols": symbols})
