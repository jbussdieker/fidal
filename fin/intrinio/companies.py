from fin.intrinio.client import Client

def fetch():
    return Client().request("companies")
