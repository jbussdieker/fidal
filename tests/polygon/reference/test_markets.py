import unittest

from tests.helper import get_vcr
from fidal.polygon.reference.markets import fetch

vcr = get_vcr("polygon/reference/markets")

class TestPolygonMarkets(unittest.TestCase):
    @vcr.use_cassette()
    def test_fetch(self):
        resp = fetch()
        self.assertEqual(len(resp), 2)
