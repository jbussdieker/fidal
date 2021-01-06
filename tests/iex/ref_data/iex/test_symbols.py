import unittest
import vcr
import requests

from unittest.mock import MagicMock, patch

from fidal.iex.ref_data.iex.symbols import fetch

iexvcr = vcr.VCR(path_transformer=vcr.VCR.ensure_suffix('.yaml'),
                 cassette_library_dir='tests/fixtures/cassettes/iex/ref_data/iex',
                 decode_compressed_response=True,
                 filter_query_parameters=['token'])

class TestIEXRefDataIEXSymbols(unittest.TestCase):
    @iexvcr.use_cassette()
    def test_fetch(self):
        with patch('logging.debug') as mock_logging:
            resp = fetch()
            self.assertEqual(len(resp), 9546)
            mock_logging.assert_called_once_with("MESSAGES USED: 0")
