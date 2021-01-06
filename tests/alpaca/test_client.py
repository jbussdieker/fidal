import unittest

from tests.helper import get_vcr
from fidal.alpaca.client import Client

vcr = get_vcr("alpaca")

class TestAlpacaClient(unittest.TestCase):
    def setUp(self):
        self.client = Client()

    @vcr.use_cassette()
    def test_request(self):
        resp = self.client.request("account")
        self.assertEqual(len(resp), 26)

    @vcr.use_cassette()
    def test_request_error_code_handling(self):
        self.assertRaises(Exception, self.client.request, "foo/bar")
