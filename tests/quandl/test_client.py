import unittest

from tests.helper import get_vcr
from fidal.quandl.client import Client

vcr = get_vcr("quandl")

class TestPolygonClient(unittest.TestCase):
    def setUp(self):
        self.client = Client()

    @vcr.use_cassette()
    def test_request_error_code_handling(self):
        self.assertRaises(Exception, self.client.request, "foo/bar")
