from fidal.alpaca.client import Client

def fetch(symbols, timespan='day', limit=10):
    client = Client()
    client.base_url = "https://data.alpaca.markets"
    client.version = "v1"
    return client.request("bars/{timespan}".format(timespan=timespan), {"limit": limit, "symbols": symbols})
