import unittest
import vcr
import requests

from unittest.mock import MagicMock, patch

from fidal.iex.client import Client

iexvcr = vcr.VCR(path_transformer=vcr.VCR.ensure_suffix('.yaml'),
                 cassette_library_dir='tests/fixtures/cassettes/iex',
                 decode_compressed_response=True,
                 filter_query_parameters=['token'])

class TestIEXClient(unittest.TestCase):
    def setUp(self):
        self.client = Client()

    @iexvcr.use_cassette()
    def test_request(self):
        with patch('logging.debug') as mock_logging:
            resp = self.client.request("ref-data/iex/symbols")
            self.assertEqual(len(resp), 9546)
            mock_logging.assert_called_once_with("MESSAGES USED: 0")

    @iexvcr.use_cassette()
    def test_request_error_code_handling(self):
        self.assertRaises(Exception, self.client.request, "foo/bar")
