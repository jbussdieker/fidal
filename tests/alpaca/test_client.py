import unittest
import vcr
import requests

from unittest.mock import MagicMock, patch

from fin.alpaca.client import Client

iexvcr = vcr.VCR(path_transformer=vcr.VCR.ensure_suffix('.yaml'),
                 cassette_library_dir='tests/fixtures/cassettes/alpaca',
                 decode_compressed_response=True,
                 filter_headers=['APCA-API-KEY-ID', 'APCA-API-SECRET-KEY'])

class TestClient(unittest.TestCase):
    def setUp(self):
        self.client = Client()

    @iexvcr.use_cassette()
    def test_request(self):
        resp = self.client.request("account")
        self.assertEqual(len(resp), 26)

    @iexvcr.use_cassette()
    def test_request_error_code_handling(self):
        self.assertRaises(Exception, self.client.request, "foo/bar")
