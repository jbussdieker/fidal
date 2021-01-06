import unittest

from tests.helper import get_vcr
from fidal.alpaca.account import fetch

vcr = get_vcr("alpaca/account")

class TestAlpacaAccount(unittest.TestCase):
    @vcr.use_cassette()
    def test_fetch(self):
        resp = fetch()
        self.assertEqual(len(resp), 26)
