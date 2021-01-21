import unittest
from unittest.mock import patch

from tests.helper import get_vcr
from fidal.quandl.datatables.wiki.prices import fetch, fetch_url

vcr = get_vcr("quandl/datatables/wiki/prices")

class TestQuandlDatatablesWikiPrices(unittest.TestCase):
    @vcr.use_cassette()
    def test_fetch_url(self):
        url = fetch_url()
        self.assertIn("https://quandl-production-datahub.s3.amazonaws.com/export/WIKI/PRICES/WIKI_PRICES", url)

    @vcr.use_cassette()
    def test_fetch(self):
        with patch("requests.get") as mock_get:
            resp = fetch()
            mock_get.assert_called_once()
