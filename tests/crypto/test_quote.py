import unittest
import vcr
import requests

from unittest.mock import MagicMock, patch

from iex.crypto.quote import fetch

iexvcr = vcr.VCR(path_transformer=vcr.VCR.ensure_suffix('.yaml'),
                 cassette_library_dir='tests/fixtures/cassettes/crypto/quote',
                 decode_compressed_response=True,
                 filter_query_parameters=['token'])

class TestStockCompany(unittest.TestCase):
    @iexvcr.use_cassette()
    def test_fetch(self):
        with patch('logging.debug') as mock_logging:
            resp = fetch("BTCUSD")
            self.assertEqual(len(resp), 11)
            mock_logging.assert_called_once_with("MESSAGES USED: 2")
