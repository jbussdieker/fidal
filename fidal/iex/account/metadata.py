from fidal.iex.client import client

def fetch():
    return client.request("account/metadata")
