import unittest
import vcr
import requests

from unittest.mock import MagicMock, patch

from fidal.polygon.reference.markets import fetch

iexvcr = vcr.VCR(path_transformer=vcr.VCR.ensure_suffix('.yaml'),
                 cassette_library_dir='tests/fixtures/cassettes/polygon/reference/markets',
                 decode_compressed_response=True,
                 filter_query_parameters=['apiKey'])

class TestPolygonMarkets(unittest.TestCase):
    @iexvcr.use_cassette()
    def test_fetch(self):
        resp = fetch()
        self.assertEqual(len(resp), 2)
