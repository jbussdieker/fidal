from fin.alpaca.client import Client

def fetch():
    return Client().request("calendar")
