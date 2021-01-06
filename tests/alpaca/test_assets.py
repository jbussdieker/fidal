import unittest

from tests.helper import get_vcr
from fidal.alpaca.assets import fetch

vcr = get_vcr("alpaca/assets")

class TestAlpacaAssets(unittest.TestCase):
    @vcr.use_cassette()
    def test_fetch(self):
        resp = fetch()
        self.assertEqual(len(resp), 10704)
