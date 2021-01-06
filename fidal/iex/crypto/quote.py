from fidal.iex.client import Client

def fetch(symbol):
    return Client().request("crypto/{symbol}/quote".format(symbol=symbol))
