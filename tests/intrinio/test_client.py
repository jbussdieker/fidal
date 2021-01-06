import unittest

from tests.helper import get_vcr
from fidal.intrinio.client import Client

vcr = get_vcr("intrinio")

class TestIntrinioClient(unittest.TestCase):
    def setUp(self):
        self.client = Client()

    @vcr.use_cassette()
    def xtest_request(self):
        resp = self.client.request("stock_exchanges")
        self.assertEqual(len(resp), 2)

    @vcr.use_cassette()
    def xtest_request_error_code_handling(self):
        self.assertRaises(Exception, self.client.request, "foo/bar")
