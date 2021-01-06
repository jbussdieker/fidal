import unittest
import vcr
import requests

from unittest.mock import MagicMock, patch

from fidal.alpaca.account import fetch

iexvcr = vcr.VCR(path_transformer=vcr.VCR.ensure_suffix('.yaml'),
                 cassette_library_dir='tests/fixtures/cassettes/alpaca/account',
                 decode_compressed_response=True,
                 filter_headers=['APCA-API-KEY-ID', 'APCA-API-SECRET-KEY'])

class TestAlpacaAccount(unittest.TestCase):
    @iexvcr.use_cassette()
    def test_fetch(self):
        resp = fetch()
        self.assertEqual(len(resp), 26)
