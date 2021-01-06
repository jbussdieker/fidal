import unittest
import vcr
import requests

from unittest.mock import MagicMock, patch

from fidal.intrinio.client import Client

iexvcr = vcr.VCR(path_transformer=vcr.VCR.ensure_suffix('.yaml'),
                 cassette_library_dir='tests/fixtures/cassettes/intrinio',
                 decode_compressed_response=True,
                 filter_query_parameters=['api_key'])

class TestIntrinioClient(unittest.TestCase):
    def setUp(self):
        self.client = Client()

    @iexvcr.use_cassette()
    def test_request(self):
        resp = self.client.request("stock_exchanges")
        self.assertEqual(len(resp), 2)

    @iexvcr.use_cassette()
    def test_request_error_code_handling(self):
        self.assertRaises(Exception, self.client.request, "foo/bar")
