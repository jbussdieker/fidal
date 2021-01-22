import unittest
from unittest.mock import MagicMock, patch

from tests.helper import get_vcr
from fidal.iex.client import Client

vcr = get_vcr('iex')

class TestIEXClient(unittest.TestCase):
    def setUp(self):
        self.client = Client()

    @vcr.use_cassette()
    def test_request(self):
        with patch('logging.debug') as mock_logging:
            resp = self.client.request("ref-data/iex/symbols")
            self.assertEqual(len(resp), 9552)
            mock_logging.assert_called_once_with("MESSAGES USED: 0")

    @vcr.use_cassette()
    def test_request_error_code_handling_wrong_path(self):
        self.assertRaisesRegex(Exception, "Not Found", self.client.request, "foo/bar")

    @vcr.use_cassette()
    def test_request_error_code_handling_auth(self):
        self.client.token = "jibberish"
        self.assertRaisesRegex(Exception, "The API key provided is not valid.", self.client.request, "ref-data/iex/symbols")

    @vcr.use_cassette()
    def test_request_error_code_handling_missing_symbol(self):
        self.assertRaisesRegex(Exception, "Unknown symbol", self.client.request, "stock/market/company?symbols=FOOBARSTOCK")
