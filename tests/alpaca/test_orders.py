import unittest

from tests.helper import get_vcr
from fidal.alpaca.orders import fetch

vcr = get_vcr("alpaca/orders")

class TestAlpacaOrders(unittest.TestCase):
    @vcr.use_cassette()
    def test_fetch(self):
        resp = fetch()
        self.assertEqual(len(resp), 0)
