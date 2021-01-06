import unittest

from tests.helper import get_vcr
from fidal.alpaca.calendar import fetch

vcr = get_vcr("alpaca/calendar")

class TestAlpacaCalendar(unittest.TestCase):
    @vcr.use_cassette()
    def test_fetch(self):
        resp = fetch()
        self.assertEqual(len(resp), 15136)
