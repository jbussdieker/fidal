import vcr
import requests

def get_vcr(name, filter_headers=[], filter_query_parameters=[]):
    return vcr.VCR(path_transformer=vcr.VCR.ensure_suffix('.yaml'),
                     cassette_library_dir='tests/fixtures/cassettes/%s' % name,
                     decode_compressed_response=True,
                     filter_query_parameters=['token', 'api_key', 'apiKey'],
                     filter_headers=['APCA-API-KEY-ID', 'APCA-API-SECRET-KEY'])
