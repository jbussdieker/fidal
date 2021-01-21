from fidal.alpaca.client import client

def fetch():
    return client.request("assets")
