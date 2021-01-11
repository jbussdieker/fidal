import unittest

from tests.helper import get_vcr
from fidal.quandl.datatables.wiki.prices import fetch

vcr = get_vcr("quandl/datatables/wiki/prices")

class TestQuandlDatatablesWikiPrices(unittest.TestCase):
    @vcr.use_cassette()
    def xtest_fetch(self):
        resp = fetch()
        self.assertEqual(len(resp), 2)
