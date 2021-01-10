import unittest

from tests.helper import get_vcr
from fidal.alpaca.bars import fetch

vcr = get_vcr("alpaca/bars")

class TestAlpacaBars(unittest.TestCase):
    @vcr.use_cassette()
    def test_fetch(self):
        resp = fetch("AAT", timespan='day', limit=10)
        self.assertEqual(len(resp["AAT"]), 10)
