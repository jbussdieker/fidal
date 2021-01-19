from fidal.alpaca.client import Client

def fetch(symbols, timespan='day', limit=None, start=None, end=None, from_=None, until=None):
    client = Client()
    client.base_url = "https://data.alpaca.markets"
    client.version = "v1"
    return client.request("bars/{timespan}".format(timespan=timespan), {
        "limit": limit,
        "symbols": symbols,
        "start": start,
        "end": end,
        "from": from_,
        "until": until,
    })
