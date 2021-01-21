from fidal.polygon.client import client

def fetch():
    return client.request("reference/markets")
