from fidal.iex.client import client

def fetch(symbol):
    return client.request("crypto/{symbol}/quote".format(symbol=symbol))
