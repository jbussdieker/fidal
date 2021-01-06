import unittest
from unittest.mock import MagicMock, patch

from tests.helper import get_vcr
from fidal.iex.stock.income import fetch

vcr = get_vcr('iex/stock/income')

class TestIEXStockIncome(unittest.TestCase):
    @vcr.use_cassette()
    def test_fetch(self):
        with patch('logging.debug') as mock_logging:
            resp = fetch("aapl,intc")
            self.assertEqual(len(resp), 2)
            mock_logging.assert_called_once_with("MESSAGES USED: 2000")
