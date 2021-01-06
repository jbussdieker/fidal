from fidal.iex.client import Client

def fetch(symbols):
    return Client().request("stock/market/cash-flow", {"symbols": symbols})
