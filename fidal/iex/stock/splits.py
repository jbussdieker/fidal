from fidal.iex.client import Client

def fetch(symbols):
    return Client().request("stock/market/splits/5y", {"symbols": symbols})
