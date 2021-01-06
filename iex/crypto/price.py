from iex.client import Client

def fetch(symbol):
    return Client().request("crypto/{symbol}/price".format(symbol=symbol))
