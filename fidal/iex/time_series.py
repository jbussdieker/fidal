from fidal.iex.client import Client

def fetch(rec_id=None, rec_key=None, **kwargs):
    if rec_id is None or rec_key is None:
        return Client().request("time-series", kwargs)
    return Client().request("time-series/%s/%s" % (rec_id, rec_key), kwargs)
