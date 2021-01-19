from fidal.iex.client import Client

def fetch():
    return Client().request("time-series")
