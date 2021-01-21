from fidal.iex.client import client

def fetch(symbols):
    return client.request("stock/market/balance-sheet", {"symbols": symbols})
