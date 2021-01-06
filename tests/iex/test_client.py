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
            self.assertEqual(len(resp), 9546)
            mock_logging.assert_called_once_with("MESSAGES USED: 0")

    @vcr.use_cassette()
    def test_request_error_code_handling(self):
        self.assertRaises(Exception, self.client.request, "foo/bar")
