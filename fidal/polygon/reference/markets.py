from fidal.polygon.client import Client

def fetch():
    return Client().request("reference/markets")
